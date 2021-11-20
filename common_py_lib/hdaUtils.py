# -----------------------------------------------------------
# hdaUtils.py
# v.1.0
# Updated: 20211120
# Houdini version: 18.5.563, Python 3
# Redshift version: 3.0.46
# -----------------------------------------------------------

"""
Custom Houdini utilities for use with callback scripts in HDAs.
"""

#************************************************************

# -----------------------------------------------------------
# TOGGLE CUSTOM OUTPUTS ))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

import hou

def toggleOutput(parmName):
    """

    Function to toggle connection and custom outputs in HDA.

    Python Callback Script in parameter:
        kwargs['node'].hdaModule().toggleOutput(kwargs['parm'].name())

    """

    node = hou.pwd()

    # Store current value of parm.
    parmValue = node.evalParm(parmName)
    # Example parm name: "enable_output_0".
    # Split parm name to retain only the ending portion of the string.
    outputName = parmName.split("_" ,1)[-1]
    # Extract index number from parm name string.
    index = int(outputName.rsplit("_" ,1)[-1])

    # Enable editable nodes configured under HDA's Node tab.
    node.allowEditingOfContents(propagate = False)

    # Access relevant nodes within HDA; these are the ones listed in the
    # HDA's Node tab under editable.
    nullNode = node.item("OUT_%s" % outputName)
    suboutNode = node.item("suboutput")

    # Evaluate number of nodes attached to current node's outputs.
    outputState = len(nullNode.outputs())

    # If greater than 0, then node is connected to suboutNode.
    if outputState > 0:
        # Detach nullNode from suboutNode.
        suboutNode.setInput(index, None, 0)
    else:
        # If not connected, then connect nullNode to corresponding index
        # outlet on suboutNode.
        suboutNode.setInput(index, nullNode, 0)

    # Debug log
    print("***************************************")
    # print("[%d]ParmName: %s" % (index, outputName))
    # print("ParmValue: %s" % parmValue)
    print("NullNode: %s; num of outputs: %d" % (nullNode, outputState))

# -----------------------------------------------------------
# TOGGLE CUSTOM OUTPUTS ))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
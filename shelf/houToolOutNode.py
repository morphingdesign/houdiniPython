# -----------------------------------------------------------
# houToolOutNode.py
# v.1.0
# Updated: 20210402
# ----------------------------------------------------------

"""
Custom shelf tool to generate a Null node with user-defined
naming. Naming convention coordinated with uppercase for quick
recall. Node color and shape coordinated with production
standards.
"""

import objecttoolutils

# -----------------------------------------------------------
# NULL NODE ))))))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
# Generate Null node
kwargs['bbox'] = hou.BoundingBox(-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)
objecttoolutils.genericTool(kwargs, 'null')

# Collect the currently selected node
curNode = kwargs['pane'].currentNode()
# -----------------------------------------------------------
# NULL NODE ))))))))}}))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# USER INPUT )))))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
# Ask user for label to be used for the OUT node. The `readInput()`
# method returns a tuple, with the 2nd element [1] being the
# user-specified label.
name = hou.ui.readInput("Type node name", title="Out Node Name")[1]
# -----------------------------------------------------------
# USER INPUT )))))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# FORMATTING )))))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
# Label Formatting
# Format the label to be all uppercase for quick recall.
name = name.upper()
# Replaces blank spaces in the input name with an underscore.
# Note that without this syntax, the null node fails to generate.
name = name.replace(" ", "_")

# Set the name variable, color, and display/render flags for
# the null node being created.
curNode.setName(name)
curNode.setColor(hou.Color(1.0, 0.0, 0.0))
curNode.setDisplayFlag(True)
curNode.setRenderFlag(True)
# -----------------------------------------------------------
# FORMATTING )))))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
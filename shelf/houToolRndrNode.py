# -----------------------------------------------------------
# houToolRndrNode.py
# v.1.0
# Updated: 20210319
# ----------------------------------------------------------

"""
Custom shelf tool for use to generate a Render Geo node with
user-defined naming. Naming convention coordinated with
Redshift ROP object list of render-ready geo.
"""

import objecttoolutils
from common_py_lib import utils

# -----------------------------------------------------------
# OBJECT NODE ))))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
# Generates node
objecttoolutils.genericTool(kwargs, 'geo')

# Return the currently selected node
render = kwargs['pane'].currentNode()

# Ask user for name for the RNDR node's suffix
# Since name is a tuple, we need the 2nd value, hence the [1]
name = hou.ui.readInput("Type node name", title="Render Geo Node Name")[1]
name = "RNDR_" + name.upper()

# Replaces blank spaces in the input name with an underscore
# Without this, the null node fails
name = name.replace(" ", "_")

# Assign name variable to the node
render.setName(name)

# Sets node's color to blue
render.setColor(utils.eof_color)

# Sets the node shape to be a circle
render.setUserData('nodeshape', 'circle')

# Disable selection flag
render.setSelectableInViewport(False)

# -----------------------------------------------------------
# OBJECT NODE ))))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# NULL OUT NODE ))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
renOut = render.createNode("null", node_name="OUT")
renOut.setColor(utils.eof_color)
# -----------------------------------------------------------
# NULL OUT NODE ))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
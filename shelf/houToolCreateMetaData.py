# -----------------------------------------------------------
# houToolCreateMetaData.py
# v.1.0
# Updated: 20211109
# ----------------------------------------------------------

"""
Shelf Tool Name: Set Creator
Custom shelf tool to store creation metadata to selected node/s
in its built-in creatorState.
"""

import hou

# Modify creator metadata for selected nodes in this project file.
# Attribute the hipname.

# -----------------------------------------------------------
# LOCAL VARIABLES ))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

hipname = hou.text.expandString("$HIPNAME")
hipfile = hou.text.expandString("$HIPFILE")
nodes = hou.selectedNodes()

# -----------------------------------------------------------
# LOCAL VARIABLES ))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# SET ATTRIBUTE ))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

for node in nodes:
    # NODE CREATOR STATE ****************************
    node.setCreatorState(hipname)
    node.setBuiltExplicitly(False)

# -----------------------------------------------------------
# SET ATTRIBUTE ))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
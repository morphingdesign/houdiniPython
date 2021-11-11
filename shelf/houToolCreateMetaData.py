# -----------------------------------------------------------
# houToolCreateMetaData.py
# v.1.0
# Updated: 20211111
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
# SETUP TAB & PARM )))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

folder = hou.FolderParmTemplate("folder", "Metadata")
folder.setFolderType(hou.folderType.Tabs)
folder.addParmTemplate(hou.StringParmTemplate("originhip", "Origin", 1))

# -----------------------------------------------------------
# SETUP TAB & PARM )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# SET ATTRIBUTE ))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

for node in nodes:
    # NODE CREATOR STATE ****************************
    node.setCreatorState(hipname)
    node.setBuiltExplicitly(False)

    # PARTIALLY VISIBLE METADATA PARAMETER **********
    group = node.parmTemplateGroup()
    group.append(folder)
    # Add parm to node's parm group.
    node.setParmTemplateGroup(group)
    node.parm("originhip").set(hipname)

# -----------------------------------------------------------
# SET ATTRIBUTE ))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
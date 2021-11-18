# -----------------------------------------------------------
# houToolCreateMetaData.py
# v.1.0
# Updated: 20211118
# ----------------------------------------------------------

"""
Shelf Tool Name: Set Creator
Custom shelf tool to store creation metadata to selected node/s
in its built-in creatorState and user data.
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

folder = hou.FolderParmTemplate("folder", "Metadata",
                                tab_conditionals={hou.parmCondType.DisableWhen: '{ origin != /"/" }'})
folder.setFolderType(hou.folderType.Tabs)
folder.addParmTemplate(hou.StringParmTemplate("origin", "Origin", 1))

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
    # Check if parm already exists.
    if (node.parm("origin")):
        print("Parameter already created for %s." % node.name())
    else:
        group = node.parmTemplateGroup()
        group.append(folder)
        # Add parm to node's parm group.
        node.setParmTemplateGroup(group)
        node.parm("origin").set(hipname)

# -----------------------------------------------------------
# SET ATTRIBUTE ))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# PER NODE USER DATA )))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# Reference: https://www.sidefx.com/docs/houdini/hom/nodeuserdata.html

for node in nodes:
    # Prefix of "nodeinfo_" allows for key/value dictionary entry
    # to be viewable in node's info dialog box.
    node.setUserData("nodeinfo_Origin", hipname)

# -----------------------------------------------------------
# PER NODE USER DATA  ))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
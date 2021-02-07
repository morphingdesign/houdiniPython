# -----------------------------------------------------------
# houObjMergeAdvNode.py
# v.1.0
# Updated: 20210206
# ----------------------------------------------------------

"""
Custom shelf tool to store selected node/s to clipboard and
have them available for pasting into same network or other
networks as individual Object Merge nodes linked to
originally copied node/s. By default, operation nests
reference path as absolute, but tool includes kwargs for CTRL
to specify path as relative.
"""

# Check if node/s are selected by user; if not, NOP.
if hou.selectedNodes():
    # -----------------------------------------------------------
    # LOCAL VARIABLES ))))))))))))))))))))))))))))))))))))) START
    # -----------------------------------------------------------
    ctrlCheck = kwargs["ctrlclick"]
    selectedNode = hou.selectedNodes()[0]
    parent = selectedNode.parent()
    defaultGreen = hou.Color(0.302,0.525,0.114)
    # -----------------------------------------------------------
    # LOCAL VARIABLES ))))))))))))))))))))))))))))))))))))))) END
    # -----------------------------------------------------------

    # -----------------------------------------------------------
    # NODE SETUP )))))))))))))))))))))))))))))))))))))))))) START
    # -----------------------------------------------------------
    objMerge = selectedNode.parent().createNode("object_merge")
    objMerge.setColor(defaultGreen)
    # -----------------------------------------------------------
    # NODE SETUP )))))))))))))))))))))))))))))))))))))))))))) END
    # -----------------------------------------------------------

    # -----------------------------------------------------------
    # CONFIGURE PARAMETERS )))))))))))))))))))))))))))))))) START
    # -----------------------------------------------------------
    # Set Transform param to be 'Into This Object'.
    objMerge.parm("xformtype").set(1)

    # Check if kwargs is enabled by CTRL key.
    if not ctrlCheck:
        # Set to absolute path.
        objMerge.parm("objpath1").set(selectedNode.path())
    else:
        # Set to relative path.
        objMerge.parm("objpath1").set("../" + selectedNode.name())

    # Set name for newly created Object Merge node.
    if parent.node("./get_%s" % selectedNode.name()) == None:
        objMerge.setName("get_%s" % selectedNode.name())
    # -----------------------------------------------------------
    # CONFIGURE PARAMETERS )))))))))))))))))))))))))))))))))) END
    # -----------------------------------------------------------

    # -----------------------------------------------------------
    # COPY/PASTE OPERATION )))))))))))))))))))))))))))))))) START
    # -----------------------------------------------------------
    # Position new node relative to corresponding linked node.
    selectedNodePos = selectedNode.position()
    pos = hou.Vector2(selectedNodePos[0], selectedNodePos[1] - 1)
    objMerge.setPosition(pos)
    # Store newly positioned Object Merge node/s to clipboard
    hou.copyNodesToClipboard((objMerge,))
    # Destroy aforementioned node/s
    objMerge.destroy()
    # With the Object Merge nodes stored in the clipboard, user
    # can now paste them in current geo network or other geo
    # network, as needed.
    # -----------------------------------------------------------
    # COPY/PASTE OPERATION )))))))))))))))))))))))))))))))))) END
    # -----------------------------------------------------------

# To mitigate potential error when shelf tool is enabled without
# a selected node or collection of selected nodes, execute the
# following as no operation (NOP).
pass
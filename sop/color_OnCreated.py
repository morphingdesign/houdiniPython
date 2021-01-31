# -----------------------------------------------------------
# color_OnCreated.py
# v.1.0
# Updated: 20210130
# ----------------------------------------------------------

"""
Custom script to set node color from user-defined color
parameter by way of a hidden parallel color parameter and
Python script callback.
"""
from common_py_lib import utils

# -----------------------------------------------------------
# GLOBAL VARIABLES )))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
node = kwargs['node']
# -----------------------------------------------------------
# GLOBAL VARIABLES )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# CUSTOMIZATIONS )))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
# Instantiate custom folder for parameter to hold color param
# values and script callback for when color values in node's
# default params are updated.
customFolder = hou.FolderParmTemplate('custom', 'Custom')
customFolder.setFolderType(hou.folderType.Simple)
tempGroup = node.parmTemplateGroup()
# Add parameter to parm template object, set script callback
# and associated tags, as well as set to be hidden.
customFolder.addParmTemplate(hou.FloatParmTemplate("active_color", "Active Color", 3, default_value=(0, 0, 0), is_hidden=True, script_callback="hou.pwd().setColor(hou.Color((hou.pwd().evalParm('colorr'), hou.pwd().evalParm('colorg'), hou.pwd().evalParm('colorb'))))", script_callback_language=hou.scriptLanguage.Python))
# Add parm template object to node's UI.
tempGroup.append(customFolder)
node.setParmTemplateGroup(tempGroup)

# Set channel references to node's color params in new
# params so that script callback activates upon change.
node.parm('active_colorx').setExpression('ch("./colorr")')
node.parm('active_colory').setExpression('ch("./colorg")')
node.parm('active_colorz').setExpression('ch("./colorb")')
# -----------------------------------------------------------
# CUSTOMIZATIONS )))))))))))))))))))))))))))))))))}}))))) END
# -----------------------------------------------------------
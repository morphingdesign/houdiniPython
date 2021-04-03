# -----------------------------------------------------------
# houToolCtrlNode.py
# v.1.0
# Updated: 20210402
# ----------------------------------------------------------

"""
Script for use to generate a Control Panel node by using the
Null node as a basis, but with additional variations to streamline
creation process of a control panel for parameters.
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
# Ask user for label suffix to be used for the CTRL node. The
# `readInput()` method returns a tuple, with the 2nd element
# [1] being the user-specified label.
name = hou.ui.readInput("Type node name", title="Ctrl Node Name")[1]
# -----------------------------------------------------------
# USER INPUT )))))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# LABEL FORMATTING )))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
# Append prefix and uppercase for quick recall.
name = "CTRL_" + name.upper()
# Replaces blank spaces in the input name with an underscore.
# Note that without this syntax, the null node fails to generate.
name = name.replace(" ", "_")

# Set the name variable, color, and display/render flags for
# the null node being created.
curNode.setName(name)
curNode.setColor(hou.Color(0.094, 0.369, 0.69))
curNode.setUserData('nodeshape', 'circle')
# -----------------------------------------------------------
# LABEL FORMATTING )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# PARAMETER TEMPLATE )))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
####################################################################
# Add custom parameters as initial starting point for CTRL node.

# Add folder used to collect all newly create parameters
folder = hou.FolderParmTemplate("folder", "Folder Name")
# Define folder type; default is Tabs. Set to Simple
folder.setFolderType(hou.folderType.Simple)

# Add parameter types, defined by parameter name, label, and number of components.
# Add float parameter
folder.addParmTemplate(hou.FloatParmTemplate("parm1", "Parameter 1 Name", 1))
# Add vector2 parameter
folder.addParmTemplate(hou.FloatParmTemplate("parm2", "Parameter 2 Name", 2))
# Add vector3 parameter
folder.addParmTemplate(hou.FloatParmTemplate("parm3", "Parameter 3 Name", 3))
# Add integer parameter
folder.addParmTemplate(hou.IntParmTemplate("parm4", "Parameter 4 Name", 1))

# Add parameters to node
# Define parameter group used to collect folder/s
group = curNode.parmTemplateGroup()
# Add folder to group and group to node
group.append(folder)
curNode.setParmTemplateGroup(group)
# -----------------------------------------------------------
# PARAMETER TEMPLATE )))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
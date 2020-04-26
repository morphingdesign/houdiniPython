# Script for use to generate a Control Panel node by using the
# Null node as a basis, but with additional variations to streamline
# creation process of a control panel for parameters.

####################################################################

# Imports vital Houdini library
import objecttoolutils

####################################################################

# Generates node (can be copied from existing tools to save time)
kwargs['bbox'] = hou.BoundingBox(-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)
objecttoolutils.genericTool(kwargs, 'null')

# This returns the currently selected node
curNode = kwargs['pane'].currentNode()

# Ask user for name for the CTRL node's suffix
# Since name is a tuple, we need the 2nd value, hence the [1]
name = hou.ui.readInput("Type node name", title="Ctrl Node Name")[1]
name = "CTRL_" + name.upper()

# Replaces blank spaces in the input name with an underscore
# Without this, the null node fails
name = name.replace(" ", "_")

# Assign name variable to the node
curNode.setName(name)

# Sets node's color to blue
curNode.setColor(hou.Color(0.094, 0.369, 0.69))

# Sets the node shape to be a circle
curNode.setUserData('nodeshape', 'circle')

####################################################################
# Add custom parameters

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
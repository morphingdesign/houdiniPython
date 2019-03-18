# Displays the string message when tool is activated
#hou.ui.displayMessage("Display Message")

# Imports vital Houdini library
import objecttoolutils

# Generates node (can be copied from existing tools to save time)
kwargs['bbox'] = hou.BoundingBox(-0.5, -0.5, -0.5, 0.5, 0.5, 0.5)
objecttoolutils.genericTool(kwargs, 'null')

# This returns the currently selected node
curNode = kwargs['pane'].currentNode()

# Ask user for name for the OUT node
# Since name is a tuple, we need the 2nd value, hence the [1]
name = hou.ui.readInput("Type node name", title="Out Node Name")[1]
name = name.upper()

# Replaces blank spaces in the input name with an underscore
# Without this, the null node fails
name = name.replace(" ", "_")

# Assigns the name variable to the null node being created
curNode.setName(name)

# Sets the color for the null node being created
curNode.setColor(hou.Color(1.0, 0.0, 0.0))

# Sets the blue flag on the null node being created
curNode.setDisplayFlag(True)
curNode.setRenderFlag(True)

# Prints null node name to the python shell
#print name
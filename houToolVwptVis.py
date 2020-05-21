# Script for use to quickly visualize attributes in Scene view
# Request user input via dialog boxes and display defined visualizer
# Scene View

####################################################################

# Imports Houdini tool library
import toolutils

# Access current viewport via SceneViewer class
geoView = toolutils.SceneViewer().curViewport()

# UI
# Get text input from user of geo attribute to visualize
# Returns tuple of int and text entered by user
# Assign var to value 1 in tuple to get text, user's chosen attribute
attrToVis = hou.ui.readInput("Visualize Attribute")[1]

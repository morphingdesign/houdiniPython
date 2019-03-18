import soptoolutils

# Store nodes that are selected
selNodes = hou.selectedNodes()

# Creates the merge node
mrg = soptoolutils.genericTool(kwargs, 'merge')

# Use a for loop and store each node in an iterable format using enumerate
for x, node in enumerate(selNodes):
    # Test the printing of selected nodes
    # node.name()
    # print node.name()

    # Attached a wire from each selected node to the new merge node
    # stored in the mrg variable
    mrg.setNextInput(node)

# Sets the display and render flags for merge
mrg.setDisplayFlag(True)
mrg.setRenderFlag(True)
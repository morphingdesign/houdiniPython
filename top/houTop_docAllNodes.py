# -----------------------------------------------------------
# houTop_docAllNodes.py
# v.1.0
# Updated: 20211112
# ----------------------------------------------------------

"""
Python Processor
Initialize work items for top stream by collecting and documenting
all nodes in project file for organizational log. The intent is
to pass this a CSV Output TOP for documenting node hierarchy in
project file.
"""

# -----------------------------------------------------------
# HOUDINI REFERENCE DOC ))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# Called when this node should generate new work items from upstream items.
#
# self             -   A reference to the current pdg.Node instance
# item_holder      -   A pdg.WorkItemHolder for constructing and adding work items
# upstream_items   -   The list of work items in the node above, or empty list if there are no inputs
# generation_type  -   The type of generation, e.g. pdg.generationType.Static, Dynamic, or Regenerate

# -----------------------------------------------------------
# HOUDINI REFERENCE DOC ))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

import hou

# Modify creator metadata for selected nodes in this project file.
# Attribute the hipname.

# -----------------------------------------------------------
# LOCAL VARIABLES ))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

obj = hou.node("/obj")
all = hou.node("/")
# allSubChildren() is top-down logging of nodes and recursive.
# Other options include allNodes(), but doesn't return tuple.
allnodes = all.allSubChildren()

# -----------------------------------------------------------
# LOCAL VARIABLES ))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# GENERATE WORK ITEMS ))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

for k, node in enumerate(allnodes):
    # Generate work item. Note ref above that item_holder is
    # recognized by PDG.
    new_item = item_holder.addWorkItem(index = k)
    # Add string attributes for each node/work item.
    new_item.setStringAttrib("name", node.name())
    new_item.setStringAttrib("path", node.path())

# -----------------------------------------------------------
# GENERATE WORK ITEMS ))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
# -----------------------------------------------------------
# houTop_logAttr.py
# v.1.0
# Updated: 20211114
# ----------------------------------------------------------

"""
Python Script
This TOP runs over each work_item; basically acting like a loop
iterating through each work_item.
"""

# -----------------------------------------------------------
# HOUDINI REFERENCE DOC ))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# Executes a Python script, either in process or as a job
#
# The following variables and functions are available in both case:
# work_item
# intData, floatData, strData,
# intDataArray, floatDataArray, strDataArray
#
# In addition to the above, in-process scripts can also access:
# self         - the current PDG node
# parent_item  - the parent work item, if it exists

# Ref: https://www.sidefx.com/docs/houdini/tops/pdg/index.html

# -----------------------------------------------------------
# HOUDINI REFERENCE DOC ))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

import hou

# Modify creator metadata for selected nodes in this project file.
# Attribute the hipname.

# -----------------------------------------------------------
# LOCAL VARIABLES ))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# Get values for each work_item's attributes. In this case, the
# attributes for each work_item had been previously setup in a
# Python Processor storing the info for each node in project file.
data_name = (strData(work_item, "name"))
data_net = (strData(work_item, "network"))
data_type = (strData(work_item, "type"))
data_path = (strData(work_item, "path"))
data_index = (intData(work_item, "index"))
data_note = (strData(work_item, "note"))
if data_note == "":
    data_note = "N/A"
else:
    data_note = data_note

# -----------------------------------------------------------
# LOCAL VARIABLES ))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# LOG ATTRIBUTE VALUES )))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# Output work_item values to log.
print("****************************")
print("%d: %s" % (data_index, data_name))
print("Network: %s" % data_net)
print("Type: %s" % data_type)
print("Notes: %s" % data_note)
print("Path: %s" % data_path)

# Split data path into levels for hierarchy organization.
data_path = (strDataArray(work_item, "split"))
data_path.remove("")
print(data_path)

for k, elem in enumerate(data_path):
    work_item.setStringAttrib("p%d" % k, elem)
    path_attr = (strData(work_item, "p%d" % k))
    print("Level %d: %s" % (k, path_attr))

# -----------------------------------------------------------
# LOG ATTRIBUTE VALUES )))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------



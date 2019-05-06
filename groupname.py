# groupname.py
# Input code for group node in Houdini to auto name group
# based on node name

#########################################################
# Import relevant libs

import toolutils
import soptoolutils

# Set var to identify group node creation
grp = soptoolutils.genericTool(kwargs, 'groupcreate')

# Set parm to auto name the group based on the node name
grp.parm("groupname").set("`opname('.')`")
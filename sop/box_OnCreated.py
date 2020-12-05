#########################################################
"""Custom script to setup typical box startup parameters."""

import sys

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# IMPORTANT: Reset path to user-defined path with 'username'
library_path = r'C:\Users\username\Documents\houdini18.0\scripts'
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

sys.path.append(library_path)
from common_py_lib import utils

# Access this node via variable
node = kwargs['node']

# Set Parameters

# Set primitive type to polygon mesh.
node.parm("type").set("polymesh")

node.parmTuple('size').set([0.5,0.5,0.5])
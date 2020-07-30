#########################################################
"""Custom script to setup typical group expression operator name."""

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

# Access function from utils lib
utils.lib_set_opname(node, "groupname1")
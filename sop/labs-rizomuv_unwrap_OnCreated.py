#########################################################
"""Custom script to define Rizom.exe path on disk."""

# Source: https://www.sidefx.com/docs/houdini/hom/locations.html

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
# Set path to Rizom.exe on disk
utils.lib_set_rizomExe(node)
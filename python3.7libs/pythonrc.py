# -----------------------------------------------------------
# pythonrc.py
# v.1.0
# Updated: 20211117
# Houdini version: 18.5.563, Python 3
# File located inside Python3.7libs directory. Sim to previous
#   version which would have been Python2.7libs directory.
# -----------------------------------------------------------

"""
Houdini startup scripts for personal/studio-wide operations.
Ref: https://www.sidefx.com/docs/houdini/hom/locations.html#startup
"""

# -----------------------------------------------------------
# GLOBAL VARIABLES )))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# IMPORTANT: Reset 'USERNAME' and 'VERSION' with path to user-
# defined path of scripts location.
library_path = r'C:\Users\USERNAME\Documents\houdiniVERSION\scripts'

# -----------------------------------------------------------
# GLOBAL VARIABLES )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# IMPORT LIBRARIES )))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

import sys
sys.path.append(library_path)
import hou
from common_py_lib import utils, uiUtils

# -----------------------------------------------------------
# IMPORT LIBRARIES )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------


# -----------------------------------------------------------
# REGISTER CALLBACK ))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

hou.hipFile.addEventCallback(utils.scene_was_saved)

# User notification that this script file was enabled and processed.
print("Python RC enabled.")

# -----------------------------------------------------------
# REGISTER CALLBACK ))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
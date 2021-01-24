# -----------------------------------------------------------
# delete_OnCreated.py
# v.1.0
# Updated: 20210124
# ----------------------------------------------------------

"""
Custom script to format delete content node.
"""
from common_py_lib import utils

# -----------------------------------------------------------
# GLOBAL VARIABLES )))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
node = kwargs['node']
# -----------------------------------------------------------
# GLOBAL VARIABLES )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# CUSTOMIZATIONS )))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
# Set node to delete content default color and shape
utils.lib_set_deleteNodeDefaults(node)
# -----------------------------------------------------------
# CUSTOMIZATIONS )))))))))))))))))))))))))))))))))}}))))) END
# -----------------------------------------------------------
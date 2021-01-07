# -----------------------------------------------------------
# sphere_OnCreated.py
# v.1.1
# Updated: 20201207
# ----------------------------------------------------------

"""
Custom script to setup typical sphere startup parameters
"""

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
# Set Parameters
node.parm("type").set("polymesh")
node.parmTuple('rad').set([0.5,0.5,0.5])
# -----------------------------------------------------------
# CUSTOMIZATIONS )))))))))))))))))))))))))))))))))}}))))) END
# -----------------------------------------------------------
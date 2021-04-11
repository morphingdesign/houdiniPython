# -----------------------------------------------------------
# houToolRSMatNode.py
# v.1.0
# Updated: 20210410
# ----------------------------------------------------------

"""
Custom shelf tool to generate a Redshift Material Builder node
with configuration to accept Substance material output from
Substance Painter. Includes texture inputs for Base Color,
Metallic, Roughness, Normal, Height, and Emission.
"""

# Libs used for testing
#import soptoolutils
#import stateutils
from common_py_lib import utils

# -----------------------------------------------------------
# ACCESS NETWORK )))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
# The intent is to access the intended Material Network.
# Ultimately, the strategy taken is to access the network
# via the mouse cursor position in the network editor.

#########################################
# Testing for identifying current network.
#pane = stateutils.activePane(kwargs)
#print(pane)
#curNet = pane.pwd()
#print(pane.cd())
#########################################

# Collect network editor view currently under mouse cursor.
curPane = hou.ui.paneTabUnderCursor()
# -----------------------------------------------------------
# ACCESS NETWORK )))}}))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# MATERIAL CREATION ))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
# Check if current pane is a network editor view
if isinstance(curPane, hou.NetworkEditor):
    #print('success')   # DEBUGGING
    # Use path to current network editor and store as current
    # node for creating the new Redshift material.
    curNet = curPane.pwd()
    curNet = kwargs['pane'].currentNode()
    utils.lib_create_RSMatForSubP(curNet)
else:
    # Notify user that the current pane is not a network
    # editor view. Since the 'paneTabUnderCursor()` requires
    # the mouse cursor to be accessed from within the bounds
    # of the network editor, this shelf tool must be accessed
    # from within these bounds and not solely through the
    # shelf toolbar icon.
    #print('failure')   # DEBUGGING
    hou.ui.setStatusMessage('Access this tool from within a Material Network.', severity=hou.severityType.Message)
    #pass
# -----------------------------------------------------------
# MATERIAL CREATION ))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------













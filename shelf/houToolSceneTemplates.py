# -----------------------------------------------------------
# houToolSceneTemplate.py
# v.1.0
# Updated: 20211127
# Houdini version: 18.5.563, Python 3
# ----------------------------------------------------------

"""
Custom shelf tool using a Qt dialog to display options for
startup template files.
"""

# -----------------------------------------------------------
# IMPORT LIBRARIES )))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

from PySide2 import QtGui, QtUiTools, QtWidgets, QtCore
from common_py_lib import qtUtils

# -----------------------------------------------------------
# IMPORT LIBRARIES )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

# -----------------------------------------------------------
# DIALOG )))))))))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
# Generate Null node
# Instantiate template window UI
dialog = qtUtils.TemplateWindow()
# Parent dialog to the main hou window to preserve dialog
dialog.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
dialog.show()
# -----------------------------------------------------------
# DIALOG ))))))))))))))))))))))))))))))))))))))}})))))))) END
# -----------------------------------------------------------
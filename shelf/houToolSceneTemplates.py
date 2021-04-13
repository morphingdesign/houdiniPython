# -----------------------------------------------------------
# houToolSceneTemplate.py
# v.1.0
# Updated: 20210413
# ----------------------------------------------------------

"""
Custom shelf tool using a Qt dialog to display options for
startup template files.
"""

from PySide2 import QtGui, QtUiTools, QtWidgets, QtCore
from common_py_lib import qtUtils

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
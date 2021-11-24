# -----------------------------------------------------------
# houQtUiTool_001.py
# v.1.0
# Updated: 20211124
# ----------------------------------------------------------

"""
Custom shelf tool using a Qt dialog to evaluate combo box options.
"""

from PySide2 import QtGui, QtUiTools, QtWidgets, QtCore
from common_py_lib import qtUtils

# -----------------------------------------------------------
# DIALOG )))))))))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------
# Instantiate window UI
dialog = qtUtils.NewColorNode()
# Parent dialog to the main hou window to preserve dialog
# Source: https://www.sidefx.com/docs/houdini/hom/hou/qt/mainWindow.html
dialog.setParent(hou.qt.mainWindow(), QtCore.Qt.Window)
dialog.show()
# -----------------------------------------------------------
# DIALOG ))))))))))))))))))))))))))))))))))))))}})))))))) END
# -----------------------------------------------------------
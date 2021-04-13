# -----------------------------------------------------------
# qtUtils.py
# v.1.0
# Updated: 20210413
# -----------------------------------------------------------

"""
Custom Houdini UI utilities for use with startup and quick node
creation specifically designed around Qt.
"""

from PySide2 import QtGui, QtUiTools, QtWidgets, QtCore

# -----------------------------------------------------------
# TEMPLATES ))))))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

class TemplateWindow(QtWidgets.QWidget):
    # Init function
    def __init__(self):
        super(TemplateWindow, self).__init__()

        # Load UI file.
        ui_file = 'D:/DataSync/04_Research/RnD_Python/03_script/z_other/QtDesigner/initHouUI.ui'
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget = self)

        # Set dialog title.
        self.setWindowTitle("Houdini Templates")
        # Enact button and process method.
        self.ui.startBtn.clicked.connect(self.setText)

    # Method to change text label.
    def setText(self):
        self.ui.textLabel.setText('user feedback')

    # Unparent from main window to destroy dialog.
    def closeEvent(self, event):
        self.setParent(None)

# -----------------------------------------------------------
# TEMPLATES ))))))))))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
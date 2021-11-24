# -----------------------------------------------------------
# qtUtils.py
# v.1.0
# Updated: 20211124
# -----------------------------------------------------------

"""
Custom Houdini UI utilities for use with startup and quick node
creation specifically designed around Qt.
"""

import hou
from PySide2 import QtGui, QtUiTools, QtWidgets, QtCore
from common_py_lib import hpUtils

# Specify local path for Qt .ui file.
localDir = hpUtils.AssetDir()
qtDirPath = localDir.getQtDir()

# -----------------------------------------------------------
# GLOBAL VARIABLES )))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# List of colors formatted for Houdini content.
red_color = hou.Color(1.0, 0.0, 0.0)
green_color = hou.Color(0.0, 1.0, 0.0)
blue_color = hou.Color(0.0, 0.0, 1.0)
colors = [red_color, green_color, blue_color]

# -----------------------------------------------------------
# GLOBAL VARIABLES )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------


# -----------------------------------------------------------
# TEMPLATES ))))))))))))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

class TemplateWindow(QtWidgets.QWidget):
    # Init function
    def __init__(self):
        super(TemplateWindow, self).__init__()

        # Load UI file.
        ui_file = qtDirPath + "initHouUI.ui"
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

# -----------------------------------------------------------
# COMBO BOX & BUTTON )))))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

class NewColorNode(QtWidgets.QWidget):
    def __init__(self):
        super(NewColorNode, self).__init__()

        # Load UI file.
        ui_file = qtDirPath + "ui_tool_01.ui"

        # Initialize and load Qt window.
        self.ui = QtUiTools.QUiLoader().load(ui_file, parentWidget=self)
        self.setParent(hou.ui.mainQtWindow(), QtCore.Qt.Window)
        self.setWindowTitle('UI Tool 01')

        # Combo box with options.
        cb = self.ui.btn_comboBox
        cb.addItems(["Red", "Green", "Blue"])

        # Button to enact action. Pass in current index from combo box
        # into create_node function.
        self.ui.btn_createNode.clicked.connect(lambda: self.create_node(cb.currentIndex()))

    # Create new node of specified color.
    def create_node(self, index):
        newNode = hou.node('/obj').createNode('null', "Node")
        specColor = colors[index]
        newNode.setColor(specColor)
        print(specColor)

        # Debug log combo box options.

    def selectionChange(self, i):
        print("Items in the list are:")
        for count in range(self.ui.btn_comboBox.count()):
            print(self.ui.btn_comboBox.itemText(count))
        print("Current index %d selection changed %s." % (i, self.ui.btn_comboBox.currentText()))
        return i

# -----------------------------------------------------------
# COMBO BOX & BUTTON )))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
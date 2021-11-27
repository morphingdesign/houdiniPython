# -----------------------------------------------------------
# qtUtils.py
# v.1.0
# Updated: 20211124
# -----------------------------------------------------------

"""
Custom Houdini UI utilities for use with startup and quick node
creation specifically designed around Qt.
"""

# -----------------------------------------------------------
# HOT RELOADING IN HOU )))))))))))))))))))))))))))))))) START
# -----------------------------------------------------------

# Include the following to allow for hot reload in Houdini Python console.
# In console simply type the following to load the module:
#       Syntax                  Example
#       import <module>         from common_py_lib import qtUtils
# Then to reload any edits made to the module:
#       Syntax                  Example
#       reload(<module>)        reload(qtUtils)

import importlib

__builtins__['reload'] = importlib.reload

# -----------------------------------------------------------
# HOT RELOADING IN HOU )))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------

import hou
import toolutils
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
# NODE CREATION UI )))))))))))))))))))))))))))))))))))) START
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

        # Line edit user-entered text.
        self.le = self.ui.text_nodeName
        self.le.editingFinished.connect(self.setName)

        # Combo box with options.
        self.cb = self.ui.btn_comboBox
        self.cb.addItems(["Red", "Green", "Blue"])

        # Button to enact action. Pass in current index from combo box
        # into create_node function.
        self.ui.btn_createNode.clicked.connect(lambda: self.create_node(self.cb.currentIndex()))

    # Create new node of specified color.
    def create_node(self, index):
        newNode = hou.node('/obj').createNode('null', "Node")
        specColor = colors[index]
        newNode.setColor(specColor)
        # Unique name arg enabled to prevent same name errors.
        newNode.setName(self.le.text(), unique_name=True)
        # Verify node is placed in new position each time to prevent overlaps.
        toolutils.moveNodesToGoodPosition([newNode])
        #print(specColor)

    # Debug log combo box options.
    def selectionChange(self, i):
        print("Items in the list are:")
        for count in range(self.ui.btn_comboBox.count()):
            print(self.ui.btn_comboBox.itemText(count))
        print("Current index %d selection changed %s." % (i, self.ui.btn_comboBox.currentText()))
        return i

    # Method to eval user-entered text field.
    def setName(self):
        print(self.le.text())

# -----------------------------------------------------------
# NODE CREATION UI )))))))))))))))))))))))))))))))))))))) END
# -----------------------------------------------------------
# -----------------------------------------------------------
# node_log.py
# v.1.0
# Updated: 20220807
# -----------------------------------------------------------

"""
Qt Table UI for visualizing node utilization log.
"""

import sys
from PyQt5 import QtCore, QtWidgets
import json


def main():

    json_path = 'C:/temp/hou_log/hou_node_usage_log.json'

    app = QtWidgets.QApplication(sys.argv)

    with open(json_path) as f:
        d = json.load(f)
    keys = ["name", "type", "category", "current", "path", "date", "time"]
    labels = keys

    w = QtWidgets.QTableWidget(0, len(labels))
    w.setHorizontalHeaderLabels(labels)

    for i, entry in enumerate(d["node_details"]):
        w.insertRow(w.rowCount())
        for j, (k, v) in enumerate(entry.items()):
            it = QtWidgets.QTableWidgetItem()
            it.setData(QtCore.Qt.DisplayRole, v)
            w.setItem(i, j, it)
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

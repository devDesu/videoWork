# -*-coding: utf-8 -*-

import sys
from test import Ui_MainWindow
from PyQt4 import QtGui
import time
from PyQt4.QtCore import pyqtSlot


class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clk)

    @pyqtSlot()
    def clk(self):
        print time.time()

app = QtGui.QApplication(sys.argv)
f = MainWindow(None)
f.show()
app.exec_()
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created: Wed Jun 03 12:52:21 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(522, 275)
        MainWindow.setTabShape(QtGui.QTabWidget.Rounded)
        MainWindow.setDockNestingEnabled(False)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 521, 261))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.selectFolder = QtGui.QPushButton(self.tab)
        self.selectFolder.setGeometry(QtCore.QRect(10, 170, 101, 23))
        self.selectFolder.setObjectName(_fromUtf8("selectFolder"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(10, 145, 491, 21))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.check = QtGui.QPushButton(self.tab)
        self.check.setEnabled(False)
        self.check.setGeometry(QtCore.QRect(120, 170, 75, 23))
        self.check.setObjectName(_fromUtf8("check"))
        self.preview = QtGui.QCheckBox(self.tab)
        self.preview.setEnabled(True)
        self.preview.setGeometry(QtCore.QRect(400, 173, 101, 17))
        self.preview.setObjectName(_fromUtf8("preview"))
        self.run = QtGui.QPushButton(self.tab)
        self.run.setEnabled(False)
        self.run.setGeometry(QtCore.QRect(310, 170, 75, 23))
        self.run.setObjectName(_fromUtf8("run"))
        self.fps = QtGui.QDoubleSpinBox(self.tab)
        self.fps.setEnabled(True)
        self.fps.setGeometry(QtCore.QRect(240, 170, 62, 22))
        self.fps.setDecimals(0)
        self.fps.setMinimum(1.0)
        self.fps.setMaximum(48.0)
        self.fps.setProperty("value", 24.0)
        self.fps.setObjectName(_fromUtf8("fps"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(210, 173, 21, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(10, 200, 501, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.errorEdit = QtGui.QTextEdit(self.tab)
        self.errorEdit.setGeometry(QtCore.QRect(20, 20, 481, 121))
        self.errorEdit.setReadOnly(True)
        self.errorEdit.setObjectName(_fromUtf8("errorEdit"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.selectFolder.setText(_translate("MainWindow", "Выберите папку", None))
        self.check.setText(_translate("MainWindow", "Проверить", None))
        self.preview.setText(_translate("MainWindow", "Предпросмотр", None))
        self.run.setText(_translate("MainWindow", "Запуск", None))
        self.label_2.setText(_translate("MainWindow", "fps", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Склейка", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Нормализация", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'email_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        self.MainWindow.setObjectName("MainWindow")
        self.MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.email_content = QtWidgets.QTextEdit(self.centralwidget)
        self.email_content.setObjectName("email_content")
        self.gridLayout.addWidget(self.email_content, 2, 0, 1, 1)
        self.label_from = QtWidgets.QLabel(self.centralwidget)
        self.label_from.setObjectName("label_from")
        self.gridLayout.addWidget(self.label_from, 0, 0, 1, 1)
        self.label_other = QtWidgets.QLabel(self.centralwidget)
        self.label_other.setObjectName("label_other")
        self.gridLayout.addWidget(self.label_other, 1, 0, 1, 1)
        self.MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(self.MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.action_folder = QtWidgets.QAction(self.MainWindow)
        self.action_folder.setObjectName("action_folder")
        self.action_browser = QtWidgets.QAction(self.MainWindow)
        self.action_browser.setObjectName("action_browser")
        self.menuFile.addAction(self.actionQuit)
        self.menuFile.addAction(self.action_folder)
        self.menuFile.addAction(self.action_browser)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(self.MainWindow)
        QtCore.QMetaObject.connectSlotsByName(self.MainWindow)

    def _show(self):
        self.MainWindow.show()

    def _quit(self):
        # QtCore.QCoreApplication.instance().quit()
        self.MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Email"))
        self.label_from.setText(_translate("MainWindow", "From : "))
        self.label_other.setText(_translate("MainWindow", "To : "))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.action_folder.setText(_translate("MainWindow", "Go to Folder"))
        self.action_browser.setText(_translate("MainWindow", "Open in Browser"))
        self.actionQuit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.action_browser.setShortcut(_translate("MainWindow", "Ctrl+B"))
        self.action_folder.setShortcut(_translate("MainWindow", "Ctrl+F"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'options.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1319, 948)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.folder_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.folder_label.setFont(font)
        self.folder_label.setAlignment(QtCore.Qt.AlignCenter)
        self.folder_label.setObjectName("folder_label")
        self.gridLayout.addWidget(self.folder_label, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.search_label.setFont(font)
        self.search_label.setObjectName("search_label")
        self.horizontalLayout.addWidget(self.search_label)
        self.search_input = QtWidgets.QLineEdit(self.frame_2)
        self.search_input.setMinimumSize(QtCore.QSize(500, 0))
        self.search_input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.search_input.setObjectName("search_input")
        self.horizontalLayout.addWidget(self.search_input)
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.setItemText(0, "")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.gobtn = QtWidgets.QCommandLinkButton(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gobtn.sizePolicy().hasHeightForWidth())
        self.gobtn.setSizePolicy(sizePolicy)
        self.gobtn.setMinimumSize(QtCore.QSize(5, 0))
        self.gobtn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.gobtn.setObjectName("gobtn")
        self.horizontalLayout.addWidget(self.gobtn)
        self.gridLayout_4.addLayout(self.horizontalLayout, 0, 1, 1, 2)
        self.widget = QtWidgets.QWidget(self.frame_2)
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.folder_listview = QtWidgets.QListWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.folder_listview.sizePolicy().hasHeightForWidth())
        self.folder_listview.setSizePolicy(sizePolicy)
        self.folder_listview.setMinimumSize(QtCore.QSize(50, 0))
        self.folder_listview.setObjectName("folder_listview")
        self.gridLayout_3.addWidget(self.folder_listview, 0, 0, 1, 2)
        self.add_folder_edit = QtWidgets.QLineEdit(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_folder_edit.sizePolicy().hasHeightForWidth())
        self.add_folder_edit.setSizePolicy(sizePolicy)
        self.add_folder_edit.setMinimumSize(QtCore.QSize(132, 0))
        self.add_folder_edit.setObjectName("add_folder_edit")
        self.gridLayout_3.addWidget(self.add_folder_edit, 1, 0, 1, 1)
        self.addbtn = QtWidgets.QPushButton(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addbtn.sizePolicy().hasHeightForWidth())
        self.addbtn.setSizePolicy(sizePolicy)
        self.addbtn.setMinimumSize(QtCore.QSize(10, 0))
        self.addbtn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.addbtn.setObjectName("addbtn")
        self.gridLayout_3.addWidget(self.addbtn, 1, 1, 1, 1)
        self.gridLayout_4.addWidget(self.widget, 1, 0, 2, 2)
        self.emails_listview = QtWidgets.QListWidget(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("URW Bookman L")
        font.setPointSize(13)
        self.emails_listview.setFont(font)
        self.emails_listview.setObjectName("emails_listview")
        self.gridLayout_4.addWidget(self.emails_listview, 2, 2, 1, 1)
        self.emails_listview.raise_()
        self.frame.raise_()
        self.widget.raise_()
        self.gridLayout_2.addWidget(self.frame_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1319, 25))
        self.menubar.setObjectName("menubar")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuView = QtWidgets.QMenu(self.menubar)
        self.menuView.setObjectName("menuView")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.another_account = QtWidgets.QAction(MainWindow)
        self.another_account.setObjectName("another_account")
        self.logout = QtWidgets.QAction(MainWindow)
        self.logout.setObjectName("logout")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionDelete = QtWidgets.QAction(MainWindow)
        self.actionDelete.setObjectName("actionDelete")
        self.actionMotif = QtWidgets.QAction(MainWindow)
        self.actionMotif.setObjectName("actionMotif")
        self.actionWindows = QtWidgets.QAction(MainWindow)
        self.actionWindows.setObjectName("actionWindows")
        self.actionCde = QtWidgets.QAction(MainWindow)
        self.actionCde.setObjectName("actionCde")
        self.actionPlastique = QtWidgets.QAction(MainWindow)
        self.actionPlastique.setObjectName("actionPlastique")
        self.actionCleanlooks = QtWidgets.QAction(MainWindow)
        self.actionCleanlooks.setObjectName("actionCleanlooks")
        self.actionWindowsvista = QtWidgets.QAction(MainWindow)
        self.actionWindowsvista.setObjectName("actionWindowsvista")
        self.actionDelete_Mail = QtWidgets.QAction(MainWindow)
        self.actionDelete_Mail.setObjectName("actionDelete_Mail")
        self.menuOptions.addAction(self.logout)
        self.menuOptions.addAction(self.another_account)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.actionExit)
        self.menuEdit.addAction(self.actionDelete)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionDelete_Mail)
        self.menuView.addAction(self.actionMotif)
        self.menuView.addAction(self.actionWindows)
        self.menuView.addAction(self.actionCde)
        self.menuView.addAction(self.actionPlastique)
        self.menuView.addAction(self.actionCleanlooks)
        self.menuView.addAction(self.actionWindowsvista)
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # custom
    def change_window_name(self, name):
        _translate = QtCore.QCoreApplication.translate
        self.MainWindow.setWindowTitle(_translate("MainWindow", name))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Email Client"))
        self.folder_label.setText(_translate("MainWindow", "Folders "))
        self.search_label.setText(_translate("MainWindow", "Search  :"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Seen"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Unseen"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Mail From"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Deleted"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Since"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Text"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Subject"))
        self.gobtn.setText(_translate("MainWindow", "Go"))
        self.addbtn.setText(_translate("MainWindow", "+"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuView.setTitle(_translate("MainWindow", "View"))
        self.another_account.setText(_translate("MainWindow", "Sign in with different acount"))
        self.another_account.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.logout.setText(_translate("MainWindow", "Logout"))
        self.logout.setShortcut(_translate("MainWindow", "Ctrl+Shift+L"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+W"))
        self.actionDelete.setText(_translate("MainWindow", "Delete selected"))
        self.actionDelete.setShortcut(_translate("MainWindow", "Del"))
        self.actionMotif.setText(_translate("MainWindow", "motif"))
        self.actionWindows.setText(_translate("MainWindow", "Windows"))
        self.actionCde.setText(_translate("MainWindow", "Cde"))
        self.actionPlastique.setText(_translate("MainWindow", "Plastique"))
        self.actionCleanlooks.setText(_translate("MainWindow", "Cleanlooks"))
        self.actionWindowsvista.setText(_translate("MainWindow", "windowsvista"))
        self.actionDelete_Mail.setText(_translate("MainWindow", "Delete Mail"))
        self.actionDelete_Mail.setShortcut(_translate("MainWindow", "Shift+Del"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

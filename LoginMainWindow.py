# Form implementation generated from reading ui file 'C:\Users\Laptop Huynh Gia\PycharmProjects\LearnFunction\K24406H\DoAn\ui\LoginMainWindow.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(437, 291)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 401, 51))
        self.label.setStyleSheet("background-color: rgb(199, 214, 160);\n"
"font: 75 18pt \"MS Shell Dlg 2\";\n"
"color: rgb(140, 94, 86);")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 121, 31))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEditUserName = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditUserName.setGeometry(QtCore.QRect(150, 79, 231, 31))
        self.lineEditUserName.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(247, 255, 229);")
        self.lineEditUserName.setText("")
        self.lineEditUserName.setObjectName("lineEditUserName")
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(150, 130, 231, 31))
        self.lineEditPassword.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(246, 254, 228);")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 131, 121, 31))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.checkBoxSaveInformation = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBoxSaveInformation.setGeometry(QtCore.QRect(150, 170, 241, 21))
        self.checkBoxSaveInformation.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.checkBoxSaveInformation.setObjectName("checkBoxSaveInformation")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogin.setGeometry(QtCore.QRect(150, 200, 111, 31))
        self.pushButtonLogin.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(253, 228, 223);")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(280, 200, 111, 31))
        self.pushButtonExit.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 230, 225);")
        self.pushButtonExit.setObjectName("pushButtonExit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 437, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600; color:#62413c;\">Login Screen</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "User name:"))
        self.label_3.setText(_translate("MainWindow", "Password:"))
        self.checkBoxSaveInformation.setText(_translate("MainWindow", "Save login information"))
        self.pushButtonLogin.setText(_translate("MainWindow", "Login"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))

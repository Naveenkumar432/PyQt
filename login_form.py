# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login_Form(object):
    def setupUi(self, Login_Form):
        Login_Form.setObjectName("Login_Form")
        Login_Form.resize(361, 184)
        self.widget = QtWidgets.QWidget(Login_Form)
        self.widget.setGeometry(QtCore.QRect(60, 30, 271, 131))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.ok_button = QtWidgets.QPushButton(self.widget)
        self.ok_button.setObjectName("ok_button")
        self.gridLayout.addWidget(self.ok_button, 4, 2, 1, 1)
        self.user_name = QtWidgets.QLabel(self.widget)
        self.user_name.setObjectName("user_name")
        self.gridLayout.addWidget(self.user_name, 0, 0, 1, 1)
        self.password_input = QtWidgets.QLineEdit(self.widget)
        self.password_input.setEnabled(True)
        self.password_input.setAutoFillBackground(False)
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setObjectName("password_input")
        self.gridLayout.addWidget(self.password_input, 1, 1, 1, 2)
        self.password = QtWidgets.QLabel(self.widget)
        self.password.setObjectName("password")
        self.gridLayout.addWidget(self.password, 1, 0, 1, 1)
        self.cancel_button = QtWidgets.QPushButton(self.widget)
        self.cancel_button.setObjectName("cancel_button")
        self.gridLayout.addWidget(self.cancel_button, 4, 0, 1, 2)
        self.user_input = QtWidgets.QLineEdit(self.widget)
        self.user_input.setObjectName("user_input")
        self.gridLayout.addWidget(self.user_input, 0, 1, 1, 2)
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 1)

        self.retranslateUi(Login_Form)
        QtCore.QMetaObject.connectSlotsByName(Login_Form)

    def retranslateUi(self, Login_Form):
        _translate = QtCore.QCoreApplication.translate
        Login_Form.setWindowTitle(_translate("Login_Form", "Form"))
        self.ok_button.setText(_translate("Login_Form", "OK"))
        self.user_name.setText(_translate("Login_Form", "User Name"))
        self.password.setText(_translate("Login_Form", "Password"))
        self.cancel_button.setText(_translate("Login_Form", "Cancel"))
        self.checkBox.setText(_translate("Login_Form", "CheckBox"))


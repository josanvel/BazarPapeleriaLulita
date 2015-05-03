# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created: Sat Apr 18 03:53:42 2015
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_Login(QtGui.QMainWindow):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(450, 420)
        Login.setMinimumSize(QtCore.QSize(450, 420))
        Login.setMaximumSize(QtCore.QSize(450, 420))
        self.centralwidget = QtGui.QWidget(Login)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.fondoLogin = QtGui.QLabel(self.centralwidget)
        self.fondoLogin.setGeometry(QtCore.QRect(10, 0, 450, 420))
        self.fondoLogin.setText(_fromUtf8(""))
        self.fondoLogin.setPixmap(QtGui.QPixmap(_fromUtf8(":/library.jpg")))
        self.fondoLogin.setObjectName(_fromUtf8("fondoLogin"))
        self.txtUser = QtGui.QLineEdit(self.centralwidget)
        self.txtUser.setGeometry(QtCore.QRect(210, 150, 141, 21))
        self.txtUser.setObjectName(_fromUtf8("txtUser"))
        self.txtPassw = QtGui.QLineEdit(self.centralwidget)
        self.txtPassw.setGeometry(QtCore.QRect(210, 190, 141, 21))
        self.txtPassw.setObjectName(_fromUtf8("txtPassw"))
        self.lblUser = QtGui.QLabel(self.centralwidget)
        self.lblUser.setGeometry(QtCore.QRect(100, 150, 67, 17))
        self.lblUser.setObjectName(_fromUtf8("lblUser"))
        self.lblPassw = QtGui.QLabel(self.centralwidget)
        self.lblPassw.setGeometry(QtCore.QRect(100, 195, 81, 17))
        self.lblPassw.setObjectName(_fromUtf8("lblPassw"))
        self.btnEntrar = QtGui.QPushButton(self.centralwidget)
        self.btnEntrar.setGeometry(QtCore.QRect(150, 240, 161, 21))
        self.btnEntrar.setObjectName(_fromUtf8("btnEntrar"))
        self.lblModificar = QtGui.QLabel(self.centralwidget)
        self.lblModificar.setGeometry(QtCore.QRect(170, 80, 121, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblModificar.setFont(font)
        self.lblModificar.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.lblModificar.setObjectName(_fromUtf8("lblModificar"))
        self.lblBazarPapeleriaLulita = QtGui.QLabel(self.centralwidget)
        self.lblBazarPapeleriaLulita.setGeometry(QtCore.QRect(110, 30, 240, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblBazarPapeleriaLulita.setFont(font)
        self.lblBazarPapeleriaLulita.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblBazarPapeleriaLulita.setObjectName(_fromUtf8("lblBazarPapeleriaLulita"))
        self.lblDireccion = QtGui.QLabel(self.centralwidget)
        self.lblDireccion.setGeometry(QtCore.QRect(80, 50, 311, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblDireccion.setObjectName(_fromUtf8("lblDireccion"))
        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Login", None))
        self.txtPassw.setToolTip(_translate("Login", "Contraseña", None))
        self.lblUser.setText(_translate("Login", "Usuario", None))
        self.lblPassw.setText(_translate("Login", "Contraseña", None))
        self.btnEntrar.setText(_translate("Login", "ENTRAR", None))
        self.lblModificar.setText(_translate("Login", "BIENVENIDO", None))
        self.lblBazarPapeleriaLulita.setText(_translate("Login", "BAZAR Y PAPELERIA LULITA", None))
        self.lblDireccion.setText(_translate("Login", "Km 8 1/2 via Daule - Cdla. \"La Gaviota\" ", None))

import Image_rc

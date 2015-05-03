# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BotonesCuenta.ui'
#
# Created: Sun Mar 15 12:21:57 2015
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

class Ui_BotonesCuenta(object):
    def setupUi(self, BotonesCuenta):
        BotonesCuenta.setObjectName(_fromUtf8("BotonesCuenta"))
        BotonesCuenta.resize(450, 370)
        BotonesCuenta.setMinimumSize(QtCore.QSize(450, 370))
        BotonesCuenta.setMaximumSize(QtCore.QSize(450, 370))
        self.btnCambiarContrasena = QtGui.QPushButton(BotonesCuenta)
        self.btnCambiarContrasena.setGeometry(QtCore.QRect(25, 120, 410, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnCambiarContrasena.setFont(font)
        self.btnCambiarContrasena.setStyleSheet(_fromUtf8("Color:rgb(191, 197, 1);"))
        self.btnCambiarContrasena.setObjectName(_fromUtf8("btnCambiarContrasena"))
        self.btnCrearCuenta = QtGui.QPushButton(BotonesCuenta)
        self.btnCrearCuenta.setGeometry(QtCore.QRect(25, 190, 410, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnCrearCuenta.setFont(font)
        self.btnCrearCuenta.setStyleSheet(_fromUtf8("Color:rgb(191, 197, 1);"))
        self.btnCrearCuenta.setObjectName(_fromUtf8("btnCrearCuenta"))
        self.btnRegresarCuenta = QtGui.QPushButton(BotonesCuenta)
        self.btnRegresarCuenta.setGeometry(QtCore.QRect(230, 280, 200, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegresarCuenta.setFont(font)
        self.btnRegresarCuenta.setStyleSheet(_fromUtf8("color: rgb(51, 102, 255);"))
        self.btnRegresarCuenta.setObjectName(_fromUtf8("btnRegresarCuenta"))
        self.lblCuentas = QtGui.QLabel(BotonesCuenta)
        self.lblCuentas.setGeometry(QtCore.QRect(80, 40, 291, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblCuentas.setFont(font)
        self.lblCuentas.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.lblCuentas.setObjectName(_fromUtf8("lblCuentas"))

        self.retranslateUi(BotonesCuenta)
        QtCore.QMetaObject.connectSlotsByName(BotonesCuenta)

    def retranslateUi(self, BotonesCuenta):
        BotonesCuenta.setWindowTitle(_translate("BotonesCuenta", "Administrar cuentas", None))
        self.btnCambiarContrasena.setToolTip(_translate("BotonesCuenta", "<html><head/><body><p>Cambiar Contraseña</p></body></html>", None))
        self.btnCambiarContrasena.setText(_translate("BotonesCuenta", "CAMBIAR CONTRASEÑA", None))
        self.btnCrearCuenta.setToolTip(_translate("BotonesCuenta", "<html><head/><body><p>Crear Nueva Cuenta</p></body></html>", None))
        self.btnCrearCuenta.setText(_translate("BotonesCuenta", "CREAR NUEVA CUENTA", None))
        self.btnRegresarCuenta.setToolTip(_translate("BotonesCuenta", "<html><head/><body><p><span style=\" color:#ffffff;\">REGRESAR</span></p></body></html>", None))
        self.btnRegresarCuenta.setText(_translate("BotonesCuenta", "REGRESAR", None))
        self.lblCuentas.setText(_translate("BotonesCuenta", "ADMINISTRAR CUENTAS", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cambiarcontrasena.ui'
#
# Created: Mon Apr 20 10:59:13 2015
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

class Ui_cambiarContrasena(QtGui.QMainWindow):
    def setupUi(self, cambiarContrasena):
        cambiarContrasena.setObjectName(_fromUtf8("cambiarContrasena"))
        cambiarContrasena.resize(450, 420)
        cambiarContrasena.setMinimumSize(QtCore.QSize(450, 420))
        cambiarContrasena.setMaximumSize(QtCore.QSize(450, 420))
        font = QtGui.QFont()
        font.setPointSize(11)
        cambiarContrasena.setFont(font)
        self.centralwidget = QtGui.QWidget(cambiarContrasena)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lblCambiarContrasena = QtGui.QLabel(self.centralwidget)
        self.lblCambiarContrasena.setGeometry(QtCore.QRect(110, 80, 221, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblCambiarContrasena.setFont(font)
        self.lblCambiarContrasena.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.lblCambiarContrasena.setObjectName(_fromUtf8("lblCambiarContrasena"))
        self.lblUser = QtGui.QLabel(self.centralwidget)
        self.lblUser.setGeometry(QtCore.QRect(50, 130, 67, 17))
        self.lblUser.setObjectName(_fromUtf8("lblUser"))
        self.lblPasswAntigua = QtGui.QLabel(self.centralwidget)
        self.lblPasswAntigua.setGeometry(QtCore.QRect(50, 180, 141, 17))
        self.lblPasswAntigua.setObjectName(_fromUtf8("lblPasswAntigua"))
        self.txtUser = QtGui.QLineEdit(self.centralwidget)
        self.txtUser.setGeometry(QtCore.QRect(240, 130, 141, 21))
        self.txtUser.setObjectName(_fromUtf8("txtUser"))
        self.txtPassw = QtGui.QLineEdit(self.centralwidget)
        self.txtPassw.setGeometry(QtCore.QRect(240, 180, 141, 21))
        self.txtPassw.setObjectName(_fromUtf8("txtPassw"))
        self.txtPasswNueva = QtGui.QLineEdit(self.centralwidget)
        self.txtPasswNueva.setGeometry(QtCore.QRect(240, 230, 141, 21))
        self.txtPasswNueva.setText(_fromUtf8(""))
        self.txtPasswNueva.setObjectName(_fromUtf8("txtPasswNueva"))
        self.txtPasswVerificar = QtGui.QLineEdit(self.centralwidget)
        self.txtPasswVerificar.setGeometry(QtCore.QRect(240, 280, 141, 21))
        self.txtPasswVerificar.setText(_fromUtf8(""))
        self.txtPasswVerificar.setObjectName(_fromUtf8("txtPasswVerificar"))
        self.lblBazarPapeleriaLulita = QtGui.QLabel(self.centralwidget)
        self.lblBazarPapeleriaLulita.setGeometry(QtCore.QRect(100, 20, 251, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblBazarPapeleriaLulita.setFont(font)
        self.lblBazarPapeleriaLulita.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblBazarPapeleriaLulita.setObjectName(_fromUtf8("lblBazarPapeleriaLulita"))
        self.lblDireccion = QtGui.QLabel(self.centralwidget)
        self.lblDireccion.setGeometry(QtCore.QRect(10, 40, 420, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblDireccion.setObjectName(_fromUtf8("lblDireccion"))
        self.btnRegresar = QtGui.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(50, 350, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegresar.setFont(font)
        self.btnRegresar.setMouseTracking(True)
        self.btnRegresar.setStyleSheet(_fromUtf8("Color:rgb(223, 15, 90);"))
        self.btnRegresar.setObjectName(_fromUtf8("btnRegresar"))
        self.btnCambiarContrasena = QtGui.QPushButton(self.centralwidget)
        self.btnCambiarContrasena.setGeometry(QtCore.QRect(220, 350, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.btnCambiarContrasena.setFont(font)
        self.btnCambiarContrasena.setMouseTracking(True)
        self.btnCambiarContrasena.setStyleSheet(_fromUtf8("Color:rgb(1, 137, 125);"))
        self.btnCambiarContrasena.setObjectName(_fromUtf8("btnCambiarContrasena"))
        self.lblPassNueva = QtGui.QLabel(self.centralwidget)
        self.lblPassNueva.setGeometry(QtCore.QRect(50, 230, 131, 17))
        self.lblPassNueva.setObjectName(_fromUtf8("lblPassNueva"))
        self.lblPasswVerificar = QtGui.QLabel(self.centralwidget)
        self.lblPasswVerificar.setGeometry(QtCore.QRect(50, 280, 141, 17))
        self.lblPasswVerificar.setObjectName(_fromUtf8("lblPasswVerificar"))
        cambiarContrasena.setCentralWidget(self.centralwidget)

        self.retranslateUi(cambiarContrasena)
        QtCore.QMetaObject.connectSlotsByName(cambiarContrasena)

    def retranslateUi(self, cambiarContrasena):
        cambiarContrasena.setWindowTitle(_translate("cambiarContrasena", "Cambiar Contraseña", None))
        self.lblCambiarContrasena.setText(_translate("cambiarContrasena", "CAMBIAR CONTRASEÑA", None))
        self.lblUser.setText(_translate("cambiarContrasena", "Usuario", None))
        self.lblPasswAntigua.setText(_translate("cambiarContrasena", "Contraseña", None))
        self.txtUser.setToolTip(_translate("cambiarContrasena", "Usuario", None))
        self.txtPassw.setToolTip(_translate("cambiarContrasena", "contraseña Actual", None))
        self.txtPasswNueva.setToolTip(_translate("cambiarContrasena", "Contraseña Nueva", None))
        self.txtPasswVerificar.setToolTip(_translate("cambiarContrasena", "Verificar Contraseña", None))
        self.lblBazarPapeleriaLulita.setText(_translate("cambiarContrasena", "BAZAR Y PAPELERIA LULITA", None))
        self.lblDireccion.setText(_translate("cambiarContrasena", "Km 8 1/2 via Daule - Cdla. \"La Gaviota\" Mz. 2262 V. 7", None))
        self.btnRegresar.setToolTip(_translate("cambiarContrasena", "<html><head/><body><p><span style=\" color:#ffffff;\">REGRESAR</span></p></body></html>", None))
        self.btnRegresar.setText(_translate("cambiarContrasena", "REGRESAR", None))
        self.btnCambiarContrasena.setToolTip(_translate("cambiarContrasena", "<html><head/><body><p><span style=\" color:#ffffff;\">CAMBIAR CONTRASEÑA</span></p></body></html>", None))
        self.btnCambiarContrasena.setText(_translate("cambiarContrasena", "CAMBIAR CONTRASEÑA", None))
        self.lblPassNueva.setText(_translate("cambiarContrasena", "Contraseña Nueva", None))
        self.lblPasswVerificar.setText(_translate("cambiarContrasena", "Verificar Contraseña", None))


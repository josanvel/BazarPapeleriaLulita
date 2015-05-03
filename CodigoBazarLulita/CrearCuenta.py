# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crearcuenta.ui'
#
# Created: Mon Apr 20 10:58:39 2015
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

class Ui_crearCuenta(QtGui.QMainWindow):
    def setupUi(self, crearCuenta):
        crearCuenta.setObjectName(_fromUtf8("crearCuenta"))
        crearCuenta.resize(450, 420)
        crearCuenta.setMinimumSize(QtCore.QSize(450, 420))
        crearCuenta.setMaximumSize(QtCore.QSize(450, 420))
        self.centralwidget = QtGui.QWidget(crearCuenta)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lblCrearCuenta = QtGui.QLabel(self.centralwidget)
        self.lblCrearCuenta.setGeometry(QtCore.QRect(150, 90, 141, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblCrearCuenta.setFont(font)
        self.lblCrearCuenta.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.lblCrearCuenta.setObjectName(_fromUtf8("lblCrearCuenta"))
        self.lblBazarPapeleriaLulita = QtGui.QLabel(self.centralwidget)
        self.lblBazarPapeleriaLulita.setGeometry(QtCore.QRect(100, 30, 251, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblBazarPapeleriaLulita.setFont(font)
        self.lblBazarPapeleriaLulita.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblBazarPapeleriaLulita.setObjectName(_fromUtf8("lblBazarPapeleriaLulita"))
        self.lblDireccion = QtGui.QLabel(self.centralwidget)
        self.lblDireccion.setGeometry(QtCore.QRect(10, 50, 420, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblDireccion.setObjectName(_fromUtf8("lblDireccion"))
        self.lblTipoCuenta = QtGui.QLabel(self.centralwidget)
        self.lblTipoCuenta.setGeometry(QtCore.QRect(60, 170, 111, 17))
        self.lblTipoCuenta.setObjectName(_fromUtf8("lblTipoCuenta"))
        self.cbxTipoCuenta = QtGui.QComboBox(self.centralwidget)
        self.cbxTipoCuenta.setGeometry(QtCore.QRect(210, 170, 171, 20))
        self.cbxTipoCuenta.setObjectName(_fromUtf8("cbxTipoCuenta"))
        self.lblUser = QtGui.QLabel(self.centralwidget)
        self.lblUser.setGeometry(QtCore.QRect(60, 220, 81, 20))
        self.lblUser.setObjectName(_fromUtf8("lblUser"))
        self.txtUser = QtGui.QLineEdit(self.centralwidget)
        self.txtUser.setGeometry(QtCore.QRect(210, 220, 171, 20))
        self.txtUser.setObjectName(_fromUtf8("txtUser"))
        self.txtPasw = QtGui.QLineEdit(self.centralwidget)
        self.txtPasw.setGeometry(QtCore.QRect(210, 270, 171, 20))
        self.txtPasw.setObjectName(_fromUtf8("txtPasw"))
        self.lblPasw = QtGui.QLabel(self.centralwidget)
        self.lblPasw.setGeometry(QtCore.QRect(60, 270, 81, 20))
        self.lblPasw.setObjectName(_fromUtf8("lblPasw"))
        self.btnRegresar = QtGui.QPushButton(self.centralwidget)
        self.btnRegresar.setGeometry(QtCore.QRect(50, 340, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegresar.setFont(font)
        self.btnRegresar.setMouseTracking(True)
        self.btnRegresar.setStyleSheet(_fromUtf8("Color:rgb(223, 15, 90);"))
        self.btnRegresar.setObjectName(_fromUtf8("btnRegresar"))
        self.btnCrearCuenta = QtGui.QPushButton(self.centralwidget)
        self.btnCrearCuenta.setGeometry(QtCore.QRect(220, 340, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btnCrearCuenta.setFont(font)
        self.btnCrearCuenta.setMouseTracking(True)
        self.btnCrearCuenta.setStyleSheet(_fromUtf8("Color:rgb(1, 137, 125);"))
        self.btnCrearCuenta.setObjectName(_fromUtf8("btnCrearCuenta"))
        crearCuenta.setCentralWidget(self.centralwidget)

        self.retranslateUi(crearCuenta)
        QtCore.QMetaObject.connectSlotsByName(crearCuenta)

    def retranslateUi(self, crearCuenta):
        crearCuenta.setWindowTitle(_translate("crearCuenta", "Crear Cuenta", None))
        self.lblCrearCuenta.setText(_translate("crearCuenta", "CREAR CUENTA", None))
        self.lblBazarPapeleriaLulita.setText(_translate("crearCuenta", "BAZAR Y PAPELERIA LULITA", None))
        self.lblDireccion.setText(_translate("crearCuenta", "Km 8 1/2 via Daule - Cdla. \"La Gaviota\" Mz. 2262 V. 7", None))
        self.lblTipoCuenta.setText(_translate("crearCuenta", "Tipo de Cuenta", None))
        self.cbxTipoCuenta.setToolTip(_translate("crearCuenta", "Tipo de Cuenta", None))
        self.lblUser.setText(_translate("crearCuenta", "Usuario", None))
        self.txtUser.setToolTip(_translate("crearCuenta", "Usuario", None))
        self.txtPasw.setToolTip(_translate("crearCuenta", "Contraseña", None))
        self.lblPasw.setText(_translate("crearCuenta", "Contraseña", None))
        self.btnRegresar.setToolTip(_translate("crearCuenta", "<html><head/><body><p><span style=\" color:#ffffff;\">Regresar</span></p></body></html>", None))
        self.btnRegresar.setText(_translate("crearCuenta", "REGRESAR", None))
        self.btnCrearCuenta.setToolTip(_translate("crearCuenta", "<html><head/><body><p><span style=\" color:#ffffff;\">Crear Cuenta</span></p></body></html>", None))
        self.btnCrearCuenta.setText(_translate("crearCuenta", "CREAR CUENTA", None))
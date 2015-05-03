# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaprincipal.ui'
#
# Created: Sun Mar 15 14:04:06 2015
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

class Ui_VentanaPrincipal(QtGui.QMainWindow):
    def setupUi(self, VentanaPrincipal):
        VentanaPrincipal.setObjectName(_fromUtf8("VentanaPrincipal"))
        VentanaPrincipal.resize(650, 420)
        VentanaPrincipal.setMinimumSize(QtCore.QSize(650, 420))
        VentanaPrincipal.setMaximumSize(QtCore.QSize(650, 420))
        font = QtGui.QFont()
        font.setPointSize(17)
        VentanaPrincipal.setFont(font)
        VentanaPrincipal.setMouseTracking(True)
        self.cwgtPrincipal = QtGui.QWidget(VentanaPrincipal)
        self.cwgtPrincipal.setObjectName(_fromUtf8("cwgtPrincipal"))
        self.lblBazarPapeleria = QtGui.QLabel(self.cwgtPrincipal)
        self.lblBazarPapeleria.setGeometry(QtCore.QRect(110, 40, 425, 35))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.lblBazarPapeleria.setFont(font)
        self.lblBazarPapeleria.setCursor(QtGui.QCursor(QtCore.Qt.SizeBDiagCursor))
        self.lblBazarPapeleria.setStyleSheet(_fromUtf8("color: rgb(51, 102, 255);"))
        self.lblBazarPapeleria.setObjectName(_fromUtf8("lblBazarPapeleria"))
        self.btnAgregar = QtGui.QPushButton(self.cwgtPrincipal)
        self.btnAgregar.setGeometry(QtCore.QRect(70, 120, 170, 110))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnAgregar.setFont(font)
        self.btnAgregar.setStyleSheet(_fromUtf8("color: rgb(223, 15, 90);\n"
""))
        self.btnAgregar.setObjectName(_fromUtf8("btnAgregar"))
        self.btnFacturacion = QtGui.QPushButton(self.cwgtPrincipal)
        self.btnFacturacion.setGeometry(QtCore.QRect(260, 120, 320, 110))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnFacturacion.setFont(font)
        self.btnFacturacion.setStyleSheet(_fromUtf8("Color:rgb(1, 137, 125);"))
        self.btnFacturacion.setObjectName(_fromUtf8("btnFacturacion"))
        self.btnReportes = QtGui.QPushButton(self.cwgtPrincipal)
        self.btnReportes.setGeometry(QtCore.QRect(70, 250, 320, 110))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnReportes.setFont(font)
        self.btnReportes.setStyleSheet(_fromUtf8("Color:rgb(191, 197, 1);"))
        self.btnReportes.setObjectName(_fromUtf8("btnReportes"))
        self.btnActualizar = QtGui.QPushButton(self.cwgtPrincipal)
        self.btnActualizar.setGeometry(QtCore.QRect(410, 250, 170, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btnActualizar.setFont(font)
        self.btnActualizar.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.btnActualizar.setObjectName(_fromUtf8("btnActualizar"))
        self.btnCuentas = QtGui.QPushButton(self.cwgtPrincipal)
        self.btnCuentas.setGeometry(QtCore.QRect(410, 310, 170, 50))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btnCuentas.setFont(font)
        self.btnCuentas.setStyleSheet(_fromUtf8("Color:rgb(0, 0, 0);"))
        self.btnCuentas.setObjectName(_fromUtf8("btnCuentas"))
        VentanaPrincipal.setCentralWidget(self.cwgtPrincipal)

        self.retranslateUi(VentanaPrincipal)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipal)

    def retranslateUi(self, VentanaPrincipal):
        VentanaPrincipal.setWindowTitle(_translate("VentanaPrincipal", "Ventana Principal", None))
        self.lblBazarPapeleria.setText(_translate("VentanaPrincipal", "BAZAR Y PAPELERIA LULITA", None))
        self.btnAgregar.setToolTip(_translate("VentanaPrincipal", "<html><head/><body><p><span style=\" color:#ffffff;\">AGREGAR</span></p></body></html>", None))
        self.btnAgregar.setText(_translate("VentanaPrincipal", "AGREGAR", None))
        self.btnFacturacion.setToolTip(_translate("VentanaPrincipal", "<html><head/><body><p><span style=\" color:#ffffff;\">FACTURACION</span></p></body></html>", None))
        self.btnFacturacion.setText(_translate("VentanaPrincipal", "FACTURACION", None))
        self.btnReportes.setToolTip(_translate("VentanaPrincipal", "<html><head/><body><p><span style=\" color:#ffffff;\">REPORTES</span></p></body></html>", None))
        self.btnReportes.setText(_translate("VentanaPrincipal", "REPORTES", None))
        self.btnActualizar.setToolTip(_translate("VentanaPrincipal", "<html><head/><body><p><span style=\" color:#ffffff;\">ACTUALIZAR</span></p></body></html>", None))
        self.btnActualizar.setText(_translate("VentanaPrincipal", "ACTUALIZAR", None))
        self.btnCuentas.setToolTip(_translate("VentanaPrincipal", "<html><head/><body><p><span style=\" color:#ffffff;\">ELIMINAR</span></p></body></html>", None))
        self.btnCuentas.setText(_translate("VentanaPrincipal", "CUENTAS", None))


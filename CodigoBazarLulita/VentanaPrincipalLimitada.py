# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaprincipallimitada.ui'
#
# Created: Mon Apr 20 11:56:26 2015
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

class Ui_VentanaPrincipalLimitada(QtGui.QMainWindow):
    def setupUi(self, VentanaPrincipalLimitada):
        VentanaPrincipalLimitada.setObjectName(_fromUtf8("VentanaPrincipalLimitada"))
        VentanaPrincipalLimitada.resize(650, 420)
        VentanaPrincipalLimitada.setMinimumSize(QtCore.QSize(650, 420))
        VentanaPrincipalLimitada.setMaximumSize(QtCore.QSize(650, 420))
        self.centralwidget = QtGui.QWidget(VentanaPrincipalLimitada)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.btnReportes = QtGui.QPushButton(self.centralwidget)
        self.btnReportes.setGeometry(QtCore.QRect(70, 250, 320, 110))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnReportes.setFont(font)
        self.btnReportes.setStyleSheet(_fromUtf8("Color:rgb(191, 197, 1);"))
        self.btnReportes.setObjectName(_fromUtf8("btnReportes"))
        self.lblBazarPapeleria = QtGui.QLabel(self.centralwidget)
        self.lblBazarPapeleria.setGeometry(QtCore.QRect(110, 40, 425, 35))
        font = QtGui.QFont()
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.lblBazarPapeleria.setFont(font)
        self.lblBazarPapeleria.setCursor(QtGui.QCursor(QtCore.Qt.SizeBDiagCursor))
        self.lblBazarPapeleria.setStyleSheet(_fromUtf8("color: rgb(51, 102, 255);"))
        self.lblBazarPapeleria.setObjectName(_fromUtf8("lblBazarPapeleria"))
        self.btnFacturacion = QtGui.QPushButton(self.centralwidget)
        self.btnFacturacion.setGeometry(QtCore.QRect(69, 120, 511, 110))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.btnFacturacion.setFont(font)
        self.btnFacturacion.setStyleSheet(_fromUtf8("Color:rgb(1, 137, 125);"))
        self.btnFacturacion.setObjectName(_fromUtf8("btnFacturacion"))
        self.btnActualizar = QtGui.QPushButton(self.centralwidget)
        self.btnActualizar.setGeometry(QtCore.QRect(410, 250, 170, 110))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.btnActualizar.setFont(font)
        self.btnActualizar.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.btnActualizar.setObjectName(_fromUtf8("btnActualizar"))
        VentanaPrincipalLimitada.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaPrincipalLimitada)
        QtCore.QMetaObject.connectSlotsByName(VentanaPrincipalLimitada)

    def retranslateUi(self, VentanaPrincipalLimitada):
        VentanaPrincipalLimitada.setWindowTitle(_translate("VentanaPrincipalLimitada", "MainWindow", None))
        self.btnReportes.setToolTip(_translate("VentanaPrincipalLimitada", "<html><head/><body><p><span style=\" color:#ffffff;\">REPORTES</span></p></body></html>", None))
        self.btnReportes.setText(_translate("VentanaPrincipalLimitada", "REPORTES", None))
        self.lblBazarPapeleria.setText(_translate("VentanaPrincipalLimitada", "BAZAR Y PAPELERIA LULITA", None))
        self.btnFacturacion.setToolTip(_translate("VentanaPrincipalLimitada", "<html><head/><body><p><span style=\" color:#ffffff;\">FACTURACION</span></p></body></html>", None))
        self.btnFacturacion.setText(_translate("VentanaPrincipalLimitada", "FACTURACION", None))
        self.btnActualizar.setToolTip(_translate("VentanaPrincipalLimitada", "<html><head/><body><p><span style=\" color:#ffffff;\">ACTUALIZAR</span></p></body></html>", None))
        self.btnActualizar.setText(_translate("VentanaPrincipalLimitada", "ACTUALIZAR", None))


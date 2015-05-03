# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'botonesreportes.ui'
#
# Created: Sun Mar 15 12:22:55 2015
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

class Ui_BotonesReportes(object):
    def setupUi(self, BotonesReportes):
        BotonesReportes.setObjectName(_fromUtf8("BotonesReportes"))
        BotonesReportes.resize(450, 370)
        BotonesReportes.setMinimumSize(QtCore.QSize(450, 370))
        BotonesReportes.setMaximumSize(QtCore.QSize(450, 370))
        self.btnReporteProductos = QtGui.QPushButton(BotonesReportes)
        self.btnReporteProductos.setGeometry(QtCore.QRect(25, 180, 410, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnReporteProductos.setFont(font)
        self.btnReporteProductos.setStyleSheet(_fromUtf8("Color:rgb(191, 197, 1);"))
        self.btnReporteProductos.setObjectName(_fromUtf8("btnReporteProductos"))
        self.btnRegresarReportes = QtGui.QPushButton(BotonesReportes)
        self.btnRegresarReportes.setGeometry(QtCore.QRect(230, 270, 200, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegresarReportes.setFont(font)
        self.btnRegresarReportes.setStyleSheet(_fromUtf8("color: rgb(51, 102, 255);"))
        self.btnRegresarReportes.setObjectName(_fromUtf8("btnRegresarReportes"))
        self.btnReporteGanancias = QtGui.QPushButton(BotonesReportes)
        self.btnReporteGanancias.setGeometry(QtCore.QRect(25, 110, 410, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnReporteGanancias.setFont(font)
        self.btnReporteGanancias.setStyleSheet(_fromUtf8("Color:rgb(191, 197, 1);"))
        self.btnReporteGanancias.setObjectName(_fromUtf8("btnReporteGanancias"))
        self.lblReportes = QtGui.QLabel(BotonesReportes)
        self.lblReportes.setGeometry(QtCore.QRect(60, 40, 341, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblReportes.setFont(font)
        self.lblReportes.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.lblReportes.setObjectName(_fromUtf8("lblReportes"))

        self.retranslateUi(BotonesReportes)
        QtCore.QMetaObject.connectSlotsByName(BotonesReportes)

    def retranslateUi(self, BotonesReportes):
        BotonesReportes.setWindowTitle(_translate("BotonesReportes", "Reportes", None))
        self.btnReporteProductos.setToolTip(_translate("BotonesReportes", "<html><head/><body><p>Reporte Productos</p></body></html>", None))
        self.btnReporteProductos.setText(_translate("BotonesReportes", "REPORTE PRODUCTOS", None))
        self.btnRegresarReportes.setToolTip(_translate("BotonesReportes", "<html><head/><body><p><span style=\" color:#ffffff;\">REGRESAR</span></p></body></html>", None))
        self.btnRegresarReportes.setText(_translate("BotonesReportes", "REGRESAR", None))
        self.btnReporteGanancias.setToolTip(_translate("BotonesReportes", "<html><head/><body><p>Reporte Ganancias</p></body></html>", None))
        self.btnReporteGanancias.setText(_translate("BotonesReportes", "REPORTE GANANCIAS", None))
        self.lblReportes.setText(_translate("BotonesReportes", "REPORTES BAZAR Y PAPELERIA", None))


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reporteproducto.ui'
#
# Created: Sun Mar 15 12:32:36 2015
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

class Ui_ReporteProducto(object):
    def setupUi(self, ReporteProducto):
        ReporteProducto.setObjectName(_fromUtf8("ReporteProducto"))
        ReporteProducto.resize(500, 140)
        ReporteProducto.setMaximumSize(QtCore.QSize(500, 140))
        self.lblModificar = QtGui.QLabel(ReporteProducto)
        self.lblModificar.setGeometry(QtCore.QRect(105, 50, 291, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblModificar.setFont(font)
        self.lblModificar.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.lblModificar.setObjectName(_fromUtf8("lblModificar"))
        self.lblBazarPapeleriaLulita = QtGui.QLabel(ReporteProducto)
        self.lblBazarPapeleriaLulita.setGeometry(QtCore.QRect(130, 0, 240, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblBazarPapeleriaLulita.setFont(font)
        self.lblBazarPapeleriaLulita.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblBazarPapeleriaLulita.setObjectName(_fromUtf8("lblBazarPapeleriaLulita"))
        self.lblDireccion = QtGui.QLabel(ReporteProducto)
        self.lblDireccion.setGeometry(QtCore.QRect(40, 20, 420, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblDireccion.setObjectName(_fromUtf8("lblDireccion"))
        self.btnGuadar = QtGui.QPushButton(ReporteProducto)
        self.btnGuadar.setGeometry(QtCore.QRect(260, 100, 200, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnGuadar.setFont(font)
        self.btnGuadar.setMouseTracking(True)
        self.btnGuadar.setStyleSheet(_fromUtf8("Color:rgb(1, 137, 125);"))
        self.btnGuadar.setObjectName(_fromUtf8("btnGuadar"))
        self.btnRegresar = QtGui.QPushButton(ReporteProducto)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 100, 200, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegresar.setFont(font)
        self.btnRegresar.setMouseTracking(True)
        self.btnRegresar.setStyleSheet(_fromUtf8("Color:rgb(223, 15, 90);"))
        self.btnRegresar.setObjectName(_fromUtf8("btnCancelar"))

        self.retranslateUi(ReporteProducto)
        QtCore.QMetaObject.connectSlotsByName(ReporteProducto)

    def retranslateUi(self, ReporteProducto):
        ReporteProducto.setWindowTitle(_translate("ReporteProducto", "Reporte Producto", None))
        self.lblModificar.setText(_translate("ReporteProducto", "Reporte de productos en Stock", None))
        self.lblBazarPapeleriaLulita.setText(_translate("ReporteProducto", "BAZAR Y PAPELERIA LULITA", None))
        self.lblDireccion.setText(_translate("ReporteProducto", "Km 8 1/2 via Daule - Cdla. \"La Gaviota\" Mz. 2262 V. 7", None))
        self.btnGuadar.setToolTip(_translate("ReporteProducto", "<html><head/><body><p><span style=\" color:#ffffff;\">GENERAR</span></p></body></html>", None))
        self.btnGuadar.setText(_translate("ReporteProducto", "GENERAR", None))
        self.btnRegresar.setToolTip(_translate("ReporteProducto", "<html><head/><body><p><span style=\" color:#ffffff;\">REGRESAR</span></p></body></html>", None))
        self.btnRegresar.setText(_translate("ReporteProducto", "REGRESAR", None))


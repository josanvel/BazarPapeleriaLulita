# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingresarproducto.ui'
#
# Created: Thu Apr 30 23:14:22 2015
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

class Ui_IngresarProducto(object):
    def setupUi(self, IngresarProducto):
        IngresarProducto.setObjectName(_fromUtf8("IngresarProducto"))
        IngresarProducto.resize(500, 140)
        IngresarProducto.setMinimumSize(QtCore.QSize(500, 140))
        IngresarProducto.setMaximumSize(QtCore.QSize(500, 140))
        self.tblWProductoStock = QtGui.QTableWidget(IngresarProducto)
        self.tblWProductoStock.setGeometry(QtCore.QRect(20, 10, 461, 81))
        self.tblWProductoStock.setMouseTracking(True)
        self.tblWProductoStock.setObjectName(_fromUtf8("tblWProductoStock"))
        self.tblWProductoStock.setColumnCount(0)
        self.tblWProductoStock.setRowCount(0)
        self.label = QtGui.QLabel(IngresarProducto)
        self.label.setGeometry(QtCore.QRect(20, 100, 67, 25))
        self.label.setObjectName(_fromUtf8("label"))
        self.spinBox = QtGui.QSpinBox(IngresarProducto)
        self.spinBox.setGeometry(QtCore.QRect(90, 100, 61, 25))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.btnAceptar = QtGui.QPushButton(IngresarProducto)
        self.btnAceptar.setGeometry(QtCore.QRect(320, 100, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnAceptar.setFont(font)
        self.btnAceptar.setStyleSheet(_fromUtf8("Color:rgb(1, 137, 125);"))
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.btnCancelar = QtGui.QPushButton(IngresarProducto)
        self.btnCancelar.setGeometry(QtCore.QRect(190, 100, 131, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setStyleSheet(_fromUtf8("Color:rgb(223, 15, 90);"))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))

        self.retranslateUi(IngresarProducto)
        QtCore.QMetaObject.connectSlotsByName(IngresarProducto)

    def retranslateUi(self, IngresarProducto):
        IngresarProducto.setWindowTitle(_translate("IngresarProducto", "Ingresar Producto", None))
        self.tblWProductoStock.setToolTip(_translate("IngresarProducto", "<html><head/><body><p><span style=\" color:#ffffff;\">Detalle</span></p></body></html>", None))
        self.label.setText(_translate("IngresarProducto", "Cantidad", None))
        self.btnAceptar.setToolTip(_translate("IngresarProducto", "<html><head/><body><p><span style=\" color:#ffffff;\">ACEPTAR</span></p></body></html>", None))
        self.btnAceptar.setText(_translate("IngresarProducto", "ACEPTAR", None))
        self.btnCancelar.setToolTip(_translate("IngresarProducto", "<html><head/><body><p><span style=\" color:#ffffff;\">CANCELAR</span></p></body></html>", None))
        self.btnCancelar.setText(_translate("IngresarProducto", "CANCELAR", None))

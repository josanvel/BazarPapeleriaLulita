# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ingresarproducto.ui'
#
# Created: Sun Mar 15 12:31:18 2015
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
        IngresarProducto.setMaximumSize(QtCore.QSize(500, 140))
        self.tblVwProductoStock = QtGui.QTableView(IngresarProducto)
        self.tblVwProductoStock.setGeometry(QtCore.QRect(20, 10, 461, 81))
        self.tblVwProductoStock.setMouseTracking(True)
        self.tblVwProductoStock.setObjectName(_fromUtf8("tblVwProductoStock"))
        self.tblVwProductoStock.horizontalHeader().setCascadingSectionResizes(True)
        self.tblVwProductoStock.horizontalHeader().setSortIndicatorShown(True)
        self.tblVwProductoStock.horizontalHeader().setStretchLastSection(True)
        self.tblVwProductoStock.verticalHeader().setVisible(False)
        self.btnAceptar = QtGui.QPushButton(IngresarProducto)
        self.btnAceptar.setGeometry(QtCore.QRect(319, 100, 160, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnAceptar.setFont(font)
        self.btnAceptar.setStyleSheet(_fromUtf8("Color:rgb(1, 137, 125);"))
        self.btnAceptar.setObjectName(_fromUtf8("btnAceptar"))
        self.btnCancelar = QtGui.QPushButton(IngresarProducto)
        self.btnCancelar.setGeometry(QtCore.QRect(179, 100, 131, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnCancelar.setFont(font)
        self.btnCancelar.setStyleSheet(_fromUtf8("Color:rgb(223, 15, 90);"))
        self.btnCancelar.setObjectName(_fromUtf8("btnCancelar"))
        self.txtCantidad = QtGui.QLineEdit(IngresarProducto)
        self.txtCantidad.setGeometry(QtCore.QRect(20, 100, 121, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        self.txtCantidad.setFont(font)
        self.txtCantidad.setText(_fromUtf8(""))
        self.txtCantidad.setObjectName(_fromUtf8("txtCantidad"))

        self.retranslateUi(IngresarProducto)
        QtCore.QMetaObject.connectSlotsByName(IngresarProducto)

    def retranslateUi(self, IngresarProducto):
        IngresarProducto.setWindowTitle(_translate("IngresarProducto", "Ingresar Producto", None))
        self.tblVwProductoStock.setToolTip(_translate("IngresarProducto", "<html><head/><body><p><span style=\" color:#ffffff;\">Detalle</span></p></body></html>", None))
        self.btnAceptar.setToolTip(_translate("IngresarProducto", "<html><head/><body><p><span style=\" color:#ffffff;\">ACEPTAR</span></p></body></html>", None))
        self.btnAceptar.setText(_translate("IngresarProducto", "ACEPTAR", None))
        self.btnCancelar.setToolTip(_translate("IngresarProducto", "<html><head/><body><p><span style=\" color:#ffffff;\">CANCELAR</span></p></body></html>", None))
        self.btnCancelar.setText(_translate("IngresarProducto", "CANCELAR", None))
        self.txtCantidad.setToolTip(_translate("IngresarProducto", "<html><head/><body><p><span style=\" color:#ffffff;\">Cantidad producto</span></p></body></html>", None))
        self.txtCantidad.setPlaceholderText(_translate("IngresarProducto", "Ingrese cantidad", None))


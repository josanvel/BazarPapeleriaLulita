# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'botonesactualizar.ui'
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

class Ui_BotonesActualizar(object):
    def setupUi(self, BotonesActualizar):
        BotonesActualizar.setObjectName(_fromUtf8("BotonesActualizar"))
        BotonesActualizar.resize(450, 370)
        BotonesActualizar.setMaximumSize(QtCore.QSize(450, 370))
        self.btnActualizarModificar = QtGui.QPushButton(BotonesActualizar)
        self.btnActualizarModificar.setGeometry(QtCore.QRect(25, 120, 410, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnActualizarModificar.setFont(font)
        self.btnActualizarModificar.setStyleSheet(_fromUtf8("Color:rgb(191, 197, 1);"))
        self.btnActualizarModificar.setObjectName(_fromUtf8("btnActualizarModificar"))
        self.btnActualizarCambiar = QtGui.QPushButton(BotonesActualizar)
        self.btnActualizarCambiar.setGeometry(QtCore.QRect(25, 190, 410, 40))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnActualizarCambiar.setFont(font)
        self.btnActualizarCambiar.setStyleSheet(_fromUtf8("Color:rgb(191, 197, 1);"))
        self.btnActualizarCambiar.setObjectName(_fromUtf8("btnActualizarCambiar"))
        self.btnRegresarActualizar = QtGui.QPushButton(BotonesActualizar)
        self.btnRegresarActualizar.setGeometry(QtCore.QRect(230, 280, 200, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegresarActualizar.setFont(font)
        self.btnRegresarActualizar.setStyleSheet(_fromUtf8("color: rgb(51, 102, 255);"))
        self.btnRegresarActualizar.setObjectName(_fromUtf8("btnRegresarActualizar"))
        self.lblActualizarProducto = QtGui.QLabel(BotonesActualizar)
        self.lblActualizarProducto.setGeometry(QtCore.QRect(80, 40, 291, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblActualizarProducto.setFont(font)
        self.lblActualizarProducto.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.lblActualizarProducto.setObjectName(_fromUtf8("lblActualizarProducto"))

        self.retranslateUi(BotonesActualizar)
        QtCore.QMetaObject.connectSlotsByName(BotonesActualizar)

    def retranslateUi(self, BotonesActualizar):
        BotonesActualizar.setWindowTitle(_translate("BotonesActualizar", "ACTUALIZAR", None))
        self.btnActualizarModificar.setToolTip(_translate("BotonesActualizar", "<html><head/><body><p>Modificar Cantidad Producto</p></body></html>", None))
        self.btnActualizarModificar.setText(_translate("BotonesActualizar", "MODIFICAR CANTIDAD PRODUCTO", None))
        self.btnActualizarCambiar.setToolTip(_translate("BotonesActualizar", "<html><head/><body><p>Cambiar Precio Producto</p></body></html>", None))
        self.btnActualizarCambiar.setText(_translate("BotonesActualizar", "CAMBIAR PRECIO PRODUCTO", None))
        self.btnRegresarActualizar.setToolTip(_translate("BotonesActualizar", "<html><head/><body><p><span style=\" color:#ffffff;\">REGRESAR</span></p></body></html>", None))
        self.btnRegresarActualizar.setText(_translate("BotonesActualizar", "REGRESAR", None))
        self.lblActualizarProducto.setText(_translate("BotonesActualizar", "ACTUALIZAR  PRODUCTOS", None))


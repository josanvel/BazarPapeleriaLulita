# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'agregar.ui'
#
# Created: Sun Mar 15 12:18:41 2015
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

class Ui_Agregar(object):
    def setupUi(self, Agregar):
        Agregar.setObjectName(_fromUtf8("Agregar"))
        Agregar.resize(450, 370)
        Agregar.setMaximumSize(QtCore.QSize(450, 370))
        self.btnAgregar = QtGui.QPushButton(Agregar)
        self.btnAgregar.setGeometry(QtCore.QRect(230, 320, 200, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnAgregar.setFont(font)
        self.btnAgregar.setMouseTracking(True)
        self.btnAgregar.setStyleSheet(_fromUtf8("Color:rgb(1, 137, 125);"))
        self.btnAgregar.setObjectName(_fromUtf8("btnAgregar"))
        self.lblAgregar = QtGui.QLabel(Agregar)
        self.lblAgregar.setGeometry(QtCore.QRect(40, 70, 360, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblAgregar.setFont(font)
        self.lblAgregar.setMouseTracking(True)
        self.lblAgregar.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.lblAgregar.setObjectName(_fromUtf8("lblAgregar"))
        self.lblBazarPapeleriaLulita = QtGui.QLabel(Agregar)
        self.lblBazarPapeleriaLulita.setGeometry(QtCore.QRect(110, 0, 240, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblBazarPapeleriaLulita.setFont(font)
        self.lblBazarPapeleriaLulita.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblBazarPapeleriaLulita.setObjectName(_fromUtf8("lblBazarPapeleriaLulita"))
        self.lblDireccion = QtGui.QLabel(Agregar)
        self.lblDireccion.setGeometry(QtCore.QRect(10, 20, 420, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblDireccion.setObjectName(_fromUtf8("lblDireccion"))
        self.btnRegresar = QtGui.QPushButton(Agregar)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 320, 200, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegresar.setFont(font)
        self.btnRegresar.setMouseTracking(True)
        self.btnRegresar.setStyleSheet(_fromUtf8("Color:rgb(223, 15, 90);"))
        self.btnRegresar.setObjectName(_fromUtf8("btnRegresar"))
        self.txtBuscar = QtGui.QLineEdit(Agregar)
        self.txtBuscar.setGeometry(QtCore.QRect(40, 120, 351, 25))
        self.txtBuscar.setAutoFillBackground(True)
        self.txtBuscar.setObjectName(_fromUtf8("txtBuscar"))
        self.lblCantidad = QtGui.QLabel(Agregar)
        self.lblCantidad.setGeometry(QtCore.QRect(40, 170, 91, 17))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lblCantidad.setFont(font)
        self.lblCantidad.setObjectName(_fromUtf8("lblCantidad"))
        self.txtPrecioUnitarioReal = QtGui.QLineEdit(Agregar)
        self.txtPrecioUnitarioReal.setGeometry(QtCore.QRect(40, 210, 351, 25))
        self.txtPrecioUnitarioReal.setAutoFillBackground(True)
        self.txtPrecioUnitarioReal.setObjectName(_fromUtf8("txtPrecioUnitarioReal"))
        self.txtPrecioUnitarioIva = QtGui.QLineEdit(Agregar)
        self.txtPrecioUnitarioIva.setGeometry(QtCore.QRect(40, 260, 351, 25))
        self.txtPrecioUnitarioIva.setAutoFillBackground(True)
        self.txtPrecioUnitarioIva.setObjectName(_fromUtf8("txtPrecioUnitarioIva"))
        self.spinBox = QtGui.QSpinBox(Agregar)
        self.spinBox.setGeometry(QtCore.QRect(200, 165, 191, 27))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))

        self.retranslateUi(Agregar)
        QtCore.QMetaObject.connectSlotsByName(Agregar)

    def retranslateUi(self, Agregar):
        Agregar.setWindowTitle(_translate("Agregar", "Agregar Producto", None))
        self.btnAgregar.setToolTip(_translate("Agregar", "<html><head/><body><p><span style=\" color:#ffffff;\">AGREGAR</span></p></body></html>", None))
        self.btnAgregar.setText(_translate("Agregar", "AGREGAR", None))
        self.lblAgregar.setToolTip(_translate("Agregar", "Agregar", None))
        self.lblAgregar.setText(_translate("Agregar", "Agregar producto al Bazar y Papeleria", None))
        self.lblBazarPapeleriaLulita.setText(_translate("Agregar", "BAZAR Y PAPELERIA LULITA", None))
        self.lblDireccion.setText(_translate("Agregar", "Km 8 1/2 via Daule - Cdla. \"La Gaviota\" Mz. 2262 V. 7", None))
        self.btnRegresar.setToolTip(_translate("Agregar", "<html><head/><body><p><span style=\" color:#ffffff;\">REGRESAR</span></p></body></html>", None))
        self.btnRegresar.setText(_translate("Agregar", "REGRESAR", None))
        self.txtBuscar.setToolTip(_translate("Agregar", "<html><head/><body><p><span style=\" color:#ffffff;\">Descripcion del producto</span></p></body></html>", None))
        self.txtBuscar.setPlaceholderText(_translate("Agregar", "Descripción del producto nuevo", None))
        self.lblCantidad.setText(_translate("Agregar", "Cantidad", None))
        self.txtPrecioUnitarioReal.setToolTip(_translate("Agregar", "<html><head/><body><p><span style=\" color:#ffffff;\">Precio real</span></p></body></html>", None))
        self.txtPrecioUnitarioReal.setPlaceholderText(_translate("Agregar", "Ingrese el precio del producto real", None))
        self.txtPrecioUnitarioIva.setToolTip(_translate("Agregar", "<html><head/><body><p><span style=\" color:#ffffff;\">Precio con Iva</span></p></body></html>", None))
        self.txtPrecioUnitarioIva.setPlaceholderText(_translate("Agregar", "Ingrese el precio del producto con Iva", None))
        self.spinBox.setToolTip(_translate("Agregar", "<html><head/><body><p><span style=\" color:#ffffff;\">Cantidad del producto</span></p></body></html>", None))


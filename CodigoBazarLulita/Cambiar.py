# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cambiar.ui'
#
# Created: Fri May  1 17:39:13 2015
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

class Ui_Cambiar(object):
    def setupUi(self, Cambiar):
        Cambiar.setObjectName(_fromUtf8("Cambiar"))
        Cambiar.resize(650, 420)
        Cambiar.setMinimumSize(QtCore.QSize(650, 420))
        Cambiar.setMaximumSize(QtCore.QSize(650, 420))
        self.lblModificar = QtGui.QLabel(Cambiar)
        self.lblModificar.setGeometry(QtCore.QRect(160, 60, 361, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblModificar.setFont(font)
        self.lblModificar.setMouseTracking(True)
        self.lblModificar.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.lblModificar.setObjectName(_fromUtf8("lblModificar"))
        self.lblBazarPapeleriaLulita = QtGui.QLabel(Cambiar)
        self.lblBazarPapeleriaLulita.setGeometry(QtCore.QRect(210, 0, 251, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblBazarPapeleriaLulita.setFont(font)
        self.lblBazarPapeleriaLulita.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblBazarPapeleriaLulita.setObjectName(_fromUtf8("lblBazarPapeleriaLulita"))
        self.lblDireccion = QtGui.QLabel(Cambiar)
        self.lblDireccion.setGeometry(QtCore.QRect(110, 20, 431, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblDireccion.setObjectName(_fromUtf8("lblDireccion"))
        self.tbVwActualizarProducto = QtGui.QTableWidget(Cambiar)
        self.tbVwActualizarProducto.setGeometry(QtCore.QRect(10, 135, 620, 230))
        self.tbVwActualizarProducto.setObjectName(_fromUtf8("tbVwActualizarProducto"))
        self.tbVwActualizarProducto.setColumnCount(0)
        self.tbVwActualizarProducto.setRowCount(0)
        self.cbxBuscar = QtGui.QComboBox(Cambiar)
        self.cbxBuscar.setGeometry(QtCore.QRect(80, 90, 481, 25))
        self.cbxBuscar.setObjectName(_fromUtf8("cbxBuscar"))
        self.btnGuardar = QtGui.QPushButton(Cambiar)
        self.btnGuardar.setGeometry(QtCore.QRect(330, 380, 200, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnGuardar.setFont(font)
        self.btnGuardar.setMouseTracking(True)
        self.btnGuardar.setStyleSheet(_fromUtf8("Color:rgb(1, 137, 125);"))
        self.btnGuardar.setObjectName(_fromUtf8("btnGuardar"))
        self.btnRegresar = QtGui.QPushButton(Cambiar)
        self.btnRegresar.setGeometry(QtCore.QRect(120, 380, 200, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegresar.setFont(font)
        self.btnRegresar.setMouseTracking(True)
        self.btnRegresar.setStyleSheet(_fromUtf8("Color:rgb(223, 15, 90);"))
        self.btnRegresar.setObjectName(_fromUtf8("btnRegresar"))

        self.retranslateUi(Cambiar)
        QtCore.QMetaObject.connectSlotsByName(Cambiar)

    def retranslateUi(self, Cambiar):
        Cambiar.setWindowTitle(_translate("Cambiar", "Actualizar Producto", None))
        self.lblModificar.setToolTip(_translate("Cambiar", "Cambiar", None))
        self.lblModificar.setText(_translate("Cambiar", "Actualizar Producto del Bazar o Papeleria", None))
        self.lblBazarPapeleriaLulita.setText(_translate("Cambiar", "BAZAR Y PAPELERIA LULITA", None))
        self.lblDireccion.setText(_translate("Cambiar", "Km 8 1/2 via Daule - Cdla. \"La Gaviota\" Mz. 2262 V. 7", None))
        self.cbxBuscar.setToolTip(_translate("Cambiar", "<html><head/><body><p><span style=\" color:#ffffff;\"> Buscar producto</span></p></body></html>", None))
        self.btnGuardar.setToolTip(_translate("Cambiar", "<html><head/><body><p><span style=\" color:#ffffff;\">GUARDAR</span></p></body></html>", None))
        self.btnGuardar.setText(_translate("Cambiar", "GUARDAR", None))
        self.btnRegresar.setToolTip(_translate("Cambiar", "<html><head/><body><p><span style=\" color:#ffffff;\">REGRESAR</span></p></body></html>", None))
        self.btnRegresar.setText(_translate("Cambiar", "REGRESAR", None))

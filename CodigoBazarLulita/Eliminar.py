# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eliminar.ui'
#
# Created: Sun Mar 15 12:23:58 2015
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

class Ui_Eliminar(object):
    def setupUi(self, Eliminar):
        Eliminar.setObjectName(_fromUtf8("Eliminar"))
        Eliminar.resize(450, 370)
        Eliminar.setMaximumSize(QtCore.QSize(450, 370))
        self.tblVwEliminar = QtGui.QTableView(Eliminar)
        self.tblVwEliminar.setGeometry(QtCore.QRect(10, 145, 421, 171))
        self.tblVwEliminar.setMouseTracking(True)
        self.tblVwEliminar.setObjectName(_fromUtf8("tblVwEliminar"))
        self.btnEliminar = QtGui.QPushButton(Eliminar)
        self.btnEliminar.setGeometry(QtCore.QRect(230, 330, 200, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnEliminar.setFont(font)
        self.btnEliminar.setMouseTracking(True)
        self.btnEliminar.setStyleSheet(_fromUtf8("Color:rgb(1, 137, 125);"))
        self.btnEliminar.setObjectName(_fromUtf8("btnEliminar"))
        self.lblEliminar = QtGui.QLabel(Eliminar)
        self.lblEliminar.setGeometry(QtCore.QRect(40, 60, 371, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblEliminar.setFont(font)
        self.lblEliminar.setMouseTracking(True)
        self.lblEliminar.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.lblEliminar.setObjectName(_fromUtf8("lblEliminar"))
        self.lblBazarPapeleriaLulita = QtGui.QLabel(Eliminar)
        self.lblBazarPapeleriaLulita.setGeometry(QtCore.QRect(110, 0, 240, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblBazarPapeleriaLulita.setFont(font)
        self.lblBazarPapeleriaLulita.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblBazarPapeleriaLulita.setObjectName(_fromUtf8("lblBazarPapeleriaLulita"))
        self.lblDireccion = QtGui.QLabel(Eliminar)
        self.lblDireccion.setGeometry(QtCore.QRect(10, 20, 420, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblDireccion.setObjectName(_fromUtf8("lblDireccion"))
        self.btnBuscar = QtGui.QCommandLinkButton(Eliminar)
        self.btnBuscar.setGeometry(QtCore.QRect(360, 90, 70, 35))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBuscar.sizePolicy().hasHeightForWidth())
        self.btnBuscar.setSizePolicy(sizePolicy)
        self.btnBuscar.setMouseTracking(True)
        self.btnBuscar.setAutoFillBackground(False)
        self.btnBuscar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/buscar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon)
        self.btnBuscar.setIconSize(QtCore.QSize(70, 40))
        self.btnBuscar.setCheckable(True)
        self.btnBuscar.setAutoExclusive(False)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.btnRegresar = QtGui.QPushButton(Eliminar)
        self.btnRegresar.setGeometry(QtCore.QRect(20, 330, 200, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegresar.setFont(font)
        self.btnRegresar.setMouseTracking(True)
        self.btnRegresar.setStyleSheet(_fromUtf8("Color:rgb(223, 15, 90);"))
        self.btnRegresar.setObjectName(_fromUtf8("btnRegresar"))
        self.txtBuscar = QtGui.QLineEdit(Eliminar)
        self.txtBuscar.setGeometry(QtCore.QRect(10, 100, 351, 25))
        self.txtBuscar.setAutoFillBackground(True)
        self.txtBuscar.setObjectName(_fromUtf8("txtBuscar"))

        self.retranslateUi(Eliminar)
        QtCore.QMetaObject.connectSlotsByName(Eliminar)

    def retranslateUi(self, Eliminar):
        Eliminar.setWindowTitle(_translate("Eliminar", "Eliminar Producto", None))
        self.tblVwEliminar.setToolTip(_translate("Eliminar", "<html><head/><body><p><span style=\" color:#ffffff;\">Detalle</span></p></body></html>", None))
        self.btnEliminar.setToolTip(_translate("Eliminar", "<html><head/><body><p><span style=\" color:#ffffff;\">ELIMINAR</span></p></body></html>", None))
        self.btnEliminar.setText(_translate("Eliminar", "ELIMINAR", None))
        self.lblEliminar.setToolTip(_translate("Eliminar", "Eliminar producto", None))
        self.lblEliminar.setText(_translate("Eliminar", "Eliminar producto del Bazar o Papeleria", None))
        self.lblBazarPapeleriaLulita.setText(_translate("Eliminar", "BAZAR Y PAPELERIA LULITA", None))
        self.lblDireccion.setText(_translate("Eliminar", "Km 8 1/2 via Daule - Cdla. \"La Gaviota\" Mz. 2262 V. 7", None))
        self.btnBuscar.setToolTip(_translate("Eliminar", "<html><head/><body><p><span style=\" color:#ffffff;\">Ingresar producto</span></p></body></html>", None))
        self.btnRegresar.setToolTip(_translate("Eliminar", "<html><head/><body><p><span style=\" color:#ffffff;\">REGRESAR</span></p></body></html>", None))
        self.btnRegresar.setText(_translate("Eliminar", "REGRESAR", None))
        self.txtBuscar.setToolTip(_translate("Eliminar", "<html><head/><body><p><span style=\" color:#ffffff;\">Buscar producto</span></p></body></html>", None))
        self.txtBuscar.setPlaceholderText(_translate("Eliminar", "Buscar producto del Bazar y Papeleria ", None))


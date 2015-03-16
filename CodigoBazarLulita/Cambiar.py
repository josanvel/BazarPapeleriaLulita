# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cambiar.ui'
#
# Created: Sun Mar 15 12:23:33 2015
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
        Cambiar.resize(450, 370)
        Cambiar.setMaximumSize(QtCore.QSize(450, 370))
        self.tblVwModificar = QtGui.QTableView(Cambiar)
        self.tblVwModificar.setGeometry(QtCore.QRect(10, 145, 421, 171))
        self.tblVwModificar.setMouseTracking(True)
        self.tblVwModificar.setObjectName(_fromUtf8("tblVwModificar"))
        self.btnImprimir = QtGui.QPushButton(Cambiar)
        self.btnImprimir.setGeometry(QtCore.QRect(230, 330, 200, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnImprimir.setFont(font)
        self.btnImprimir.setMouseTracking(True)
        self.btnImprimir.setStyleSheet(_fromUtf8("Color:rgb(1, 137, 125);"))
        self.btnImprimir.setObjectName(_fromUtf8("btnImprimir"))
        self.lblModificar = QtGui.QLabel(Cambiar)
        self.lblModificar.setGeometry(QtCore.QRect(30, 50, 391, 20))
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
        self.lblBazarPapeleriaLulita.setGeometry(QtCore.QRect(110, 0, 240, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblBazarPapeleriaLulita.setFont(font)
        self.lblBazarPapeleriaLulita.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblBazarPapeleriaLulita.setObjectName(_fromUtf8("lblBazarPapeleriaLulita"))
        self.lblDireccion = QtGui.QLabel(Cambiar)
        self.lblDireccion.setGeometry(QtCore.QRect(10, 20, 420, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblDireccion.setObjectName(_fromUtf8("lblDireccion"))
        self.btnBuscar = QtGui.QCommandLinkButton(Cambiar)
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
        self.btnRegresar = QtGui.QPushButton(Cambiar)
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
        self.txtBuscar = QtGui.QLineEdit(Cambiar)
        self.txtBuscar.setGeometry(QtCore.QRect(10, 100, 351, 25))
        self.txtBuscar.setAutoFillBackground(True)
        self.txtBuscar.setObjectName(_fromUtf8("txtBuscar"))

        self.retranslateUi(Cambiar)
        QtCore.QMetaObject.connectSlotsByName(Cambiar)

    def retranslateUi(self, Cambiar):
        Cambiar.setWindowTitle(_translate("Cambiar", "Cambiar Precio Producto", None))
        self.tblVwModificar.setToolTip(_translate("Cambiar", "<html><head/><body><p><span style=\" color:#ffffff;\">Detalle</span></p></body></html>", None))
        self.btnImprimir.setToolTip(_translate("Cambiar", "<html><head/><body><p><span style=\" color:#ffffff;\">IMPRIMIR</span></p></body></html>", None))
        self.btnImprimir.setText(_translate("Cambiar", "GUARDAR", None))
        self.lblModificar.setToolTip(_translate("Cambiar", "Cambiar", None))
        self.lblModificar.setText(_translate("Cambiar", "Cambiar precio producto del Bazar o Papeleria", None))
        self.lblBazarPapeleriaLulita.setText(_translate("Cambiar", "BAZAR Y PAPELERIA LULITA", None))
        self.lblDireccion.setText(_translate("Cambiar", "Km 8 1/2 via Daule - Cdla. \"La Gaviota\" Mz. 2262 V. 7", None))
        self.btnBuscar.setToolTip(_translate("Cambiar", "<html><head/><body><p><span style=\" color:#ffffff;\">Ingresar producto</span></p></body></html>", None))
        self.btnRegresar.setToolTip(_translate("Cambiar", "<html><head/><body><p><span style=\" color:#ffffff;\">REGRESAR</span></p></body></html>", None))
        self.btnRegresar.setText(_translate("Cambiar", "REGRESAR", None))
        self.txtBuscar.setToolTip(_translate("Cambiar", "<html><head/><body><p><span style=\" color:#ffffff;\">Buscar producto</span></p></body></html>", None))
        self.txtBuscar.setPlaceholderText(_translate("Cambiar", "Buscar producto del Bazar y Papeleria ", None))



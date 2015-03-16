# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'modificar.ui'
#
# Created: Sun Mar 15 12:31:41 2015
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

class Ui_Modificar(object):
    def setupUi(self, Modificar):
        Modificar.setObjectName(_fromUtf8("Modificar"))
        Modificar.resize(450, 370)
        Modificar.setMaximumSize(QtCore.QSize(450, 370))
        self.txtBuscar = QtGui.QLineEdit(Modificar)
        self.txtBuscar.setGeometry(QtCore.QRect(10, 100, 351, 25))
        self.txtBuscar.setAutoFillBackground(True)
        self.txtBuscar.setObjectName(_fromUtf8("txtBuscar"))
        self.lblDireccion = QtGui.QLabel(Modificar)
        self.lblDireccion.setGeometry(QtCore.QRect(15, 20, 420, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblDireccion.setObjectName(_fromUtf8("lblDireccion"))
        self.btnGuadar = QtGui.QPushButton(Modificar)
        self.btnGuadar.setGeometry(QtCore.QRect(230, 330, 200, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnGuadar.setFont(font)
        self.btnGuadar.setMouseTracking(True)
        self.btnGuadar.setStyleSheet(_fromUtf8("Color:rgb(1, 137, 125);"))
        self.btnGuadar.setObjectName(_fromUtf8("btnGuadar"))
        self.btnRegresar = QtGui.QPushButton(Modificar)
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
        self.btnBuscar = QtGui.QCommandLinkButton(Modificar)
        self.btnBuscar.setGeometry(QtCore.QRect(360, 90, 70, 35))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBuscar.sizePolicy().hasHeightForWidth())
        self.btnBuscar.setSizePolicy(sizePolicy)
        self.btnBuscar.setAutoFillBackground(False)
        self.btnBuscar.setText(_fromUtf8(""))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/iconos/buscar.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnBuscar.setIcon(icon)
        self.btnBuscar.setIconSize(QtCore.QSize(70, 40))
        self.btnBuscar.setCheckable(True)
        self.btnBuscar.setAutoExclusive(False)
        self.btnBuscar.setObjectName(_fromUtf8("btnBuscar"))
        self.lblBazarPapeleriaLulita = QtGui.QLabel(Modificar)
        self.lblBazarPapeleriaLulita.setGeometry(QtCore.QRect(105, 0, 240, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblBazarPapeleriaLulita.setFont(font)
        self.lblBazarPapeleriaLulita.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblBazarPapeleriaLulita.setObjectName(_fromUtf8("lblBazarPapeleriaLulita"))
        self.lblModificar = QtGui.QLabel(Modificar)
        self.lblModificar.setGeometry(QtCore.QRect(35, 50, 391, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lblModificar.setFont(font)
        self.lblModificar.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.lblModificar.setObjectName(_fromUtf8("lblModificar"))
        self.tblVwModificar = QtGui.QTableView(Modificar)
        self.tblVwModificar.setGeometry(QtCore.QRect(10, 145, 421, 171))
        self.tblVwModificar.setObjectName(_fromUtf8("tblVwModificar"))

        self.retranslateUi(Modificar)
        QtCore.QMetaObject.connectSlotsByName(Modificar)

    def retranslateUi(self, Modificar):
        Modificar.setWindowTitle(_translate("Modificar", "Modificar Cantidad Producto", None))
        self.txtBuscar.setToolTip(_translate("Modificar", "<html><head/><body><p><span style=\" color:#ffffff;\">Buscar producto</span></p></body></html>", None))
        self.txtBuscar.setPlaceholderText(_translate("Modificar", "Buscar producto del Bazar y Papeleria ", None))
        self.lblDireccion.setText(_translate("Modificar", "Km 8 1/2 via Daule - Cdla. \"La Gaviota\" Mz. 2262 V. 7", None))
        self.btnGuadar.setToolTip(_translate("Modificar", "<html><head/><body><p><span style=\" color:#ffffff;\">GUARDAR</span></p></body></html>", None))
        self.btnGuadar.setText(_translate("Modificar", "GUARDAR", None))
        self.btnRegresar.setToolTip(_translate("Modificar", "<html><head/><body><p><span style=\" color:#ffffff;\">REGRESAR</span></p></body></html>", None))
        self.btnRegresar.setText(_translate("Modificar", "REGRESAR", None))
        self.btnBuscar.setToolTip(_translate("Modificar", "<html><head/><body><p><span style=\" color:#ffffff;\">Ingresar producto</span></p></body></html>", None))
        self.lblBazarPapeleriaLulita.setText(_translate("Modificar", "BAZAR Y PAPELERIA LULITA", None))
        self.lblModificar.setText(_translate("Modificar", "Modificar cantidad producto del Bazar y Papeleria", None))
        self.tblVwModificar.setToolTip(_translate("Modificar", "<html><head/><body><p><span style=\" color:#ffffff;\">Detalle</span></p></body></html>", None))



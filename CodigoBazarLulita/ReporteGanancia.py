# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reporteganancia.ui'
#
# Created: Sun Mar 15 12:32:12 2015
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

class Ui_ReporteGanancia(object):
    def setupUi(self, ReporteGanancia):
        ReporteGanancia.setObjectName(_fromUtf8("ReporteGanancia"))
        ReporteGanancia.resize(500, 140)
        ReporteGanancia.setMaximumSize(QtCore.QSize(500, 140))
        self.lblModificar = QtGui.QLabel(ReporteGanancia)
        self.lblModificar.setGeometry(QtCore.QRect(170, 40, 161, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblModificar.setFont(font)
        self.lblModificar.setStyleSheet(_fromUtf8("Color:rgb(243, 157, 0);"))
        self.lblModificar.setObjectName(_fromUtf8("lblModificar"))
        self.lblBazarPapeleriaLulita = QtGui.QLabel(ReporteGanancia)
        self.lblBazarPapeleriaLulita.setGeometry(QtCore.QRect(130, 0, 240, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblBazarPapeleriaLulita.setFont(font)
        self.lblBazarPapeleriaLulita.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblBazarPapeleriaLulita.setObjectName(_fromUtf8("lblBazarPapeleriaLulita"))
        self.lblDireccion = QtGui.QLabel(ReporteGanancia)
        self.lblDireccion.setGeometry(QtCore.QRect(40, 20, 420, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.lblDireccion.setFont(font)
        self.lblDireccion.setStyleSheet(_fromUtf8("Color:rgb(51, 102, 255);"))
        self.lblDireccion.setObjectName(_fromUtf8("lblDireccion"))
        self.btnGenerar = QtGui.QPushButton(ReporteGanancia)
        self.btnGenerar.setGeometry(QtCore.QRect(250, 110, 200, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnGenerar.setFont(font)
        self.btnGenerar.setStyleSheet(_fromUtf8("Color:rgb(1, 137, 125);"))
        self.btnGenerar.setObjectName(_fromUtf8("btnGenerar"))
        self.btnRegresar = QtGui.QPushButton(ReporteGanancia)
        self.btnRegresar.setGeometry(QtCore.QRect(40, 110, 200, 25))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.btnRegresar.setFont(font)
        self.btnRegresar.setStyleSheet(_fromUtf8("Color:rgb(223, 15, 90);"))
        self.btnRegresar.setObjectName(_fromUtf8("btnRegresar"))
        self.dteFechaFinal = QtGui.QDateTimeEdit(ReporteGanancia)
        self.dteFechaFinal.setGeometry(QtCore.QRect(250, 70, 200, 27))
        self.dteFechaFinal.setObjectName(_fromUtf8("dteFechaFinal"))
        self.dteFechaInicial = QtGui.QDateTimeEdit(ReporteGanancia)
        self.dteFechaInicial.setGeometry(QtCore.QRect(40, 70, 200, 27))
        self.dteFechaInicial.setMouseTracking(True)
        self.dteFechaInicial.setObjectName(_fromUtf8("dteFechaInicial"))

        self.retranslateUi(ReporteGanancia)
        QtCore.QMetaObject.connectSlotsByName(ReporteGanancia)

    def retranslateUi(self, ReporteGanancia):
        ReporteGanancia.setWindowTitle(_translate("ReporteGanancia", "Reporte Ganancia", None))
        self.lblModificar.setText(_translate("ReporteGanancia", "Reportes Ganancias", None))
        self.lblBazarPapeleriaLulita.setText(_translate("ReporteGanancia", "BAZAR Y PAPELERIA LULITA", None))
        self.lblDireccion.setText(_translate("ReporteGanancia", "Km 8 1/2 via Daule - Cdla. \"La Gaviota\" Mz. 2262 V. 7", None))
        self.btnGenerar.setToolTip(_translate("ReporteGanancia", "<html><head/><body><p><span style=\" color:#ffffff;\">GENERAR</span></p></body></html>", None))
        self.btnGenerar.setText(_translate("ReporteGanancia", "GENERAR", None))
        self.btnRegresar.setToolTip(_translate("ReporteGanancia", "<html><head/><body><p><span style=\" color:#ffffff;\">REGRESAR</span></p></body></html>", None))
        self.btnRegresar.setText(_translate("ReporteGanancia", "REGRESAR", None))
        self.dteFechaFinal.setToolTip(_translate("ReporteGanancia", "Fecha Final", None))
        self.dteFechaInicial.setToolTip(_translate("ReporteGanancia", "Fecha Inicial", None))


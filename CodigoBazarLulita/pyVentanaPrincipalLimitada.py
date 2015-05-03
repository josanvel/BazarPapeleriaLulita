'''
Created on 20/04/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui, QtSql

from VentanaPrincipalLimitada import Ui_VentanaPrincipalLimitada
from pyFacturacion import MyformFacturacion
from pyBotonesReportes import MyformBotonesReportes
from pyCambiar import MyformCambiar

class MyformVentanaPrincipalLimitada(QtGui.QMainWindow):
	def __init__(self, parent=None):
		 QtGui.QWidget.__init__(self, parent)
		 self.uiVentanaPrincipalLimitada = Ui_VentanaPrincipalLimitada()
		 self.uiVentanaPrincipalLimitada.setupUi(self)
		 self.center()

		 self.connect(self.uiVentanaPrincipalLimitada.btnFacturacion, QtCore.SIGNAL("clicked()"), self.entrarFacturacion)
		 self.connect(self.uiVentanaPrincipalLimitada.btnReportes, QtCore.SIGNAL("clicked()"), self.entrarReporte)
		 self.connect(self.uiVentanaPrincipalLimitada.btnActualizar, QtCore.SIGNAL("clicked()"), self.entrarActualizar)

	def entrarFacturacion(self):
		self.hide()
		self.facturacion = MyformFacturacion()
		self.facturacion.regresarVentanaR(self)
		self.facturacion.show()

	def entrarReporte(self):
		self.hide()
		self.reporte = MyformBotonesReportes()
		self.reporte.regresarVentanaR(self)
		self.reporte.show()

	def entrarActualizar(self):
		self.hide()
		self.actualizar = MyformCambiar()
		self.actualizar.regresarVentanaR(self)
		self.actualizar.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def obtenerUsuarioContrasena(self, usuario, contrasena):
		self.user = usuario
		self.password = contrasena
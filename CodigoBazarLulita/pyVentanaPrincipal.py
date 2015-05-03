'''
Created on 20/04/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui, QtSql

from VentanaPrincipal import Ui_VentanaPrincipal
from pyAgregar import MyformAgregar
from pyFacturacion import MyformFacturacion
from pyBotonesReportes import MyformBotonesReportes
from pyCambiar import MyformCambiar
from pyBotonesCuenta import MyformBotonesCuenta

class pyVentanaP(QtGui.QMainWindow):
	def __init__(self, parent=None):
		 QtGui.QWidget.__init__(self, parent)
		 self.ui = Ui_VentanaPrincipal()
		 self.ui.setupUi(self)
		 self.center()

		 self.connect(self.ui.btnAgregar, QtCore.SIGNAL("clicked()"), self.entrarAgregar)
		 self.connect(self.ui.btnFacturacion, QtCore.SIGNAL("clicked()"), self.entrarFacturacion)
		 self.connect(self.ui.btnReportes, QtCore.SIGNAL("clicked()"), self.entrarReporte)
		 self.connect(self.ui.btnActualizar, QtCore.SIGNAL("clicked()"), self.entrarActualizar)
		 self.connect(self.ui.btnCuentas, QtCore.SIGNAL("clicked()"), self.entrarCuentas)

	def entrarAgregar(self):
		self.hide()
		self.agregar = MyformAgregar()
		self.agregar.regresarVentanaR(self)
		self.agregar.show()

	def entrarFacturacion(self):
		self.hide()
		self.facturacion = MyformFacturacion()
		self.facturacion.regresarVentanaR(self)
		self.facturacion.obtenerUsuario(self.user)
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

	def entrarCuentas(self):
		self.hide()
		self.cuentas = MyformBotonesCuenta()
		self.cuentas.regresarVentanaR(self)
		self.cuentas.obtenerUsuarioContrasena(self.user, self.password)
		self.cuentas.show()

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def obtenerUsuarioContrasena(self, usuario, contrasena):
		self.user = usuario
		self.password = contrasena
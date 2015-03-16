'''
Created on 27/07/2013

@author: josanvel
'''

from PyQt4 import QtCore, QtGui, QtSql

from VentanaPrincipal import Ui_VentanaPrincipal
from pyAgregar import MyformAgregar
from pyFacturacion import MyformFacturacion
from pyBotonesReportes import MyformBotonesReportes
from pyBotonesActualizar import MyformBotonesActualizar
from pyEliminar import MyformEliminar

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
		 self.connect(self.ui.btnEliminar, QtCore.SIGNAL("clicked()"), self.entrarEliminar)

	def entrarAgregar(self):
		self.hide()
		self.agregar = MyformAgregar()
		self.agregar.regresarVentanaR(self)
		self.agregar.show()

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
		self.actualizar = MyformBotonesActualizar()
		self.actualizar.regresarVentanaR(self)
		self.actualizar.show()

	def entrarEliminar(self):
		self.hide()
		self.eliminar = MyformEliminar()
		self.eliminar.regresarVentanaR(self)
		self.eliminar.show()

	def IniciarBase(self):
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setUserName("root");
        self.db.setPassword("");
        self.db.setHostName("127.0.0.1");
        self.db.setDatabaseName("BazarPapeleriaLulita")
        self.db.open()
        
	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
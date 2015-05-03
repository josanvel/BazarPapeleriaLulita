'''
Created on 20/04/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui, QtSql
from CrearCuenta import Ui_crearCuenta

class MyformCrearCuenta(QtGui.QMainWindow):
	def __init__(self, parent=None):
		 QtGui.QWidget.__init__(self, parent)
		 self.uiCrearCuenta = Ui_crearCuenta()
		 self.uiCrearCuenta.setupUi(self)
		 self.center()

		 self.uiCrearCuenta.cbxTipoCuenta.addItem('Administrador')
		 self.uiCrearCuenta.cbxTipoCuenta.addItem('Usuario')

		 self.connect(self.uiCrearCuenta.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarCrearCuenta)
		 self.connect(self.uiCrearCuenta.btnCrearCuenta, QtCore.SIGNAL("clicked()"), self.crearCuenta)
		 self.uiCrearCuenta.txtPasw.returnPressed.connect(self.uiCrearCuenta.btnCrearCuenta.click)

	def regresarVentanaR(self,ventanaAtras):
		self.ventana = ventanaAtras

	def regresarCrearCuenta(self):
		reply = QtGui.QMessageBox.question(self, 'CREAR CUENTA', "Se perdera informacion ingresada", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
		if reply == QtGui.QMessageBox.Yes:
			self.hide()
			self.ventana.show()

	def crearCuenta(self):
		tipoCuenta = self.uiCrearCuenta.cbxTipoCuenta.currentText()
		usuario = self.uiCrearCuenta.txtUser.displayText()
		contrasena = self.uiCrearCuenta.txtPasw.displayText()
		if tipoCuenta == 'Administrador':
			tipo = 1
		else:
			tipo = 2

		if not QtSql.QSqlDatabase.database().isOpen():
			if not QtSql.QSqlDatabase.database():
				QtGui.QMessageBox.information(None, 'BASES DE DATOS', 'No se pudo abrir la BASES DE DATOS') 

		query = QtSql.QSqlQuery()
		query.prepare("call PRInsertCuenta(?,?,?)")

		query.addBindValue(usuario)
		query.addBindValue(contrasena)
		query.addBindValue(tipo)

		if not query.exec_():
			QtGui.QMessageBox.warning( None, "CREAR CUENTA",\
				"No se pudo CREAR la Cuenta, el Usuario ya existe" )
			self.uiCrearCuenta.txtUser.setText("")
			self.uiCrearCuenta.txtPasw.setText("")
		else:
			QtGui.QMessageBox.information(None, "CREAR CUENTA","Se creo una nueva Cuenta") 
			self.regresarCrearCuenta()

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())
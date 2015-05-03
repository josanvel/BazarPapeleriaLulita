'''
Created on 20/04/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui, QtSql
from CambiarContrasena import Ui_cambiarContrasena

class MyformCambiarContrasena(QtGui.QMainWindow):
	def __init__(self, parent=None):
		 QtGui.QWidget.__init__(self, parent)
		 self.uiCambiarContrasena = Ui_cambiarContrasena()
		 self.uiCambiarContrasena.setupUi(self)
		 self.center()
		 self.ocultarContrasena()

		 self.connect(self.uiCambiarContrasena.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarCambiarContrasena)
		 self.connect(self.uiCambiarContrasena.btnCambiarContrasena, QtCore.SIGNAL("clicked()"), self.cambiarContrasena)
		 self.uiCambiarContrasena.txtPasswVerificar.returnPressed.connect(self.uiCambiarContrasena.btnCambiarContrasena.click)

	def ocultarContrasena(self):
		self.uiCambiarContrasena.txtPassw.setEchoMode(QtGui.QLineEdit.Password)
		self.uiCambiarContrasena.txtPasswNueva.setEchoMode(QtGui.QLineEdit.Password)
		self.uiCambiarContrasena.txtPasswVerificar.setEchoMode(QtGui.QLineEdit.Password)

	def regresarVentanaR(self,ventanaAtras):
		self.ventana = ventanaAtras

	def regresarCambiarContrasena(self):
		reply = QtGui.QMessageBox.question(self, 'CAMBIAR CONTRASENA', "Se perdera informacion ingresada", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
		if reply == QtGui.QMessageBox.Yes:
			self.hide()
			self.ventana.show()

	def cambiarContrasena(self):
		usuario = self.uiCambiarContrasena.txtUser.text()
		contrasena = self.uiCambiarContrasena.txtPassw.text()
		contNueva = self.uiCambiarContrasena.txtPasswNueva.text()
		verificarCont = self.uiCambiarContrasena.txtPasswVerificar.text()	

		if not QtSql.QSqlDatabase.database().isOpen():
			if not QtSql.QSqlDatabase.database():
				QtGui.QMessageBox.warning( None, "BASES DE DATOS",\
                                          "No se pudo abrir la BASES DE DATOS" ) 

		query = QtSql.QSqlQuery("call PRQueryBuscarCuenta('"+usuario+"','"+contrasena+"')")
		count = 0

		while query.next():
			count = count + 1

		if count == 1:
			if contNueva == verificarCont:
				if not QtSql.QSqlDatabase.database().isOpen():
					if not QtSql.QSqlDatabase.database():
						QtGui.QMessageBox.information(None, 'BASES DE DATOS', 'No se pudo abrir la BASES DE DATOS') 

				query = QtSql.QSqlQuery()
				query.prepare("call PRUpdateCuenta(?,?)")
				query.addBindValue(usuario)
				query.addBindValue(contNueva)

				if not query.exec_():
					QtGui.QMessageBox.warning( None, "CAMBIAR CONTRASENA",\
						"No se pudo cambiar la Contrasena" )
					self.uiCambiarContrasena.txtPassw.setText("")
				else:
					message = QtGui.QMessageBox.information(None, "CAMBIAR CONTRASENA","Se cambio la contrasena")
					self.uiCambiarContrasena.txtPassw.setText("")
					self.uiCambiarContrasena.txtPasswNueva.setText("")
					self.uiCambiarContrasena.txtPasswVerificar
					self.regresarCambiarContrasena()
			else:
				QtGui.QMessageBox.warning( None, "CAMBIAR CONTRASENA",\
                                          "Las contrasenas no coinciden" )
				self.uiCambiarContrasena.txtPasswNueva.setText("")
				self.uiCambiarContrasena.txtPasswVerificar.setText("")

		else:
			QtGui.QMessageBox.warning( None, "CAMBIAR CONTRASENA",\
                                          "No se pudo cambiar la contrasena, credenciales incorrectas" )
			self.uiCambiarContrasena.txtPassw.setText("")

	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def obtenerUsuarioContrasena(self, usuario, contrasena):
		self.user = usuario
		self.password = contrasena
		self.uiCambiarContrasena.txtUser.setText(''+self.user)
		self.uiCambiarContrasena.txtUser.setEnabled(False)
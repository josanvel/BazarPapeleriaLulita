'''
Created on 20/04/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui, QtSql

from Login import Ui_Login
from pyVentanaPrincipal import pyVentanaP
from pyVentanaPrincipalLimitada import MyformVentanaPrincipalLimitada

class pyLoginP(QtGui.QMainWindow):
	def __init__(self, parent=None):
		 QtGui.QWidget.__init__(self, parent)
		 self.uiLogin = Ui_Login()
		 self.uiLogin.setupUi(self)
		 self.IniciarBase()
		 self.center()

		 self.uiLogin.txtPassw.setEchoMode(QtGui.QLineEdit.Password)
		 self.connect(self.uiLogin.btnEntrar, QtCore.SIGNAL("clicked()"), self.entrar)
		 self.uiLogin.txtPassw.returnPressed.connect(self.uiLogin.btnEntrar.click)

	def entrar(self):
		usuario = self.uiLogin.txtUser.text()
		contrasena = self.uiLogin.txtPassw.text()

		if not QtSql.QSqlDatabase.database().isOpen():
			if not QtSql.QSqlDatabase.database():
				QtGui.QMessageBox.warning( None, "BASES DE DATOS",\
                                          "No se pudo abrir la BASES DE DATOS" ) 

		query = QtSql.QSqlQuery("call PRQueryBuscarCuenta('"+usuario+"','"+contrasena+"')")
		count = 0

		while query.next():
			count = count + 1
			self.user = query.value(1).toString()
			self.password = query.value(2).toString()
			self.tipo = query.value(3).toInt()

		if count == 1:
			self.hide()
			if self.tipo[0] == 1:
				self.entrarPrincipal = pyVentanaP(self)
			else:
				self.entrarPrincipal = MyformVentanaPrincipalLimitada(self)
			self.entrarPrincipal.obtenerUsuarioContrasena(self.user, self.password)
			self.entrarPrincipal.show()
		else:
			self.uiLogin.txtPassw.setText("")
			QtGui.QMessageBox.warning( None, "LOGIN",\
                                          "Datos ingresados incorrectos" ) 
			self.uiLogin.txtUser.setText("")

	def IniciarBase(self):
		self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
		self.db.setUserName("root")
		self.db.setPassword("")
		self.db.setHostName("127.0.0.1")
		self.db.setDatabaseName("BazarPapeleriaLulita")
		self.db.open()
        
	def center(self):
		qr = self.frameGeometry()
		cp = QtGui.QDesktopWidget().availableGeometry().center()
		qr.moveCenter(cp)
		self.move(qr.topLeft())

	def toInt(self,num):
		try:
			return int(num)
		except exceptions.ValueError:
			return None
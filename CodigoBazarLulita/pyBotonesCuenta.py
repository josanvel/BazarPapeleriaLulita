'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from BotonesCuenta import Ui_BotonesCuenta
from pyCrearCuenta import MyformCrearCuenta
from pyCambiarContrasena import MyformCambiarContrasena

class MyformBotonesCuenta(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiBotonesCuenta = Ui_BotonesCuenta()
                self.uiBotonesCuenta.setupUi(self)
                self.center()

                self.connect(self.uiBotonesCuenta.btnRegresarCuenta, QtCore.SIGNAL("clicked()"), self.regresarCuenta)
                self.connect(self.uiBotonesCuenta.btnCambiarContrasena, QtCore.SIGNAL("clicked()"), self.entrarCambiarContrasena)
                self.connect(self.uiBotonesCuenta.btnCrearCuenta, QtCore.SIGNAL("clicked()"), self.entrarCrearCuenta)

        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarCuenta(self):
                self.hide()
                self.ventana.show()

        def entrarCambiarContrasena(self):
                self.hide()
                self.cambiarContrasena = MyformCambiarContrasena()
                self.cambiarContrasena.regresarVentanaR(self)
                self.cambiarContrasena.obtenerUsuarioContrasena(self.user, self.password)
                self.cambiarContrasena.show()
                
        def entrarCrearCuenta(self):
                self.hide()
                self.crearCuenta = MyformCrearCuenta()
                self.crearCuenta.regresarVentanaR(self)
                self.crearCuenta.show()

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())

        def obtenerUsuarioContrasena(self, usuario, contrasena):
                self.user = usuario
                self.password = contrasena
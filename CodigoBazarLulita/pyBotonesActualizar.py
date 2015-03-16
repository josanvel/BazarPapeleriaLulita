'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from BotonesActualizar import Ui_BotonesActualizar
from pyCambiar import MyformCambiar
from pyModificar import MyformModificar


class MyformBotonesActualizar(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiBotonesActualizar = Ui_BotonesActualizar()
                self.uiBotonesActualizar.setupUi(self)
                self.center()

                self.connect(self.uiBotonesActualizar.btnRegresarActualizar, QtCore.SIGNAL("clicked()"), self.regresarActualizar)
                self.connect(self.uiBotonesActualizar.btnActualizarCambiar, QtCore.SIGNAL("clicked()"), self.entrarActualizarCambiar)
                self.connect(self.uiBotonesActualizar.btnActualizarModificar, QtCore.SIGNAL("clicked()"), self.entrarActualizarModificar)



        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarActualizar(self):
                self.hide()
                self.ventana.show()


        def entrarActualizarCambiar(self):
                self.hide()
                self.actualizarCambiar = MyformCambiar()
                self.actualizarCambiar.regresarVentanaR(self)
                self.actualizarCambiar.show()

        def entrarActualizarModificar(self):
                self.hide()
                self.actualizarModificar = MyformModificar()
                self.actualizarModificar.regresarVentanaR(self)
                self.actualizarModificar.show()

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())
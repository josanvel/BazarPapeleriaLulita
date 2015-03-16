'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from Cambiar import Ui_Cambiar


class MyformCambiar(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiCambiar = Ui_Cambiar()
                self.uiCambiar.setupUi(self)
                self.center()

                self.connect(self.uiCambiar.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarCambiar)

        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarCambiar(self):
                self.hide()
                self.ventana.show()

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())
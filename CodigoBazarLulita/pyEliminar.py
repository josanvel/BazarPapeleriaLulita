'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from Eliminar import Ui_Eliminar


class MyformEliminar(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiEliminar= Ui_Eliminar()
                self.uiEliminar.setupUi(self)
                self.center()

                self.connect(self.uiEliminar.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarEliminar)

        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarEliminar(self):
                self.hide()
                self.ventana.show()

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())
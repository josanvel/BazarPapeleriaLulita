'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from Agregar import Ui_Agregar


class MyformAgregar(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiAgregar = Ui_Agregar()
                self.uiAgregar.setupUi(self)
                self.center()

                self.connect(self.uiAgregar.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarAgregar)


        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarAgregar(self):
                self.hide()
                self.ventana.show()

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())
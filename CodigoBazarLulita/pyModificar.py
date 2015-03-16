'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from Modificar import Ui_Modificar


class MyformModificar(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiModificar = Ui_Modificar()
                self.uiModificar.setupUi(self)
                self.center()

                self.connect(self.uiModificar.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarModificar)

        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarModificar(self):
                self.hide()
                self.ventana.show()

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())
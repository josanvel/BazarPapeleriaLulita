'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from Facturacion import Ui_Facturacion


class MyformFacturacion(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiFacturacion = Ui_Facturacion()
                self.uiFacturacion.setupUi(self)
                self.center()

                self.connect(self.uiFacturacion.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarFacturacion)

        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarFacturacion(self):
                self.hide()
                self.ventana.show()

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())
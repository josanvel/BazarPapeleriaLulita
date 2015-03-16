'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from ReporteProducto import Ui_ReporteProducto


class MyformReporteProductos(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiReporteProducto= Ui_ReporteProducto()
                self.uiReporteProducto.setupUi(self)
                self.center()

                self.connect(self.uiReporteProducto.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarReporteProductos)

        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarReporteProductos(self):
                self.hide()
                self.ventana.show()

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())
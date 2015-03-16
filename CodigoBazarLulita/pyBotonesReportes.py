'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from BotonesReportes import Ui_BotonesReportes
from pyReporteGanancia import MyformReporteGanancias
from pyReporteProducto import MyformReporteProductos


class MyformBotonesReportes(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiBotonesReportes= Ui_BotonesReportes()
                self.uiBotonesReportes.setupUi(self)
                self.center()

                self.connect(self.uiBotonesReportes.btnRegresarReportes, QtCore.SIGNAL("clicked()"), self.regresarReportes)
                self.connect(self.uiBotonesReportes.btnReporteGanancias, QtCore.SIGNAL("clicked()"), self.entrarReporteGanancias)
                self.connect(self.uiBotonesReportes.btnReporteProductos, QtCore.SIGNAL("clicked()"), self.entrarReporteProductos)

        


        def entrarReporteGanancias(self):
                self.hide()
                self.reporteGanancias = MyformReporteGanancias()
                self.reporteGanancias.regresarVentanaR(self)
                self.reporteGanancias.show()

        def entrarReporteProductos(self):
                self.hide()
                self.reporteProductos = MyformReporteProductos()
                self.reporteProductos.regresarVentanaR(self)
                self.reporteProductos.show()

        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarReportes(self):
                self.hide()
                self.ventana.show()

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())
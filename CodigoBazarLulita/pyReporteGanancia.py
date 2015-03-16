'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from ReporteGanancia import Ui_ReporteGanancia


class MyformReporteGanancias(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiReporteGanancia = Ui_ReporteGanancia()
                self.uiReporteGanancia.setupUi(self)
                self.center()

                self.connect(self.uiReporteGanancia.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarReporteGanancias)

        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarReporteGanancias(self):
                self.hide()
                self.ventana.show()

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())
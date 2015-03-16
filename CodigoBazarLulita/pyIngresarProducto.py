'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui
from IngresarProducto import Ui_IngresarProducto


class MyformIngresarProducto(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiIngresarProducto = Ui_IngresarProducto()
                self.uiIngresarProducto.setupUi(self)
                self.center()

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())
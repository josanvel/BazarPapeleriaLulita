'''
Created on 15/03/2015

@author: josanvel
'''
from PyQt4.QtGui import * 
from PyQt4.QtSql import * 
from PyQt4.QtCore import * 
from PyQt4 import QtCore, QtGui, QtSql
import exceptions
from IngresarProducto import Ui_IngresarProducto

class MyformIngresarProducto(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiIngresarProducto = Ui_IngresarProducto()
                self.uiIngresarProducto.setupUi(self)
                self.center()

                self.connect(self.uiIngresarProducto.btnCancelar, QtCore.SIGNAL("clicked()"), self.cancelarProducto)
                self.connect(self.uiIngresarProducto.btnAceptar, QtCore.SIGNAL("clicked()"), self.ingresarProducto)

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())

        def cancelarProducto(self):
                self.hide()

        def ingresarProducto(self):
                
                self.cantidad = int(self.uiIngresarProducto.spinBox.value())
                if self.cantidad > 0:
                        self.hide()
                        self.venta.getCantidadProducto(self.cantidad,self.idProducto)
                else:
                        QtGui.QMessageBox.warning( None, "INGRESAR PRODUCTO",\
                                          "Ingrese cantidad de producto" )
                
        def getProducto(self, indice, ventana):
                self.venta = ventana
                self.mostrarProducto(indice)

        def mostrarProducto(self, idP):
                query = QtSql.QSqlQuery("CALL PRQueryBuscarProductoID("+str(idP)+");")

                self.uiIngresarProducto.tblWProductoStock.setColumnCount(query.record().count())
                self.uiIngresarProducto.tblWProductoStock.setRowCount(query.size())
                self.uiIngresarProducto.tblWProductoStock.setHorizontalHeaderLabels(["DESCRIPCION_PRODUCTO", "CANTIDAD",  "PRECIO_UNITARIO "])
                index=0

                while (query.next()):
                        self.uiIngresarProducto.tblWProductoStock.setItem(index,0,QTableWidgetItem(query.value(0).toString()))
                        self.uiIngresarProducto.tblWProductoStock.setItem(index,1,QTableWidgetItem(query.value(1).toString()))
                        self.uiIngresarProducto.tblWProductoStock.setItem(index,2,QTableWidgetItem(query.value(2).toString()))
                        self.stock = int(query.value(1).toString())
                        self.idProducto = int(str(idP))

                        print 'stock: ', self.stock
                        print 'id: ', self.idProducto
                        index = index+1
                        self.uiIngresarProducto.spinBox.setMinimum(0)
                        self.uiIngresarProducto.spinBox.setMaximum(self.stock)

                self.uiIngresarProducto.tblWProductoStock.resizeColumnsToContents()
                self.uiIngresarProducto.tblWProductoStock.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        def toInt(self,num):
                try:
                        return int(num)
                except exceptions.ValueError:
                        return None
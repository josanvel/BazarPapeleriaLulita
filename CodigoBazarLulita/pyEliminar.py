'''
Created on 15/03/2015

@author: josanvel
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui, QtSql
from Eliminar import Ui_Eliminar

lista_Productos = []
class MyformEliminar(QtGui.QMainWindow):

        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiEliminar= Ui_Eliminar()
                self.uiEliminar.setupUi(self)
                self.center()

                self.connect(self.uiEliminar.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarEliminar)
                self.connect(self.uiEliminar.btnBuscar, QtCore.SIGNAL("clicked()"), self.buscarProducto)
                self.connect(self.uiEliminar.btnEliminar, QtCore.SIGNAL("clicked()"), self.eliminarProducto)

        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarEliminar(self):
                self.hide()
                self.ventana.show()

        def buscarProducto(self):
                if not QtSql.QSqlDatabase.database().isOpen():
                        if not QtSql.QSqlDatabase.database():
                                QtGui.QMessageBox.information(None,'BASES DE DATOS', 'No se pudo abrir la BASES DE DATOS')

                buscar = self.uiEliminar.txtBuscar.displayText()
                model = QtSql.QSqlTableModel(self)

                '''
                model.setQuery(QtSql.QSqlQuery("call PRQueryBuscarProducto('"+buscar+"')"))
                model.select();

                self.uiEliminar.tblVwEliminar.setModel(model)
                self.uiEliminar.tblVwEliminar.resizeColumnsToContents()
                self.uiEliminar.tblVwEliminar.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
                '''
                
                query = QtSql.QSqlQuery("call PRQueryBuscarProducto('"+buscar+"')")
                fieldNo_IdProd =  query.record().indexOf("IdProducto")
                fieldNo_Descripcion =  query.record().indexOf("Descripcion")
                fieldNo_PrecioReal =  query.record().indexOf("PrecioReal")
                fieldNo_Stock =  query.record().indexOf("stock")

                while query.next():
                        idP = query.value(fieldNo_IdProd).toString()
                        descrip = query.value(fieldNo_Descripcion).toString()
                        precReal = query.value(fieldNo_PrecioReal).toString()
                        stock = query.value(fieldNo_Stock).toString()
                        producto = idP +'-'+descrip+'-'+precReal+'-'+stock
                        lista_Productos.append(producto)

                model = QStandardItemModel()
                tam = len(lista_Productos)

                for n in range(tam):
                        item = QStandardItem(lista_Productos[n])
                        item.setCheckable(True)
                        model.appendRow(item)

                self.uiEliminar.tblVwEliminar.setModel(model)
                self.uiEliminar.tblVwEliminar.resizeColumnsToContents()
                self.uiEliminar.tblVwEliminar.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())

        def eliminarProducto(self):

                QtGui.QMessageBox.information(None,'Eliminar Producto/s', 'Esta seguro de ELIMINAR Producto/s')

                model = self.uiEliminar.tblVwEliminar
                tam = len(lista_Productos)
                
                print tam
                data = []
                for fila in range(tam):
                        data.append([])
                        for columna in range(1):
                                index = model.index(row, column)
                                print index
                                data[row].append(str(model.data(index).toString()))
'''
Created on 15/03/2015

@author: josanvel
'''
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui, QtSql
from Modificar import Ui_Modificar

lista_Productos = []
class MyformModificar(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiModificar = Ui_Modificar()
                self.uiModificar.setupUi(self)
                self.center()

                self.connect(self.uiModificar.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarModificar)
                self.connect(self.uiModificar.btnBuscar, QtCore.SIGNAL("clicked()"), self.buscarProducto)
                self.connect(self.uiModificar.btnGuadar, QtCore.SIGNAL("clicked()"), self.guardarProducto)

        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarModificar(self):
                self.hide()
                self.ventana.show()

        def buscarProducto(self):
                if not QtSql.QSqlDatabase.database().isOpen():
                        if not QtSql.QSqlDatabase.database():
                                QtGui.QMessageBox.information(None,'BASES DE DATOS', 'No se pudo abrir la BASES DE DATOS')

                buscar = self.uiModificar.txtBuscar.displayText()
                model = QtSql.QSqlTableModel(self)
                
                query = QtSql.QSqlQuery("call PRQueryBuscarProducto('"+buscar+"')")
                model.setQuery(query)
                model.select()

                self.uiModificar.tblVwModificar.setModel(model)
                self.uiModificar.tblVwModificar.resizeColumnsToContents()
                
                '''
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

                self.uiModificar.tblVwModificar.setModel(model)
                self.uiModificar.tblVwModificar.resizeColumnsToContents()
                self.uiModificar.tblVwModificar.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
                '''

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())
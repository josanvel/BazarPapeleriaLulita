'''
Created on 02/05/2015

@author: josanvel
'''
from PyQt4.QtGui import * 
from PyQt4.QtSql import * 
from PyQt4.QtCore import * 
from PyQt4 import QtCore, QtGui, QtSql
from Cambiar import Ui_Cambiar

lista_Productos = []
class MyformCambiar(QtGui.QComboBox):
        def __init__(self, parent=None):
                super(MyformCambiar, self).__init__(parent)
                self.uiCambiar = Ui_Cambiar()
                self.uiCambiar.setupUi(self)
                self.center()

                self.comboBoxProducto(self.uiCambiar.cbxBuscar)
                self.mostrarProducto()

                self.connect(self.uiCambiar.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarCambiar)
                self.connect(self.uiCambiar.btnGuardar, QtCore.SIGNAL("clicked()"), self.guardarProducto)

        def comboBoxProducto(self, combobox):
                self.comboBoxP(combobox)
                def filter(text):
                        self.comboboxF.pFilterModel.setFilterFixedString(str(text))

                self.comboboxF.lineEdit().textEdited[unicode].connect(filter)
                self.comboboxF.completer.activated.connect(self.on_completer_activated)

                self.llenarComboBoxProducto()

        def comboBoxP(self, combobox):
                self.comboboxF = combobox 
                self.comboboxF.setFocusPolicy(QtCore.Qt.StrongFocus)
                self.comboboxF.setEditable(True)

                self.comboboxF.pFilterModel = QtGui.QSortFilterProxyModel(self)
                combobox.pFilterModel.setFilterCaseSensitivity(QtCore.Qt.CaseInsensitive)
                self.comboboxF.pFilterModel.setSourceModel(self.comboboxF.model())

                self.comboboxF.completer = QtGui.QCompleter(self)

                self.comboboxF.completer.setModel(self.comboboxF.pFilterModel)
                self.comboboxF.completer.setCompletionMode(QtGui.QCompleter.UnfilteredPopupCompletion)
                self.comboboxF.setCompleter(self.comboboxF.completer)

        def on_completer_activated(self, text):
                #print "activated"
                if text:
                        #print "text: ", text
                        index = self.comboboxF.findText(str(text))
                        #print "index: ", index
                        self.comboboxF.setCurrentIndex(index)
                        self.buscarProducto(index)

        def buscarProducto(self, indice):
            if not QtSql.QSqlDatabase.database().isOpen():
                if not QtSql.QSqlDatabase.database():
                    QtGui.QMessageBox.information(None, 'BASES DE DATOS', 'No se pudo abrir la BASES DE DATOS') 

            query = QtSql.QSqlQuery("call PRQueryBuscarProductoID("+str(indice)+")")
            self.uiCambiar.tbVwActualizarProducto.setColumnCount(query.record().count())
            self.uiCambiar.tbVwActualizarProducto.setRowCount(query.size())
            self.uiCambiar.tbVwActualizarProducto.setHorizontalHeaderLabels(["ID", "DescripcionProductoBazarPapeleria", "PrecReal", "PrecIva", "StockInicial", "StockActual"])

            index=0
            while query.next():
                idp = query.value(0).toString()
                descripcion = query.value(1).toString()
                precioR = query.value(2).toString()
                precioI = query.value(3).toString()
                stockI = query.value(4).toString()
                stockA = query.value(5).toString()

                self.uiCambiar.tbVwActualizarProducto.setItem(index,0,QTableWidgetItem(idp))
                self.uiCambiar.tbVwActualizarProducto.setItem(index,1,QTableWidgetItem(descripcion))
                self.uiCambiar.tbVwActualizarProducto.setItem(index,2,QTableWidgetItem(precioR))
                self.uiCambiar.tbVwActualizarProducto.setItem(index,3,QTableWidgetItem(precioI))
                self.uiCambiar.tbVwActualizarProducto.setItem(index,4,QTableWidgetItem(stockI))
                self.uiCambiar.tbVwActualizarProducto.setItem(index,5,QTableWidgetItem(stockA))
                index = index+1

            self.uiCambiar.tbVwActualizarProducto.hideColumn(0)
            self.uiCambiar.tbVwActualizarProducto.resizeColumnsToContents()

        def setModel(self, model):
                super(MyformCambiar, self).setModel(model)
                self.comboboxF.pFilterModel.setSourceModel(model)
                self.comboboxF.completer.setModel(self.pFilterModel)

        def setModelColumn(self, column):
                self.comboboxF.completer.setCompletionColumn(column)
                self.comboboxF.pFilterModel.setFilterKeyColumn(column)
                super(MyformCambiar, self).setModelColumn(column)

        def llenarComboBoxProducto(self):
                if not QtSql.QSqlDatabase.database().isOpen():
                        if not QtSql.QSqlDatabase.database():
                                QtGui.QMessageBox.information(None,'BASES DE DATOS', 'No se pudo abrir la BASES DE DATOS')

                query = QtSql.QSqlQuery("call PRQueryProducto()")
                lista = [""]
                while query.next():
                        producto = query.value(1).toString()
                        lista.append(str(producto))
                # fill the standard model of the combobox
                self.comboboxF.addItems(lista)
                self.comboboxF.setModelColumn(0)
                self.comboboxF.show()

        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarCambiar(self):
            reply = QtGui.QMessageBox.question(self, 'ACTUALIZACION', "Se perdera informacion de la Actualizacion de los Productos", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
            if reply == QtGui.QMessageBox.Yes:
                self.hide()
                self.ventana.show()

        def mostrarProducto(self):
            if not QtSql.QSqlDatabase.database().isOpen():
                if not QtSql.QSqlDatabase.database():
                    QtGui.QMessageBox.information(None, 'BASES DE DATOS', 'No se pudo abrir la BASES DE DATOS') 

            query = QtSql.QSqlQuery("call PRQueryProducto()")

            self.uiCambiar.tbVwActualizarProducto.setColumnCount(query.record().count())
            self.uiCambiar.tbVwActualizarProducto.setRowCount(query.size())
            self.uiCambiar.tbVwActualizarProducto.setHorizontalHeaderLabels(["ID", "DescripcionProductoBazarPapeleria", "PrecReal", "PrecIva", "StockInicial", "StockActual"])

            index=0
            while query.next():
                self.uiCambiar.tbVwActualizarProducto.setItem(index,0,QTableWidgetItem(query.value(0).toString()))
                self.uiCambiar.tbVwActualizarProducto.setItem(index,1,QTableWidgetItem(query.value(1).toString()))
                self.uiCambiar.tbVwActualizarProducto.setItem(index,2,QTableWidgetItem(query.value(2).toString()))
                self.uiCambiar.tbVwActualizarProducto.setItem(index,3,QTableWidgetItem(query.value(3).toString()))
                self.uiCambiar.tbVwActualizarProducto.setItem(index,4,QTableWidgetItem(query.value(4).toString()))
                self.uiCambiar.tbVwActualizarProducto.setItem(index,5,QTableWidgetItem(query.value(5).toString()))
                index = index+1

            self.uiCambiar.tbVwActualizarProducto.hideColumn(0)
            self.uiCambiar.tbVwActualizarProducto.resizeColumnsToContents()

        def guardarProducto(self):
            fila = self.uiCambiar.tbVwActualizarProducto.rowCount()
            for row in range(fila):
                item1 = self.uiCambiar.tbVwActualizarProducto.item(row, 0)
                item2 = self.uiCambiar.tbVwActualizarProducto.item(row, 1)
                item3 = self.uiCambiar.tbVwActualizarProducto.item(row, 2)
                item4 = self.uiCambiar.tbVwActualizarProducto.item(row, 3)
                item5 = self.uiCambiar.tbVwActualizarProducto.item(row, 4)
                item6 = self.uiCambiar.tbVwActualizarProducto.item(row, 5)

                idP = str(unicode(item1.text()).encode('utf8'))
                descripcion = str(unicode(item2.text()).encode('utf8'))
                precioReal = (str(unicode(item3.text()).encode('utf8')))
                precioIva = (str(unicode(item4.text()).encode('utf8')))
                stockInicial = (str(unicode(item5.text()).encode('utf8')))
                stockActual = (str(unicode(item6.text()).encode('utf8')))

                query = QtSql.QSqlQuery("call PRUpdateProducto("+idP+",'"+descripcion+"',"+precioReal+","+precioIva+","+stockInicial+","+stockActual+");")

                if not query.exec_():
                    QtGui.QMessageBox.warning( None, "ERROR-ACTUALIZAR",\
                        "No se pudo ACTUALIZAR los PRODUCTO" )
                else:
                    QtGui.QMessageBox.information(None, "ACTUALIZAR","Se Actualizaron los Producto") 
                    self.hide()
                    self.ventana.show()

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())

        def toInt(self,num):
                try:
                        return int(num)
                except exceptions.ValueError:
                        return None
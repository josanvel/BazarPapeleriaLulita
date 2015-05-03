'''
Created on 01/05/2015

@author: josanvel
'''
from PyQt4.QtGui import * 
from PyQt4.QtSql import * 
from PyQt4.QtCore import * 
from PyQt4 import QtCore, QtGui, QtSql
import exceptions
from Facturacion import Ui_Facturacion
from pyIngresarProducto import MyformIngresarProducto
import datetime


class MyformFacturacion(QtGui.QComboBox):
        def __init__(self, parent=None):
                super(MyformFacturacion, self).__init__(parent)

                self.uiFacturacion = Ui_Facturacion()
                self.uiFacturacion.setupUi(self)
                self.center()
                self.index = 0

                

                self.comboBoxCliente(self.uiFacturacion.cbxCliente)
                self.comboBoxCedula(self.uiFacturacion.cbxCedula)
                self.comboBoxProducto(self.uiFacturacion.cbxProducto)

                self.connect(self.uiFacturacion.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarFacturacion)
                self.connect(self.uiFacturacion.btnGuardar, QtCore.SIGNAL("clicked()"), self.guardarFactura)
                self.uiFacturacion.txtPago.returnPressed.connect(self.getVuelto)

        def guardarFactura(self):

                cliente = str(self.uiFacturacion.cbxCliente.currentText())
                cedula = str(self.uiFacturacion.cbxCedula.currentText())
                direcion = str(unicode(self.uiFacturacion.txtDireccion.displayText()).encode('utf8'))
                fechaActual = QtCore.QDateTime.currentDateTime()
                now = datetime.datetime.now()

                #Ingresar los datos del clientes a la bases de datos
                queryNombre = QtSql.QSqlQuery("call PRQueryClienteNombre('"+cliente+"');")
                print 'Guardar1: ', cliente, queryNombre.size()
                if queryNombre.size() == 1:
                        index = 0
                        while queryNombre.next():
                                idClienteQuery = queryNombre.value(0).toString()
                                cedulaQuery = queryNombre.value(4).toString()
                        if cedula == cedulaQuery:
                                idCliente = idClienteQuery
                                queryDireccion = QtSql.QSqlQuery("call PRUpdateCliente('"+direcion+"',"+idCliente+",'"+cedula+"');")
                                print 'Guardar2: ', direcion, idCliente, cedula, queryDireccion.size()
                        else:
                                QtGui.QMessageBox.information(None, 'DATOS INCORRECTOS','Nombre y Cedula no coinciden.')
                else:
                        queryIngresar = QtSql.QSqlQuery("call PRInsertCliente('"+cliente+"','"+direcion+"',null, '"+cedula+"', null);")
                        queryNombre = QtSql.QSqlQuery("call PRQueryClienteNombre('"+cliente+"');")

                        index = 0
                        while queryNombre.next():
                                idClienteQuery = queryNombre.value(0).toString()
                                cedulaQuery = queryNombre.value(4).toString()
                        idCliente = idClienteQuery
                print 'Datos del cliente:  ',cliente, idCliente

                #Ingresando una factura con los datos del cliente y el vendedor
                usuario = str(self.user)
                queryUser = QtSql.QSqlQuery("call PRQueryCuentaUser('"+usuario+"');")
                print 'Guardar3: ', usuario, queryUser.size()
                index = 0
                while queryUser.next():
                        idCuentaQuery = queryUser.value(0).toString()
                        usuarioQuery = queryUser.value(1).toString()

                queryFactura = QtSql.QSqlQuery()
                queryFactura.prepare("call PRInsertFactura(?,?,?)")
                queryFactura.addBindValue(idCliente)
                queryFactura.addBindValue(fechaActual)
                queryFactura.addBindValue(idCuentaQuery)
                print 'Guardar4: '
                if not queryFactura.exec_():
                        print "No se pudo ingresar una factura " 
                else:
                        print "Se ingreso una factura"

                queryFacturaID =QtSql.QSqlQuery("call PRQueryFacturaID('"+idCliente+"','"+idCuentaQuery+"');")
                while queryFacturaID.next():
                        idFacturaQuery = queryFacturaID.value(0).toString()

                print 'Guardar6: ', idFacturaQuery

                #Actualizar PRODUCTO de la factura
                fila = self.uiFacturacion.tbVwFactura.rowCount()
                for row in range(fila):
                        item1 = self.uiFacturacion.tbVwFactura.item(row, 0)
                        item2 = self.uiFacturacion.tbVwFactura.item(row, 1)
                        item3 = self.uiFacturacion.tbVwFactura.item(row, 2)
                        item4 = self.uiFacturacion.tbVwFactura.item(row, 3)

                        cantidad = int(str(unicode(item1.text()).encode('utf8')))
                        descripcion = str(unicode(item2.text()).encode('utf8'))
                        precioIva = (str(unicode(item3.text()).encode('utf8')))
                        total = (str(unicode(item4.text()).encode('utf8')))

                        queryProducto = QtSql.QSqlQuery("call PRQueryBuscarProducto('"+descripcion+"');")
                        while queryProducto.next():
                                idProducto = queryProducto.value(0).toString()
                                stockActual = queryProducto.value(4).toString()
                        print 'Guardar7: ', descripcion, queryProducto.size()

                        stock= int(stockActual) - cantidad
                        print 'stock en bazar: ',stock
                        queryUpdateFactura = QtSql.QSqlQuery("call PRUpdateProductoFactura("+str(idProducto)+","+str(stock)+");")
                        print 'Guardar8: '
                        if not queryUpdateFactura.exec_():
                                print "No se pudo actualizo el producto "
                        else:
                                print "Se actualizo el producto"

                        #Ingresar DETALLE de la factura
                        #CALL PRInsertDetalle(4,'0.45', '1.80', 2,1);
                        queryInsertFactura = QtSql.QSqlQuery("call PRInsertDetalle('"+str(cantidad)+"','"+precioIva+"','"+total+"','"+str(idProducto)+"','"+idFacturaQuery+"')")

        def comboBoxCliente(self, combobox):
                self.comboBoxP(combobox)
                def filter(text):
                        #print "Edited: ", text, "type: ", type(text)
                        self.uiFacturacion.cbxCliente.pFilterModel.setFilterFixedString(str(text))

                self.uiFacturacion.cbxCliente.lineEdit().textEdited[unicode].connect(filter)
                self.uiFacturacion.cbxCliente.completer.activated.connect(self.on_completer_activated)

                self.llenarComboBoxCliente()

        def comboBoxCedula(self, combobox):
                self.comboBoxP(combobox)
                def filter(text):
                        #print "Edited: ", text, "type: ", type(text)
                        self.uiFacturacion.cbxCedula.pFilterModel.setFilterFixedString(str(text))

                self.uiFacturacion.cbxCedula.lineEdit().textEdited[unicode].connect(filter)
                self.uiFacturacion.cbxCedula.completer.activated.connect(self.on_completer_activated)


                self.llenarComboBoxCedula()

        def comboBoxProducto(self, combobox):
                self.comboBoxP(combobox)
                def filter(text):
                        #print "Edited: ", text, "type: ", type(text)
                        self.uiFacturacion.cbxProducto.pFilterModel.setFilterFixedString(str(text))

                self.uiFacturacion.cbxProducto.lineEdit().textEdited[unicode].connect(filter)
                self.uiFacturacion.cbxProducto.completer.activated.connect(self.on_completer_activated)

                self.llenarComboBoxProductos()

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

        def ingresarFactura(self):
                self.ingresarProducto = MyformIngresarProducto(self)
                i = self.toInt(str(self.indexP))

                self.ingresarProducto.getProducto(i, self)
                self.ingresarProducto.show()

        def getCantidadProducto(self, cantidad, idP):
                self.cant = cantidad
                self.idPr = idP
                #print self.cant, self.idPr
                self.mostrarProductoIngresado()

        def mostrarProductoIngresado(self):

                self.comboboxF.setCurrentIndex(0)
                query = QtSql.QSqlQuery("CALL PRQueryBuscarProductoID("+str(self.idPr)+");")
                
                columna = query.record().count()+1
                #print 'columna: ', columna
                self.uiFacturacion.tbVwFactura.setColumnCount(query.record().count()+1)
                self.uiFacturacion.tbVwFactura.setRowCount(query.size()+self.index)
                self.uiFacturacion.tbVwFactura.setHorizontalHeaderLabels(["CANTIDAD", "DESCRIPCION_PRODUCTO",  "PRECIO_UNITARIO", "TOTAL_PRODUCTO"])

                while (query.next()):
                        cantidad = str(self.cant)
                        self.uiFacturacion.tbVwFactura.setItem(self.index,0,QTableWidgetItem(cantidad))
                        
                        self.uiFacturacion.tbVwFactura.setItem(self.index,1,QTableWidgetItem(query.value(0).toString()))
                        
                        precioUnitario = str(query.value(2).toString())
                        self.uiFacturacion.tbVwFactura.setItem(self.index,2,QTableWidgetItem(precioUnitario))
                        
                        total = str(float(cantidad) * float(precioUnitario))
                        #print 'total: ', total
                        self.uiFacturacion.tbVwFactura.setItem(self.index,3,QTableWidgetItem(total))
                        self.index = self.index+1

                self.uiFacturacion.tbVwFactura.resizeColumnsToContents()
                self.uiFacturacion.tbVwFactura.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

                totalP = 0
                for row in range(self.index):
                        for column in xrange(3,columna):
                                precio = self.uiFacturacion.tbVwFactura.item(row,column)
                                totalP = totalP + float(str((unicode(precio.text()).encode('utf8'))))

                subtotalP =  totalP / 1.12
                ivaP = totalP - subtotalP
                self.uiFacturacion.txtSubtotal.setText(str(subtotalP))
                self.uiFacturacion.txtIva.setText(str(ivaP))
                self.uiFacturacion.txtTotal.setText(str(totalP))

        def getVuelto(self):
                pago = str(self.uiFacturacion.txtPago.text())
                total = str(self.uiFacturacion.txtTotal.text())
                vuelto = float(pago) - float(total)
                self.uiFacturacion.txtVuelto.setText(str(vuelto))

        def on_completer_activated(self, text):
                if text:
                        #print "text: ", text
                        self.indexP = (self.uiFacturacion.cbxProducto.findText(str(text)))
                        self.indexC = (self.uiFacturacion.cbxCliente.findText(str(text)))
                        self.indexCI = (self.uiFacturacion.cbxCedula.findText(str(text)))
                        if self.indexC > 0:
                                #print 'indice Cliente', self.indexC
                                self.uiFacturacion.cbxCliente.setCurrentIndex(self.indexC)
                                self.uiFacturacion.cbxCedula.setCurrentIndex(self.indexC)
                                self.getDireccionCliente(self.indexC)
                        elif self.indexCI >0:
                                #print 'indice Cedula', self.indexCI
                                self.uiFacturacion.cbxCedula.setCurrentIndex(self.indexCI)
                                self.uiFacturacion.cbxCliente.setCurrentIndex(self.indexCI)
                                self.getDireccionCliente(self.indexCI)
                        elif self.indexP >0:
                                #print 'indice Producto', self.indexP
                                self.uiFacturacion.cbxProducto.setCurrentIndex(self.indexP)
                                self.ingresarFactura()

        def getDireccionCliente(self, idC):
                query = QtSql.QSqlQuery("CALL PRQueryClienteID("+str(idC)+");")
                index=0

                while (query.next()):
                        idC = query.value(0).toString()
                        nombre =query.value(1).toString()
                        direccion = query.value(2).toString()
                        fechaN = query.value(3).toString()
                        cedula = query.value(4).toString()
                        telefono =query.value(5).toString()

                self.uiFacturacion.txtDireccion.setText(direccion)

        def setModel(self, model):
                super(MyformFacturacion, self).setModel(model)
                self.comboboxF.pFilterModel.setSourceModel(model)
                self.comboboxF.completer.setModel(self.comboboxF.pFilterModel)

        def setModelColumn(self, column):
                self.comboboxF.completer.setCompletionColumn(column)
                self.comboboxF.pFilterModel.setFilterKeyColumn(column)
                super(MyformFacturacion, self).setModelColumn(column)

        def regresarVentanaR(self, ventanaAtras):
                self.ventana = ventanaAtras

        def regresarFacturacion(self):
                reply = QtGui.QMessageBox.question(self, 'FACTURACION', "Se perdera informacion de la Factura", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
                if reply == QtGui.QMessageBox.Yes:
                        self.hide()
                        self.ventana.show()

                
        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())

        def llenarComboBoxCliente(self):
                if not QtSql.QSqlDatabase.database().isOpen():
                        if not QtSql.QSqlDatabase.database():
                                QtGui.QMessageBox.information(None,'BASES DE DATOS', 'No se pudo abrir la BASES DE DATOS')

                query = QtSql.QSqlQuery("call PRQueryCliente()")
                listaCliente = ["Consumidor Final"]
                while query.next():
                        cliente = query.value(1).toString()
                        listaCliente.append(str(cliente))
                # fill the standard model of the combobox
                self.comboboxF.addItems(listaCliente)
                self.comboboxF.setModelColumn(0)
                self.comboboxF.show()

        def llenarComboBoxCedula(self):
                if not QtSql.QSqlDatabase.database().isOpen():
                        if not QtSql.QSqlDatabase.database():
                                QtGui.QMessageBox.information(None,'BASES DE DATOS', 'No se pudo abrir la BASES DE DATOS')

                query = QtSql.QSqlQuery("call PRQueryCliente()")
                listaCedula = ["null"]
                while query.next():
                        cedula = query.value(4).toString()
                        listaCedula.append(str(cedula))
                # fill the standard model of the combobox
                self.comboboxF.addItems(listaCedula)
                self.comboboxF.setModelColumn(0)
                self.comboboxF.show()

        def llenarComboBoxProductos(self):
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

        def toInt(self,num):
                try:
                        return int(num)
                except exceptions.ValueError:
                        return None

        def obtenerUsuario(self, usuario):
                self.user = usuario

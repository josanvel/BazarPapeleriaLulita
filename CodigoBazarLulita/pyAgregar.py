'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui, QtSql
from Agregar import Ui_Agregar
import exceptions

class MyformAgregar(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiAgregar = Ui_Agregar()
                self.uiAgregar.setupUi(self)
                self.center()

                self.connect(self.uiAgregar.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarAgregar)
                self.connect(self.uiAgregar.btnAgregar, QtCore.SIGNAL("clicked()"), self.ingresarProducto)
                self.uiAgregar.txtPrecioUnitarioIva.returnPressed.connect(self.uiAgregar.btnAgregar.click)

        def regresarVentanaR(self,ventanaAtras):
                self.ventana = ventanaAtras

        def regresarAgregar(self):
            reply = QtGui.QMessageBox.question(self, 'AGREGAR', "Se perdera informacion de los Productos a agregar", QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.Yes)
            if reply == QtGui.QMessageBox.Yes:
                self.hide()
                self.ventana.show()                

        def ingresarProducto(self):
                descripcion = self.uiAgregar.txtDescripcion.displayText()
                precioReal = self.uiAgregar.txtPrecioUnitarioReal.displayText()
                precioIva = self.uiAgregar.txtPrecioUnitarioIva.displayText()
                stock = self.uiAgregar.spinBoxCantidad.value()

                if descripcion!='' and precioReal!='' and precioIva!='' and stock!=0: 
                        if self.toFloatNum(precioReal) == None:
                                QtGui.QMessageBox.information(None, 'Ingreso erroneo','Precio Real incorrecto')
                                self.uiAgregar.txtPrecioUnitarioReal.setText("")
                        elif self.toFloatNum(precioIva) == None:
                                QtGui.QMessageBox.information(None, 'Ingreso erroneo','Precio IVA incorrecto')
                                self.uiAgregar.txtPrecioUnitarioIva.setText("")
                        else:
                                self.IngresarOperacion()
                                self.hide()
                                self.ventana.show()
                else:
                        QtGui.QMessageBox.information(None, 'Campos vacios', 'Todos los campos deben contener informacion')

        def IngresarOperacion(self):
                descrip = str(self.uiAgregar.txtDescripcion.displayText())
                precReal = float(self.uiAgregar.txtPrecioUnitarioReal.displayText())
                precIVA = float(self.uiAgregar.txtPrecioUnitarioIva.displayText())
                stock = int(self.uiAgregar.spinBoxCantidad.value())

                if not QtSql.QSqlDatabase.database().isOpen():
                        if not QtSql.QSqlDatabase.database():
                                QtGui.QMessageBox.information(None, 'BASES DE DATOS', 'No se pudo abrir la BASES DE DATOS') 

                query = QtSql.QSqlQuery()
                query.prepare("call PRInsertProducto(?,?,?,?)")

                query.addBindValue(descrip)
                query.addBindValue(precReal)
                query.addBindValue(precIVA)
                query.addBindValue(stock)

                if not query.exec_():
                        QtGui.QMessageBox.warning( None, "Error al ingresar un producto",\
                                          "No se pudo AGREGAR a un nuevo PRODUCTO" )
                else:
                        QtGui.QMessageBox.information(None, "INFORMACION","Se ingreso un  nuevo Producto") 

        def center(self):
                qr = self.frameGeometry()
                cp = QtGui.QDesktopWidget().availableGeometry().center()
                qr.moveCenter(cp)
                self.move(qr.topLeft())

        def toFloatNum(self, num):
                try:
                        return float(num)
                except exceptions.ValueError:
                        return None
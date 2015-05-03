'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui,  QtSql
from ReporteProducto import Ui_ReporteProducto
import xlwt


class MyformReporteProductos(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiReporteProducto= Ui_ReporteProducto()
                self.uiReporteProducto.setupUi(self)
                self.center()

                self.connect(self.uiReporteProducto.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarReporteProductos)
                self.connect(self.uiReporteProducto.btnGenerar, QtCore.SIGNAL("clicked()"), self.generarReporteProductos)

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

        def generarReporteProductos(self):
                wbk = xlwt.Workbook()
                fila1 = 4

                self.sheet = wbk.add_sheet("sheet")

                style = xlwt.easyxf('font: bold 1')
                self.sheet.write(0,0, "BAZAR Y PAPELERIA LULITA", style)
                self.sheet.write(1,0, "Km 8 1/2 via Daule - Cdla. \"La Gaviota\" Mz. 2262 V. 7", style)

                self.sheet.write(3,0, "DESCRIPCION", style)
                self.sheet.write(3,1, "PRECIO_REAL", style)
                self.sheet.write(3,2, "PRECIO_IVA", style)
                self.sheet.write(3,3, "STOCK", style)

                query = QtSql.QSqlQuery("CALL PRQueryProducto()")

                list_Descrip = []
                list_PrecioR = []
                list_PrecioI = []
                list_Stock = []

                while query.next():
                        descripcion = query.value(1).toString()
                        precioR = query.value(2).toString()
                        precioI = query.value(3).toString()
                        stock = query.value(5).toString()

                        list_Descrip.append(descripcion)
                        list_PrecioR.append(precioR)
                        list_PrecioI.append(precioI)
                        list_Stock.append(stock)

                row = query.size()
                column = 0

                for fila in range(row):
                        try:
                                descripcion = list_Descrip[fila]
                                precioR = list_PrecioR[fila]
                                precioI = list_PrecioI[fila]
                                stock = list_Stock[fila]

                                self.sheet.write(fila+fila1, column, unicode(descripcion).encode('utf8'))
                                column = column +1
                                self.sheet.write(fila+fila1, column, unicode(precioR).encode('utf8'))
                                column = column +1
                                self.sheet.write(fila+fila1, column, unicode(precioI).encode('utf8'))
                                column = column +1
                                self.sheet.write(fila+fila1, column, unicode(stock).encode('utf8'))
                        except AttributeError:
                                pass

                        column = 0
                wbk.save("ReporteProducto.xls")

                message = QtGui.QMessageBox.information(None, "REPORTE PRODUCTO","Se genero el Reporte")
                self.regresarReporteProductos()
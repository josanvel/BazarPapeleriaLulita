'''
Created on 15/03/2015

@author: josanvel
'''

from PyQt4 import QtCore, QtGui, QtSql
from ReporteGanancia import Ui_ReporteGanancia
import sys, csv
import xlwt
from xlwt.Utils import rowcol_to_cell

class MyformReporteGanancias(QtGui.QMainWindow):
        def __init__(self, parent=None):
                QtGui.QWidget.__init__(self, parent)
                self.uiReporteGanancia = Ui_ReporteGanancia()
                self.uiReporteGanancia.setupUi(self)
                self.center()

                self.connect(self.uiReporteGanancia.btnRegresar, QtCore.SIGNAL("clicked()"), self.regresarReporteGanancias)
                self.connect(self.uiReporteGanancia.btnGenerar, QtCore.SIGNAL("clicked()"), self.generarReporteGananciasFecha)

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

        def generarReporteGananciasFecha(self):
                wbk = xlwt.Workbook()
                fila1 = 4

                self.sheet = wbk.add_sheet("sheet")

                style = xlwt.easyxf('font: bold 1')
                self.sheet.write(0,0, "BAZAR Y PAPELERIA LULITA", style)
                self.sheet.write(1,0, "Km 8 1/2 via Daule - Cdla. \"La Gaviota\" Mz. 2262 V. 7", style)

                self.sheet.write(3,0, "CLIENTE", style)
                self.sheet.write(3,1, "CEDULA", style)
                self.sheet.write(3,2, "FECHA", style)
                self.sheet.write(3,3, "DESCRIPCION", style)
                self.sheet.write(3,4, "CANTIDAD", style)
                self.sheet.write(3,5, "PRECIO_UNITARIO", style)
                self.sheet.write(3,6, "PRECIO_TOTAL", style)

                dia1 =self.uiReporteGanancia.dteFechaInicial.date().day()
                mes1 =self.uiReporteGanancia.dteFechaInicial.date().month()
                ano1 =self.uiReporteGanancia.dteFechaInicial.date().year()

                dia2 =self.uiReporteGanancia.dteFechaFinal.date().day()
                mes2 =self.uiReporteGanancia.dteFechaFinal.date().month()
                ano2 =self.uiReporteGanancia.dteFechaFinal.date().year()


                fechaInicial = str(ano1)+"/"+str(mes1)+"/"+str(dia1)
                fechaFinal = str(ano2)+"/"+str(mes2)+"/"+str(dia2)

                query = QtSql.QSqlQuery("CALL PRQueryProductoFecha('"+fechaInicial+"','"+fechaFinal+"')")
                print query.size()
                list_Descrip = []
                list_Cantidad = []
                list_PrecioUnitario = []
                list_PrecioTotal = []
                list_Nombre = []
                list_Cedula = []
                list_Fecha = []

                while query.next():
                        descripcion = query.value(0).toString()
                        cantidad = query.value(1).toString()
                        precioU = query.value(2).toString()
                        precioT = query.value(3).toString()
                        nombre = query.value(4).toString()
                        cedula = query.value(5).toString()
                        fecha = query.value(6).toString()

                        list_Descrip.append(descripcion)
                        list_Cantidad.append(cantidad)
                        list_PrecioUnitario.append(precioU)
                        list_PrecioTotal.append(precioT)
                        list_Nombre.append(nombre)
                        list_Cedula.append(cedula)
                        list_Fecha.append(fecha)
                #CALL PRQueryProductoFecha('2015-05-02','2015-05-03');

                row = query.size()
                column = 0

                for fila in range(row):
                        try:
                                descripcion = list_Descrip[fila]
                                cantidad = list_Cantidad[fila]
                                precioU = list_PrecioUnitario[fila]
                                precioT = list_PrecioTotal[fila]
                                nombre = list_Nombre[fila]
                                cedula = list_Cedula[fila]
                                fecha = list_Fecha[fila]

                                self.sheet.write(fila+fila1, column, unicode(nombre).encode('utf8'))
                                column = column +1
                                self.sheet.write(fila+fila1, column, unicode(cedula).encode('utf8'))
                                column = column +1
                                self.sheet.write(fila+fila1, column, unicode(fecha).encode('utf8'))
                                column = column +1
                                self.sheet.write(fila+fila1, column, unicode(descripcion).encode('utf8'))
                                column = column +1
                                self.sheet.write(fila+fila1, column, unicode(cantidad).encode('utf8'))
                                column = column +1
                                self.sheet.write(fila+fila1, column, unicode(precioU).encode('utf8'))
                                column = column +1
                                self.sheet.write(fila+fila1, column, unicode(precioT).encode('utf8'))
                                column = column +1
                        except AttributeError:
                                pass
                        column = 0
                self.sheet.write(row+fila1,5, "TOTAL", style)

                
                for x in xrange(6,7):
                        first_price_cell = rowcol_to_cell(fila1, x)
                        last_price_cell = rowcol_to_cell(fila+fila1, x)
                        total_formula = "SUM(%s:%s)" % (first_price_cell, last_price_cell)
                        self.sheet.write(row+fila1, x, xlwt.Formula(total_formula), style)

                wbk.save("ReporteGananciasFecha.xls")

                message = QtGui.QMessageBox.information(None, "REPORTE GANANCIAS","Se genero el Reporte")
                self.regresarReporteGanancias()

        def generarReporteGanancias(self):
                wbk = xlwt.Workbook()
                fila1 = 4

                self.sheet = wbk.add_sheet("sheet")

                style = xlwt.easyxf('font: bold 1')
                self.sheet.write(0,0, "BAZAR Y PAPELERIA LULITA", style)
                self.sheet.write(1,0, "Km 8 1/2 via Daule - Cdla. \"La Gaviota\" Mz. 2262 V. 7", style)

                self.sheet.write(3,0, "DESCRIPCION", style)
                self.sheet.write(3,1, "PRECIO_REAL", style)
                self.sheet.write(3,2, "PRECIO_IVA", style)
                self.sheet.write(3,3, "STOCK_INICIAL", style)
                self.sheet.write(3,4, "STOCK_ACTUAL", style)
                self.sheet.write(3,5, "VENTAS_SIN_IVA", style)
                self.sheet.write(3,6, "VENTAS_CON_IVA", style)
                self.sheet.write(3,7, "GANANCIA_PRODUCTO", style)

                query = QtSql.QSqlQuery("CALL PRQueryProducto()")

                list_Descrip = []
                list_PrecioR = []
                list_PrecioI = []
                list_StockI = []
                list_StockA = []

                while query.next():
                        descripcion = query.value(1).toString()
                        precioR = query.value(2).toString()
                        precioI = query.value(3).toString()
                        stockI = query.value(4).toString()
                        stockA = query.value(5).toString()

                        list_Descrip.append(descripcion)
                        list_PrecioR.append(precioR)
                        list_PrecioI.append(precioI)
                        list_StockI.append(stockI)
                        list_StockA.append(stockA)

                row = query.size()
                column = 0

                for fila in range(row):
                        try:
                                descripcion = list_Descrip[fila]
                                precioR = list_PrecioR[fila]
                                precioI = list_PrecioI[fila]
                                stockI = list_StockI[fila]
                                stockA = list_StockA[fila]

                                self.sheet.write(fila+fila1, column, unicode(descripcion).encode('utf8'))
                                column = column +1
                                self.sheet.write(fila+fila1, column, unicode(precioR).encode('utf8'))
                                column = column +1
                                self.sheet.write(fila+fila1, column, unicode(precioI).encode('utf8'))
                                column = column +1
                                self.sheet.write(fila+fila1, column, unicode(stockI).encode('utf8'))
                                column = column +1
                                self.sheet.write(fila+fila1, column, unicode(stockA).encode('utf8'))
                                column = column +1
                                
                                if column == 5:
                                        item = '(D5 - E5)*B5'
                                        a = str(fila+fila1+1)
                                        self.sheet.write(fila+fila1, column, xlwt.Formula("(D"+a+" - E"+a+")*B"+a))
                                        column = column +1
                                if column == 6:
                                        item = '(D5 - E5)*C5'
                                        a = str(fila+fila1+1)
                                        self.sheet.write(fila+fila1, column, xlwt.Formula("(D"+a+" - E"+a+")*C"+a))
                                        column = column +1
                                if column == 7:
                                        item = '(G5 - F5)'
                                        a = str(fila+fila1+1)
                                        self.sheet.write(fila+fila1, column, xlwt.Formula("G"+a+" - F"+a))
                        except AttributeError:
                                pass

                        column = 0
                self.sheet.write(row+fila1,4, "TOTAL", style)

                for x in xrange(5,8):
                        first_price_cell = rowcol_to_cell(fila1, x)
                        last_price_cell = rowcol_to_cell(fila+fila1, x)
                        total_formula = "SUM(%s:%s)" % (first_price_cell, last_price_cell)
                        self.sheet.write(row+fila1, x, xlwt.Formula(total_formula), style)

                wbk.save("ReporteGanancias.xls")

                message = QtGui.QMessageBox.information(None, "REPORTE GANANCIAS","Se genero el Reporte")
                self.regresarReporteGanancias()
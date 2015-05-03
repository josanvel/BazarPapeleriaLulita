#!/usr/bin/python
'''
Created on 15/03/2015

@author: josanvel
'''
import sys
from PyQt4 import QtGui
from pyLogin import pyLoginP

def main():
    aplicacion = QtGui.QApplication(sys.argv)
    login = pyLoginP()
    login.show()
    sys.exit(aplicacion.exec_())

if __name__ == '__main__':
    main()

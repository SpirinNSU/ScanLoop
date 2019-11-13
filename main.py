"""
 V.15
 13.11.2019
"""

# -*- coding: utf-8 -*-

import sys
from PyQt5 import QtWidgets 
from Windows.MainWindow import MainWindow

       
def main():
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    main = MainWindow()
    main.show()

    return main

if __name__ == '__main__':         
    m = main()
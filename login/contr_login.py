#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from login import Ui_MainWindow
import manejo_bd

class Main(QtGui.QMainWindow):

    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.ui =  Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.iniciar_botones()



    def iniciar_botones(self):
        """
        Funcion que inicia las señales de los objetos
        """
        self.ui.pushButton.clicked.connect(self.entra)
        self.ui.label_4.setText("")


    def entra(self):
        
        menu = controladorMenu.Display(self)
        menu.exec_()


        """clave = manejo_bd.consulta_clave(unicode(self.ui.lineEdit.text()))
        clave2 = clave[0]
        print type(clave2)
        clave1 =unicode(self.ui.lineEdit.text())
        print type(clave1)
        if clave2 ==clave1:
            menu = controladorMenu.Display(self)
            menu.exec_()
        else:
            menu = controladorMenu.Display(self)
            menu.exec_()
            #self.errorMessageDialog = QtGui.QErrorMessage(self)
            #self.errorMessageDialog.showMessage("error de ingreso")"""
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())



        
    

    
    

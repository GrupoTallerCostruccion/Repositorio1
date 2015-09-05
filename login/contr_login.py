#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from login import Ui_MainWindow
import menu_controlador
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
        datos = manejo_bd.consulta_claves()
        for row in datos:
            print row['id']
            if(row['id']==str(self.ui.lineEdit.text()) and row['pass']==str(self.ui.lineEdit_2.text())):
                menu = menu_controlador.Main(self)
                menu.exec_
       
        else:
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("error de ingreso")
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())



        
    

    
    

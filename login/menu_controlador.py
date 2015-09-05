#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from menu import Ui_MainWindow
import manejo_bd 
import modulo_clientes.controlador_modulo_cliente as controlador_modulo_cliente
import modulo_marcas.vista_marca as vista_marca
import modulo_modelos.vista_modelo as vista_modelo



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
        self.ui.BotonMarcas.clicked.connect(self.entraMarca)
        self.ui.BotonClientes.clicked.connect(self.entraCliente)
        self.ui.BotonModelos.clicked.connect(self.entraModelo)
    def entraMarca(self):
        marca = vista_marca.Main(self)
        marca.exec_()



    def entraCliente(self):
        cliente=controlador_modulo_cliente.Main(self)
        cliente.exec_()
    def entraModelo(self):
        modelo=vista_modelo.Main(self)
        modelo.exec_()    


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())



        
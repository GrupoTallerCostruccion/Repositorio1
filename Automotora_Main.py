#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui
from ui_main import Ui_MainWindow as Ui_Main
from modulo_clientes.controlador_modulo_cliente import Main as Mod1
from modulo_marcas.vista_marca import Main as Mod2
from modulo_modelos.vista_modelo import Main as Mod3
from login.vista_login import Main as Mod4

class Main(QtGui.QMainWindow):
    """
    Módulo principal del sistema
    """
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_Main()
        self.ui.setupUi(self)
        # Cargamos las acciones al presionar el menú
        self.menu_actions()
        self.show()

    def menu_actions(self):
        self.ui.actionModulo_Clientes.triggered.connect(self.load_mod1)
        self.ui.actionMarcas.triggered.connect(self.load_mod2)
        self.ui.actionModelosAutos.triggered.connect(self.load_mod3)
        self.ui.actionLogin.triggered.connect(self.load_mod4)
        
    def load_mod1(self):
        """carga modulo clientes"""
        widget = Mod1(self)
        self.setCentralWidget(widget)

    def load_mod2(self):
        """
        carga modulo marcas
        """
        widget = Mod2(self)
        self.setCentralWidget(widget)

    def load_mod3(self):
        """
        carga modulo modelos
        """
        widget = Mod3(self)
        self.setCentralWidget(widget)

    def load_mod4(self):
        """
        carga modulo del login
        """
        widget = Mod4(self)
        self.setCentralWidget(widget)

    def activar(self):
        """
        Este metodo lo llamara el login para activar las
        opciones princupales [originalmente estan desasctivadas]
        """
        self.ui.actionModulo_Clientes.setEnabled(True)
        self.ui.actionMarcas.setEnabled(True)
        self.ui.actionModelosAutos.setEnabled(True)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

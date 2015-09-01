#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
from form_compra import Ui_Dialog
import manejo_bd_clientes

class Display(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Dialog()
        self.editado = False
        self.nombre = ""
        self.apellido= ""
        self.ui.setupUi(self)
        self.cargar_datos("")
        self.iniciar_botones()
    def cargar_datos(self,text):
        """
        Función que carga la información de autos en la grilla de compras
        """
        autos = manejo_bd_clientes.obtener_autos()
        #Creamos el modelo asociado a la tabla
        self.model = QtGui.QStandardItemModel(len(autos), 3)
        self.model.setHorizontalHeaderItem(
            0, QtGui.QStandardItem(u"patente"))
        self.model.setHorizontalHeaderItem(
            1, QtGui.QStandardItem(u"color"))
        self.model.setHorizontalHeaderItem(
            2, QtGui.QStandardItem(u"precio_venta"))
        self.model.setHorizontalHeaderItem(
            3, QtGui.QStandardItem(u"cliente_rut"))
       

        for r, row in enumerate(autos):
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['patente'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['color'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['precio_venta'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['cliente_rut'])

        self.ui.tableView.setModel(self.model)

        # Para que las columnas 1 y 2 se estire o contraiga cuando
        # se cambia el tamaño de la pantalla
        self.ui.tableView.horizontalHeader().setResizeMode(
            1, self.ui.tableView.horizontalHeader().Stretch)
        self.ui.tableView.horizontalHeader().setResizeMode(
            2, self.ui.tableView.horizontalHeader().Stretch)

        self.ui.tableView.setColumnWidth(0, 100)
        self.ui.tableView.setColumnWidth(1, 210)
        self.ui.tableView.setColumnWidth(2, 210)
        self.ui.tableView.setColumnWidth(3, 220)
      


    def iniciar_botones(self):
        """
        Funcion que inicia las señales de los objetos
        """
        self.ui.comprar_bt.clicked.connect(self.comprar)
        self.ui.cancelar_bt.clicked.connect(self.cancelar)

    def cancelar(self):
        self.reject()

    def comprar(self):
        
        self.reject()

    def rellenar(self, rut):
        print rut
        """
        Función que carga los datos de un producto en el formulario para poder
        editarlos.
        """
        self.editado = True

        datos = manejo_bd_clientes.datos_clientes(rut)
        
        datos = datos[0]

        rut = unicode(datos[0])
        nombres = unicode(datos[1])
        apelldos = unicode(datos[2])
       
       
        

        self.ui.nom_cliente.setText(nombres+" "+apelldos)
       
    

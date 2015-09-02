#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
from form_registro import Ui_Dialog
import manejo_bd_clientes

class Display(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_Dialog()
        self.editado = False
        self.nombre = ""
        self.apellido= ""
        self.ui.setupUi(self)
        self.iniciar_botones()



    def iniciar_botones(self):
        """
        Funcion que inicia las señales de los objetos
        """
        self.ui.aceptar_bt.clicked.connect(self.guardar)
        self.ui.cancelar_bt.clicked.connect(self.cancelar)

    def cancelar(self):
        self.reject()

    def guardar(self):
        print "hola hola"
        print self.editado
        """
        Función que guarda los cambios hechos en la tabla de clientes. La forma
        de guardar dependerá si el formulario se usó para editar o para agregar
        un nuevo producto
        """
        if(self.editado):
            manejo_bd_clientes.editar_cliente(
                unicode(self.ui.linea_nombre.text()),
                unicode(self.ui.linea_apellido.text()),
                unicode(self.ui.linea_telefono.text()),
                unicode(self.ui.linea_cliente.text()),
                unicode(self.ui.linea_rut.text()))
        else:
            manejo_bd_clientes.agregar_cliente(
                unicode(self.ui.linea_nombre.text()),
                unicode(self.ui.linea_apellido.text()),
                unicode(self.ui.linea_telefono.text()),
                unicode(self.ui.linea_cliente.text()),
                unicode(self.ui.linea_rut.text()))
        self.reject()

    def editar(self, rut):
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
        telefono = unicode(datos[3])
        correo = unicode(datos[4])
       
        

        self.ui.linea_rut.setText(rut)
        self.ui.linea_nombre.setText(nombres)
        self.ui.linea_apellido.setText(apelldos)
        self.ui.linea_telefono.setText(telefono)
        self.ui.linea_cliente.setText(correo)
    
    
        
        

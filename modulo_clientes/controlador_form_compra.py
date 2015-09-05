#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PySide import QtGui, QtCore
from Formulario_venta import Ui_dialog
import manejo_bd_clientes

class Display(QtGui.QDialog):

    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.ui =  Ui_dialog()
        self.editado = False
        self.nombre = ""
        self.apellido= ""
        self.ui.setupUi(self)
        self.cargar_datos()
        self.iniciar_botones()
        self.Rut_cliente = ""
    def cargar_datos(self,modelos=None):
        if (modelos == None):
            modelos = manejo_bd_clientes.obtener_modelos()
        #Creamos el modelo asociado a la tabla
        self.data = QtGui.QStandardItemModel(len(modelos)+1, 10)
        self.data.setHorizontalHeaderItem(
            0, QtGui.QStandardItem(u"modelo"))
        self.data.setHorizontalHeaderItem(
            1, QtGui.QStandardItem(u"Marca"))
        self.data.setHorizontalHeaderItem(
            2, QtGui.QStandardItem(u"motor"))
        self.data.setHorizontalHeaderItem(
            3, QtGui.QStandardItem(u"peso"))
        self.data.setHorizontalHeaderItem(
            4, QtGui.QStandardItem(u"rendimiendo"))
        self.data.setHorizontalHeaderItem(
            5, QtGui.QStandardItem(u"Ventas"))
        self.data.setHorizontalHeaderItem(
            6, QtGui.QStandardItem(u"fecha_creacion"))
        self.data.setHorizontalHeaderItem(
            7, QtGui.QStandardItem(u"descripcion"))
        self.data.setHorizontalHeaderItem(
            8, QtGui.QStandardItem(u"precio_lista"))

        for r, row in enumerate(modelos):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['modelo'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['Marca'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['motor'])
            index = self.data.index(r, 3, QtCore.QModelIndex())
            self.data.setData(index, row['peso'])
            index = self.data.index(r, 4, QtCore.QModelIndex())
            self.data.setData(index, row['rendimiendo'])
            index = self.data.index(r, 5, QtCore.QModelIndex())
            self.data.setData(index, row['Ventas'])
            index = self.data.index(r, 6, QtCore.QModelIndex())
            self.data.setData(index, row['fecha'])
            index = self.data.index(r, 7, QtCore.QModelIndex())
            self.data.setData(index, row['descripcion'])
            index = self.data.index(r, 8, QtCore.QModelIndex())
            self.data.setData(index, row['precio_lista'])

        self.ui.tableView.setModel(self.data)

        self.ui.tableView.horizontalHeader().setResizeMode(
            0, self.ui.tableView.horizontalHeader().Stretch)
        self.ui.tableView.horizontalHeader().setResizeMode(
            7, self.ui.tableView.horizontalHeader().Stretch)

        self.ui.tableView.setColumnWidth(0, 100)
        self.ui.tableView.setColumnWidth(7, 210)
       


    def iniciar_botones(self):
        """
        Funcion que inicia las señales de los objetos
        """
        self.ui.VenderButton.clicked.connect(self.comprar)
        self.ui.CancelarButton.clicked.connect(self.cancelar)

    def cancelar(self):
        self.reject()

    def comprar(self):
        color, patente = self.obtener_datos()
        model = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        if index.row() == -1: #No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        elif (color!="" and patente!="" ):
            try:
                self.reject()
                modelo_auto= model.index(index.row(), 0, QtCore.QModelIndex()).data()
                manejo_bd_clientes.realizar_venta(color,patente,modelo_auto,self.Rut_cliente)
                self.accepted.emit()
                self.alerta("compra realizada")
                self.close()
            except Exception,e:
                print (e)
                self.alerta("ERROR, no se pudo efectuar compra!")
                self.close()
        else:
            self.alerta("Faltan datos por agregar."
                        "Complete todos los campos.")


        
            

    def rellenar(self, rut):
        print rut
        self.Rut_cliente=rut
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

    def obtener_datos(self):
        """
        Obtiene los datos colocados por el usuario
        en el formulario
        """
        color = self.ui.lineEdit.text()
        patente = self.ui.lineEdit_2.text()
        
        
        return (color,patente)


    def alerta(self, msje):
        """
        Genera un diálogo informativo. (ventana pop-up)
        """
        msgBox = QtGui.QMessageBox()
        msgBox.setText(msje)
        msgBox.exec_()
       
    

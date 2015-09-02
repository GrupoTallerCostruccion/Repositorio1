#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from tabla_clientes import Ui_Form
import manejo_bd_clientes
import controlador_form_compra
from controlador_formulario_registro import Display
import form_registro

class Main(QtGui.QMainWindow):

    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.ui =  Ui_Form()
        self.ui.setupUi(self)
        
        self.iniciar_botones()
        self.cargar_datos("")
        self.show()

    def cargar_datos(self, text):
        """
        Función que se encarga de mostrar la tabla clientes,
        """
        
        cliente= manejo_bd_clientes.obtener_clientes()
        self.model = QtGui.QStandardItemModel(len(cliente), 5)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Rut"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Nombre"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Apellido"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"Telefono"))
        self.model.setHorizontalHeaderItem(4, QtGui.QStandardItem(u"Correo"))
        self.model.setHorizontalHeaderItem(5, QtGui.QStandardItem(
            u"Autos Comprados"))
   
        r = 0
        for row in cliente:
            index = self.model.index(r, 0, QtCore.QModelIndex())
            self.model.setData(index, row['rut'])
            index = self.model.index(r, 1, QtCore.QModelIndex())
            self.model.setData(index, row['nombre'])
            index = self.model.index(r, 2, QtCore.QModelIndex())
            self.model.setData(index, row['apellido'])
            index = self.model.index(r, 3, QtCore.QModelIndex())
            self.model.setData(index, row['telefono'])
            index = self.model.index(r, 4, QtCore.QModelIndex())
            self.model.setData(index, row['correo'])
            index = self.model.index(r, 5, QtCore.QModelIndex())
            self.model.setData(index, row['Autos Comprados'])
            r=r+1
        self.ui.tableView.setModel(self.model)

        self.ui.tableView.setColumnWidth(0, 50)
        self.ui.tableView.setColumnWidth(1, 65)
        self.ui.tableView.setColumnWidth(2, 200)
        self.ui.tableView.setColumnWidth(3, 150)
        self.ui.tableView.setColumnWidth(4, 150)
        self.ui.tableView.setColumnWidth(5, 100)


    def eliminar_cliente(self):
        """
        Función que elimina un cliente de la tabla
        """
        model = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        if index.row() == -1:
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            self.resp = QtGui.QMessageBox.question(
                self,"Borrar",
                "Seguro deseas borrar este Cliente?",
                QtGui.QMessageBox.Yes,
                QtGui.QMessageBox.No);
            
            if self.resp == QtGui.QMessageBox.Yes:
                rut = model.index(index.row(), 0, QtCore.QModelIndex()).data()
                if (manejo_bd_clientes.eliminar_cliente(rut)):
                  
                    self.cargar_datos("")
                    return True
                else:
                    self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                    self.ui.errorMessageDialog.showMessage("Error al eliminar el cliente")
                    return False

    def editar_cliente(self):
        """
        Función que permite editar un producto de la tabla de productos. Para
        poder editar un producto es necesario haber seleccionado una fila. Una
        vez presionado el botón, se abrirá el formulario cargado con los datos
        del cliente
        """
        model = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        if index.row() == -1: #No se ha seleccionado una fila
            rut = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            print rut
            formulario = controlador_formulario_registro.Display(self)
            formulario.exec_()
            self.cargar_datos("")
        else:
            rut = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            print rut
            formulario = Display(self)
            formulario.editar(rut)
            formulario.exec_()
            self.cargar_datos("")

    def iniciar_botones(self):
        """
        Función que se encarga de cargar todas las señales de los objetos.
        """
        self.ui.btn_eliminar.clicked.connect(self.eliminar_cliente)
        self.ui.btn_editar.clicked.connect(self.editar_cliente)
        self.ui.btn_agregar.clicked.connect(self.agregar_cliente)
        self.ui.btn_compra.clicked.connect(self.realizar_compra)


    def agregar_cliente(self):
        formulario = Display(self)
        formulario.exec_()
        self.cargar_datos("")

        
    def realizar_compra(self):
        model = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        if index.row() == -1: #No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage("Debe seleccionar una fila")
            return False
        else:
            rut = model.index(index.row(), 0, QtCore.QModelIndex()).data()
            print rut
            formulario = controlador_form_compra.Display(self)
            formulario.rellenar(rut)
            formulario.exec_()
            self.cargar_datos("")


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())










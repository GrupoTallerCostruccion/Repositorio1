#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from ui import Ui_MainWindow
import model_marca as db_marcas
from ctrl_form import FormMarca


class Main(QtGui.QMainWindow):
    """
    Lanza la grilla principa
    """
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.load_data()
        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.ui.agregar_marca.clicked.connect(self.agregar)
        self.ui.edtar_marca.clicked.connect(self.edit)
        self.ui.eliminar_marca.clicked.connect(self.delete)

    def load_data(self):
        """
        Función que carga la información de marcas en la grilla
        incluyendo la cantidad de modelos asociados a la marca
        """
        print "load data.."
        marcas = db_marcas.obtener_marcas()
        #Creamos el modelo asociado a la tabla
        self.data = QtGui.QStandardItemModel(len(marcas)+1, 3)
        self.data.setHorizontalHeaderItem(
            0, QtGui.QStandardItem("Nombre de Marca"))
        self.data.setHorizontalHeaderItem(
            1, QtGui.QStandardItem("Pais de Origen"))
        self.data.setHorizontalHeaderItem(
            2, QtGui.QStandardItem(u"Cantidad de Modelos"))

        for r, row in enumerate(marcas):
            index = self.data.index(r, 0, QtCore.QModelIndex())
            self.data.setData(index, row['Nombre de Marca'])
            index = self.data.index(r, 1, QtCore.QModelIndex())
            self.data.setData(index, row['Pais de Origen'])
            index = self.data.index(r, 2, QtCore.QModelIndex())
            self.data.setData(index, row['Cantidad de Modelos'])

        self.ui.tabla_marcas.setModel(self.data)

        # Para que las columnas 1 y 2 se estire o contraiga cuando
        # se cambia el tamaño de la pantalla
        self.ui.tabla_marcas.horizontalHeader().setResizeMode(
            0, self.ui.tabla_marcas.horizontalHeader().Stretch)
        self.ui.tabla_marcas.horizontalHeader().setResizeMode(
            1, self.ui.tabla_marcas.horizontalHeader().Stretch)

        self.ui.tabla_marcas.setColumnWidth(0, 100)
        self.ui.tabla_marcas.setColumnWidth(1, 210)
        self.ui.tabla_marcas.setColumnWidth(2, 210)

    def delete(self):
        """
        Función que borra un alumno de la base de datos e
        indica el resultado de la operación
        """
        data = self.ui.tabla_marcas.model()
        index = self.ui.tabla_marcas.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
            self.resp = QtGui.QMessageBox.question(
                self,"Borrar",
                "Deseas borrar esta marca?",
                QtGui.QMessageBox.Yes,
                QtGui.QMessageBox.No);
            
            if self.resp == QtGui.QMessageBox.Yes:
                marca = data.index(
                    index.row(), 0, QtCore.QModelIndex()).data()
                if (db_marcas.borrar(marca)):
                    self.load_data()
                    msgBox = QtGui.QMessageBox()
                    msgBox.setText(u"EL registro fue eliminado.")
                    msgBox.exec_()
                    return True
                else:
                    self.ui.errorMessageDialog = QtGui.QErrorMessage(self)
                    self.ui.errorMessageDialog.showMessage(
                        u"Error al eliminar el registro")
                    return False
                self.load_data()

    def agregar(self):
        """
        Agrega/edita una marca. Llama al formulario correspondiente
        """
        self.ui.form = FormMarca(self) ##
        self.ui.form.accepted.connect(self.load_data)
        #self.ui.form.rejected.connect(self.load_data)
        self.ui.form.show()

        
    def edit(self):
        """
        Función obtiene el alumno seleccionado en la grilla
        para poner sus datos en el formulario para su edición
        """
        data = self.ui.tabla_marcas.model()
        index = self.ui.tabla_marcas.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
            nom_marca = data.index(index.row(), 0, QtCore.QModelIndex()).data()
            self.ui.form = FormMarca(self, nom_marca)
            self.ui.form.accepted.connect(self.load_data)
            self.ui.form.show()
        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

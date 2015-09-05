#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PySide import QtGui, QtCore
from tabla_modelos import Ui_Dialog
import modelo_conector as db
from ctrl_form import FormModelo


class Main(QtGui.QMainWindow):
    """
    Esta es una grilla
    """
    def __init__(self,parent=None):
        super(Main, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.load_data()
        self.connect_signals()
        self.show()

    def connect_signals(self):
        self.ui.btn_agregar.clicked.connect(self.add)
        self.ui.btn_editar.clicked.connect(self.editar)
        self.ui.btn_borrar.clicked.connect(self.delete)
        self.ui.buscar.textChanged[str].connect(self.filtrar_modelos)

    def add(self):
        self.ui.form = FormModelo(self)
        self.ui.form.accepted.connect(self.load_data)
        self.ui.form.show()
        pass

    def filtrar_modelos(self,busqueda):
        """
        Filtra la busqueda de modelos ingresado en el lineEdit
        """
        mod = db.buscar_modelos(busqueda)
        self.load_data(mod)
        

    def load_data(self, modelos= None):
        """
        Función que carga la información de modelos en la grilla
        incluyendo la cantidad de modelos asociados a la marca
        """
        if (modelos == None):
            modelos = db.obtener_modelos()
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
        self.data = self.ui.tableView.selectionModel()
        self.data.currentChanged.connect(self.cambiaFila)

    def delete(self):
        """
        Función que intenta borrar un alumno de la base de datos e
        indica el resultado de la operación
        """

        data = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
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
                if (db.borrar_elemento("modelo","modelo",marca)):
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

    def cambiaFila(self,index,indexp):
        model = self.ui.tableView.model()
        ind = model.index(index.row(), 0, QtCore.QModelIndex()).data()
        auto = db.obtenerAutoMod(ind)
        url = str(auto[0]['imagen'])
        print url
        pmap = QtGui.QPixmap(url)
        pmap = pmap.scaled(250,200,QtCore.Qt.KeepAspectRatio)
        self.ui.foto.setPixmap(pmap)
        #self.ui.descripcion.setText(str(auto[0]['descripcion']))

    ########### rehacer..
    def editar(self):
        """
        Función obtiene el alumno seleccionado en la grilla
        para poner sus datos en el formulario para su edición
        """
        data = self.ui.tableView.model()
        index = self.ui.tableView.currentIndex()
        if index.row() == -1:  # No se ha seleccionado una fila
            self.errorMessageDialog = QtGui.QErrorMessage(self)
            self.errorMessageDialog.showMessage(u"Debe seleccionar una fila")
            return False
        else:
            nom_marca = data.index(index.row(), 0, QtCore.QModelIndex()).data()
            self.ui.form = FormModelo(self, nom_marca)
            self.ui.form.accepted.connect(self.load_data)
            self.ui.form.show()
        


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())

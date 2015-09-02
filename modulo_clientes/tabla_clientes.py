# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tabla_clientes.ui'
#
# Created: Wed Sep 02 17:42:01 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(560, 362)
        self.tableView = QtGui.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(20, 40, 521, 261))
        self.tableView.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableView.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableView.setObjectName("tableView")
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 16))
        self.label.setObjectName("label")
        self.frame = QtGui.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(112, 310, 431, 43))
        self.frame.setFrameShape(QtGui.QFrame.Panel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtGui.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_agregar = QtGui.QPushButton(self.frame)
        self.btn_agregar.setObjectName("btn_agregar")
        self.horizontalLayout.addWidget(self.btn_agregar)
        self.btn_editar = QtGui.QPushButton(self.frame)
        self.btn_editar.setObjectName("btn_editar")
        self.horizontalLayout.addWidget(self.btn_editar)
        self.btn_eliminar = QtGui.QPushButton(self.frame)
        self.btn_eliminar.setObjectName("btn_eliminar")
        self.horizontalLayout.addWidget(self.btn_eliminar)
        self.btn_compra = QtGui.QPushButton(self.frame)
        self.btn_compra.setObjectName("btn_compra")
        self.horizontalLayout.addWidget(self.btn_compra)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Tabla Clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_agregar.setText(QtGui.QApplication.translate("Form", "Agregar Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_editar.setText(QtGui.QApplication.translate("Form", "Editar Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_eliminar.setText(QtGui.QApplication.translate("Form", "Eliminar Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_compra.setToolTip(QtGui.QApplication.translate("Form", "Seleccione cliente en la tabla para efectuar compra de un auto", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_compra.setText(QtGui.QApplication.translate("Form", "Hacer Compra", None, QtGui.QApplication.UnicodeUTF8))


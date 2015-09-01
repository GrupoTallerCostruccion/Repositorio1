# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '1.ui'
#
# Created: Tue Sep  1 04:23:18 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(525, 362)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.linea_rut = QtGui.QLineEdit(Dialog)
        self.linea_rut.setObjectName("linea_rut")
        self.verticalLayout.addWidget(self.linea_rut)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.linea_nombre = QtGui.QLineEdit(Dialog)
        self.linea_nombre.setObjectName("linea_nombre")
        self.verticalLayout.addWidget(self.linea_nombre)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.linea_apellido = QtGui.QLineEdit(Dialog)
        self.linea_apellido.setObjectName("linea_apellido")
        self.verticalLayout.addWidget(self.linea_apellido)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.linea_telefono = QtGui.QLineEdit(Dialog)
        self.linea_telefono.setText("")
        self.linea_telefono.setObjectName("linea_telefono")
        self.verticalLayout.addWidget(self.linea_telefono)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.linea_cliente = QtGui.QLineEdit(Dialog)
        self.linea_cliente.setObjectName("linea_cliente")
        self.verticalLayout.addWidget(self.linea_cliente)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelar_bt = QtGui.QPushButton(Dialog)
        self.cancelar_bt.setObjectName("cancelar_bt")
        self.horizontalLayout.addWidget(self.cancelar_bt)
        self.aceptar_bt = QtGui.QPushButton(Dialog)
        self.aceptar_bt.setObjectName("aceptar_bt")
        self.horizontalLayout.addWidget(self.aceptar_bt)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Rut de Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Nombres del Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Apellidos del Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Teléfono del Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Correo del Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar_bt.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.aceptar_bt.setText(QtGui.QApplication.translate("Dialog", "Aceptar", None, QtGui.QApplication.UnicodeUTF8))


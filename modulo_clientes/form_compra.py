# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form_compra.ui'
#
# Created: Tue Sep  1 01:25:27 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(669, 472)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nom_cliente = QtGui.QLineEdit(Dialog)
        self.nom_cliente.setEnabled(False)
        self.nom_cliente.setObjectName("nom_cliente")
        self.gridLayout.addWidget(self.nom_cliente, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 3, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.cancelar_bt = QtGui.QPushButton(Dialog)
        self.cancelar_bt.setObjectName("cancelar_bt")
        self.horizontalLayout.addWidget(self.cancelar_bt)
        self.comprar_bt = QtGui.QPushButton(Dialog)
        self.comprar_bt.setObjectName("comprar_bt")
        self.horizontalLayout.addWidget(self.comprar_bt)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.nom_cliente.setText(QtGui.QApplication.translate("Dialog", "Nombre cliente sin modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Seleccione auto", None, QtGui.QApplication.UnicodeUTF8))
        self.cancelar_bt.setText(QtGui.QApplication.translate("Dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.comprar_bt.setText(QtGui.QApplication.translate("Dialog", "Comprar", None, QtGui.QApplication.UnicodeUTF8))


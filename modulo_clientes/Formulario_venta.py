# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Formulario_venta.ui'
#
# Created: Sat Sep  5 03:37:18 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(574, 501)
        self.gridLayout = QtGui.QGridLayout(dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.CancelarButton = QtGui.QPushButton(dialog)
        self.CancelarButton.setObjectName("CancelarButton")
        self.horizontalLayout.addWidget(self.CancelarButton)
        self.VenderButton = QtGui.QPushButton(dialog)
        self.VenderButton.setObjectName("VenderButton")
        self.horizontalLayout.addWidget(self.VenderButton)
        self.gridLayout.addLayout(self.horizontalLayout, 11, 1, 1, 1)
        self.lineEdit = QtGui.QLineEdit(dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 7, 1, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(dialog)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 8, 1, 1, 1)
        self.LabelColor = QtGui.QLabel(dialog)
        self.LabelColor.setTextFormat(QtCore.Qt.PlainText)
        self.LabelColor.setMargin(9)
        self.LabelColor.setObjectName("LabelColor")
        self.gridLayout.addWidget(self.LabelColor, 7, 0, 1, 1)
        self.label_4 = QtGui.QLabel(dialog)
        self.label_4.setMargin(9)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 8, 0, 1, 1)
        self.tableView = QtGui.QTableView(dialog)
        self.tableView.setMinimumSize(QtCore.QSize(550, 280))
        self.tableView.setObjectName("tableView")
        self.gridLayout.addWidget(self.tableView, 3, 0, 1, 2)
        self.label = QtGui.QLabel(dialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.nom_cliente = QtGui.QLineEdit(dialog)
        self.nom_cliente.setEnabled(False)
        self.nom_cliente.setObjectName("nom_cliente")
        self.gridLayout.addWidget(self.nom_cliente, 1, 0, 1, 2)
        self.label_2 = QtGui.QLabel(dialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QtGui.QApplication.translate("dialog", "Formulario venta", None, QtGui.QApplication.UnicodeUTF8))
        self.CancelarButton.setText(QtGui.QApplication.translate("dialog", "Cancelar", None, QtGui.QApplication.UnicodeUTF8))
        self.VenderButton.setText(QtGui.QApplication.translate("dialog", "Vender", None, QtGui.QApplication.UnicodeUTF8))
        self.LabelColor.setText(QtGui.QApplication.translate("dialog", "Color", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("dialog", "Patente", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dialog", "Cliente", None, QtGui.QApplication.UnicodeUTF8))
        self.nom_cliente.setText(QtGui.QApplication.translate("dialog", "Nombre cliente sin modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dialog", "Seleccione algun modelo de la lista.", None, QtGui.QApplication.UnicodeUTF8))


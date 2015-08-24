# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin_marcas.ui'
#
# Created: Mon Aug 24 02:59:00 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 386)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pais_marca = QtGui.QLineEdit(self.centralwidget)
        self.pais_marca.setObjectName("pais_marca")
        self.gridLayout.addWidget(self.pais_marca, 5, 0, 1, 1)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nombre_marca = QtGui.QLineEdit(self.centralwidget)
        self.nombre_marca.setObjectName("nombre_marca")
        self.gridLayout.addWidget(self.nombre_marca, 3, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.agregar_marca = QtGui.QPushButton(self.centralwidget)
        self.agregar_marca.setObjectName("agregar_marca")
        self.gridLayout.addWidget(self.agregar_marca, 6, 0, 1, 1)
        self.tabla_marcas = QtGui.QTableWidget(self.centralwidget)
        self.tabla_marcas.setObjectName("tabla_marcas")
        self.tabla_marcas.setColumnCount(0)
        self.tabla_marcas.setRowCount(0)
        self.gridLayout.addWidget(self.tabla_marcas, 1, 0, 1, 1)
        self.eliminar_marca = QtGui.QPushButton(self.centralwidget)
        self.eliminar_marca.setObjectName("eliminar_marca")
        self.gridLayout.addWidget(self.eliminar_marca, 7, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 620, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pais_marca.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>País de Origen</p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "MARCAS", None, QtGui.QApplication.UnicodeUTF8))
        self.nombre_marca.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>Nombre de Marca</p><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Nombre de la Marca de Automóviles(*)", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "País de Origen(*)", None, QtGui.QApplication.UnicodeUTF8))
        self.agregar_marca.setText(QtGui.QApplication.translate("MainWindow", "Agregar/Editar Marca", None, QtGui.QApplication.UnicodeUTF8))
        self.eliminar_marca.setText(QtGui.QApplication.translate("MainWindow", "Eliminar Marca", None, QtGui.QApplication.UnicodeUTF8))


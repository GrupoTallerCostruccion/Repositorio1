# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MenuPrincipal.ui'
#
# Created: Fri Sep  4 15:36:26 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(421, 411)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.labeltitulo = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labeltitulo.setFont(font)
        self.labeltitulo.setObjectName("labeltitulo")
        self.gridLayout.addWidget(self.labeltitulo, 0, 2, 1, 1)
        self.BotonClientes = QtGui.QPushButton(self.centralwidget)
        self.BotonClientes.setObjectName("BotonClientes")
        self.gridLayout.addWidget(self.BotonClientes, 3, 0, 1, 4)
        self.BotonMarcas = QtGui.QPushButton(self.centralwidget)
        self.BotonMarcas.setObjectName("BotonMarcas")
        self.gridLayout.addWidget(self.BotonMarcas, 4, 0, 1, 4)
        self.BotonModelos = QtGui.QPushButton(self.centralwidget)
        self.BotonModelos.setObjectName("BotonModelos")
        self.gridLayout.addWidget(self.BotonModelos, 7, 0, 1, 4)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 0, 3, 1, 1)
        self.graphicsView = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 1, 1, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.labeltitulo.setText(QtGui.QApplication.translate("MainWindow", "MENU", None, QtGui.QApplication.UnicodeUTF8))
        self.BotonClientes.setText(QtGui.QApplication.translate("MainWindow", "ventas/gention clientes", None, QtGui.QApplication.UnicodeUTF8))
        self.BotonMarcas.setText(QtGui.QApplication.translate("MainWindow", "gention marcas de vehiculo", None, QtGui.QApplication.UnicodeUTF8))
        self.BotonModelos.setText(QtGui.QApplication.translate("MainWindow", "gention modelos", None, QtGui.QApplication.UnicodeUTF8))


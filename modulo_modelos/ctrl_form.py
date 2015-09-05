#!/usr/bin/python
# -*- coding: utf-8 -*-
from PySide import QtGui
from form_modelo import Ui_Dialog
import modelo_conector as model

class FormModelo(QtGui.QDialog):

    def __init__(self, parent=None, nombre=None):
        """
        Formulario para crear y editar alumnos.
        Si se recibe la var rut
        entonces se está en modo de edición.
        """
        super(FormModelo, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.nom_orig = nombre
        if nombre is None:
            self.ui.btn_guardar.clicked.connect(self.crear_Modelo)
        else:
            self.colocar_datos(nombre)
            self.ui.btn_guardar.clicked.connect(self.editar_Modelo)
        

    def colocar_datos(self, nombre):
        """
        Coloca los datos de la Modelo en los widgets
        para su edición
        """
        Modelo = model.obtener_modelo(nombre)
        
        self.ui.modelo.setText(Modelo["modelo"])
        self.ui.motor.setText(Modelo["motor"])
        self.ui.peso.setText(Modelo["peso"])
        self.ui.precio.setText(Modelo["precio_lista"])
        self.ui.rendim.setText(Modelo["rendimiendo"])
        self.ui.fecha.setText(Modelo["fecha_creacion"])
        self.ui.imagen.setText(Modelo["imagen"])
        self.ui.textEdit.setText(Modelo[descripcion])
        self.ui.marca.setText(Modelo[Marca])

    def obtener_datos(self):
        """
        Obtiene los datos colocados por el usuario
        en el formulario
        """
        marca = self.ui.marca.text()
        modelo = self.ui.modelo.text()
        motor = self.ui.motor.text()
        peso = self.ui.peso.text()
        precio = self.ui.precio.text()
        rendim = self.ui.rendim.text()
        fecha = self.ui.fecha.text()
        imagen = self.ui.imagen.text()
        descrip = self.ui.textEdit.toPlainText()
        
        return (marca,modelo,motor,peso,precio,rendim,fecha,
                imagen,descrip)

    def crear_Modelo(self):
        mar,mod,mot,pes,precio,rend,fec,img,descrip = self.obtener_datos()
        if (mar!="" and mod!="" and mot!="" and pes!="" and
            precio!="" and rend !="" and fec!="" and img!=""):
            try:
                model.crear_Modelo(
                    mar,mod,mot,pes,precio,rend,fec,img,descrip)
                self.accepted.emit()
                self.alerta("Modelo Creada")
                self.close()
            except Exception,e:
                print (e)
                self.alerta("ERROR, Modelo no pudo ser guardada!")
                self.close()
        else:
            self.alerta("Faltan datos por agregar."
                        "Complete todos los campos.")

    def alerta(self, msje):
        """
        Genera un diálogo informativo. (ventana pop-up)
        """
        msgBox = QtGui.QMessageBox()
        msgBox.setText(msje)
        msgBox.exec_()
            
    def editar_Modelo(self):
        """
        Extrae datos ingresados en el formulario.
        Edita la Modelo seleccionada
        """
        marca,modelo,motor,peso,precio,
        rendim,fecha,imagen,descrip = self.obtener_datos()
        try:
            model.editar_Modelo(self.nom_orig, nombre, pais)
            self.accepted.emit()
            self.alerta("Modelo Editado.")
            self.close()
        except Exception,e:
            print (e)
            self.alerta("ERROR, Modelo no pudo ser editado!")
            self.close()
            pass


from PySide import QtGui
from form_marca import Ui_Dialog
import model_marca as model

class FormMarca(QtGui.QDialog):

    def __init__(self, parent=None, nombre=None):
        """
        Formulario para crear y editar alumnos.
        Si se recibe la var rut
        entonces se está en modo de edición.
        """
        super(FormMarca, self).__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.nom_orig = nombre
        if nombre is None:
            self.ui.btn_guardar.clicked.connect(self.crear_marca)
            self.ui.info_modo.setText(u"Modo creación de Marca")
        else:
            self.colocar_datos(nombre)
            self.ui.btn_guardar.clicked.connect(self.editar_marca)
            self.ui.info_modo.setText(u"Modo Edición de Marca")
        

    def colocar_datos(self, nombre):
        """
        Coloca los datos de la marca en los widgets
        para su edición
        """
        marca = model.obtener_marca(nombre)
        self.ui.campo_nombre.setText(marca["nombre"])
        self.ui.campo_pais.setText(marca["pais"])

    def obtener_datos(self):
        """
        Obtiene los datos colocados por el usuario
        en el formulario
        """
        nombre = self.ui.campo_nombre.text()
        pais = self.ui.campo_pais.text()
        return (nombre,pais)

    def crear_marca(self):
        nombre,pais = self.obtener_datos()
        try:
            model.crear_marca(nombre,pais)
            self.accepted.emit()
            self.alerta("Marca Creada")
            self.close()
        except Exception,e:
            print (e)
            self.alerta("ERROR, marca no pudo ser guardada!")
            self.close()

    def alerta(self, msje):
        """
        Genera un diálogo informativo. (ventana pop-up)
        """
        msgBox = QtGui.QMessageBox()
        msgBox.setText(msje)
        msgBox.exec_()
            
    def editar_marca(self):
        """
        Extrae datos ingresados en el formulario.
        Edita la marca seleccionada
        """
        nombre,pais = self.obtener_datos()
        try:
            model.editar_marca(self.nom_orig, nombre, pais)
            self.accepted.emit()
            self.alerta("Marca Editada.")
            self.close()
        except Exception,e:
            print (e)
            self.alerta("ERROR, marca no pudo ser editada!")
            self.close()
            pass

from  PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QTextOption ,QPalette,QPainter, QColor, QPen, QBrush, QImage,QPixmap
from qt_for_python.uic.ui_guiciber import *
import sys
import test as tt

class ventana (QMainWindow):
    def __init__(self,modelo):
        super().__init__()
        self.ui = Ui_IA()
        self.ui.setupUi(self)
        self.modelo=modelo
        self.controlador=Controlador(self)
        self.canvas=Canvas(self.ui.contenedorlienzo)
    
    def Get_modelo(self):
        return self.modelo

    def Get_Canvas (self):
        return self.canvas


class Canvas(QScrollArea):
    def __init__(self,parent):
        super().__init__(parent=parent)
        self.resize(parent.width(), parent.height())
        self.dibujar =False
        self.label =QLabel()
        self.label.resize(self.width(), self.height())
      
    def Set_image(self,valor):
        self.image =valor

    def is_dibujar(self):
        return self.dibujar

    def Dibujar(self,urlimage):
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setWidgetResizable(True)
        self.image= QPixmap(urlimage)
        self.label.resize(self.image.width(), self.image.height())
        self.label.setPixmap(self.image)
        self.setWidget(self.label)
        
        
class Controlador:

    def __init__(self,ventana):
        self.ventana =ventana
        self.Eventos()

    def Eventos(self):
        self.ventana.ui.botonCargar.clicked.connect(lambda: self.ventana.Get_modelo().Cargar())
        self.ventana.ui.botonEvaluar.clicked.connect(lambda :self.ventana.Get_modelo().Evaluar())

class Modelo:
    def __init__(self):
        self.ventana = ventana(self)
        self.url=""

    def Cargar(self):
        archivo  = QFileDialog.getOpenFileName(self.ventana,"Abrir Archivo",'C:\\','All files (*)')
        self.url=archivo[0]
        self.ventana.Get_Canvas().Dibujar(self.url)

    def Evaluar(self):
        try:
            tt.predict(self.url)
        except: 
            print("medi funciona")
            
    def Get_ventana(self):
        return self.ventana


if __name__ =="__main__":
    app =QApplication(sys.argv)
    gui = Modelo().Get_ventana()
    gui.show()
    sys.exit(app.exec_())

    

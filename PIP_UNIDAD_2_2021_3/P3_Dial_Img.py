import sys

from PyQt5 import uic, QtWidgets, QtGui

qtCreatorFile = "P3_Dial_Img.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.dial.setMinimum(0)
        self.dial.setMaximum(4)
        self.dial.setSingleStep(1)

        self.dial.setValue(0)
        #self.txt_valor.setText("0")

        self.dial.valueChanged.connect(self.valorCambio)

        self.diccionario = {}
        self.diccionario[0] = ["Jorge", "ISC", "Imagenes/Main_Jorge.jpg"]
        self.diccionario[1] = ["Alan", "IC", "Imagenes/Main_Alan.jpg"]
        self.diccionario[2] = ["Juan", "ISC", "Imagenes/Main_Juan.jpg"]
        self.diccionario[3] = ["Francisco", "II", "Imagenes/Main_Javier.jpg"]
        self.diccionario[4] = ["CR7", "IM", "Imagenes/Main_CR7.jpg"]

        alumno = self.diccionario[0]
        self.txt_valor.setText(alumno[0])

        self.txt_img.setPixmap(QtGui.QPixmap(alumno[2]))

        #Tarea: Recrear el ejerccio con Las imagenes de los integrantes del equipo o
        #cualquier tipo de personajes ficticios. Minimo 5 Personajes

    #area de slots
    def valorCambio(self):
        valor = self.dial.value()   ##int
        print(valor)

        #valor = str(valor)
        #self.txt_valor.setText(valor)

        alumno = self.diccionario[valor]

        self.txt_valor.setText(alumno[0])
        print(alumno[1])

        self.txt_img.setPixmap(QtGui.QPixmap(alumno[2]))

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
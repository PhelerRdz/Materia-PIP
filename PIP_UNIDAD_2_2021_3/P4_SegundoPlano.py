import sys
from PyQt5 import uic, QtWidgets, QtGui, QtCore
qtCreatorFile = "P4_SegundoPlano.ui"
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

        print("Total Elementos Diccionariio: "  + str(len(self.diccionario)))

        #########################################
        self.btn_iniciar.clicked.connect(self.iniciar)
        self.btn_reiniciar.clicked.connect(self.reiniciar)
        #########################################

        self.SegundoPlano = QtCore.QTimer()
        self.SegundoPlano.timeout.connect(self.actualizaImagen)


    #area de slots
    def actualizaImagen(self):
        valor_actual = self.dial.value()  ##int
        fin = len(self.diccionario)
        print(valor_actual)
        alumno = self.diccionario[valor_actual]
        self.txt_valor.setText(alumno[0])
        self.txt_img.setPixmap(QtGui.QPixmap(alumno[2]))
        self.dial.setValue(valor_actual+1)
        if valor_actual + 1 == fin:
            self.SegundoPlano.stop()

    def iniciar(self):
        self.SegundoPlano.start(1000)

    def reiniciar(self):
        self.dial.setValue(0)
        valor_actual = self.dial.value()
        alumno = self.diccionario[valor_actual]
        self.txt_valor.setText(alumno[0])
        self.txt_img.setPixmap(QtGui.QPixmap(alumno[2]))

    def valorCambio(self):
        valor = self.dial.value()
        print(valor)
        alumno = self.diccionario[valor]
        self.txt_valor.setText(alumno[0])
        print(alumno[1])
        self.txt_img.setPixmap(QtGui.QPixmap(alumno[2]))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
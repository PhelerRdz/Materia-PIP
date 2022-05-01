import sys

from PyQt5 import uic, QtWidgets

qtCreatorFile = "P3_SaludoNombre_V2.ui" # Nombre del archivo aquí.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.btn_enviar.clicked.connect(self.saludar)


    # Área de los Slots
    def saludar(self):
        print("Hiciste clic!")

        nombre = self.txt_nombre.text()
        #print(nombre)

        #self.mensaje("Saludos " + nombre + " :D!")

        self.txt_resultado.setText("Hi, " + nombre)

    def mensaje(self,msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
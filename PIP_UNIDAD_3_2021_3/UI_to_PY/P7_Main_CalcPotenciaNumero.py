import sys

from PyQt5 import uic, QtWidgets, QtCore

from UI_to_PY import P7_CalcPotenciaNumero as interfaz

class MyApp(QtWidgets.QMainWindow, interfaz.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        interfaz.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.btn_calcular.clicked.connect(self.calcular)

    def calcular(self):
        numero = int(self.txt_numero.text())
        exponente = int(self.txt_exponente.text())

        potencia = numero ** exponente
        print("Potencia: ", potencia)

        self.txt_resultado.setText(str(potencia))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
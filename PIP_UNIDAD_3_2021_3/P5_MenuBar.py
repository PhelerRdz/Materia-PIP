import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P5_MenuBar.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        #SOLO PARA QACTION  ...
        self.actionAbrir_Widget_2.triggered.connect(self.widget)
        self.actionAbrir_Dialog_2.triggered.connect(self.dialog)
        self.actionSalir.triggered.connect(self.salir)
        self.actionAcerca.triggered.connect(self.acerca)

    def widget(self):
        self.mensaje("Abriste un Widget")

    def dialog(self):
        self.mensaje("Abriste un Dialog")

    def salir(self):
        sys.exit()

    def acerca(self):
        self.mensaje("Acerca de ♥")

    def mensaje(self, msj):
        m = QtWidgets.QMessageBox()
        m.setText(msj)
        m.exec_()

#PRÁCTICA 1. REALIZAR LA UTILIZACIÓN DE AL MENOS DOS DE LOS TRES ELEMENTOS Combo, List widget o menu
#VISTOS EN CLASE PARA REALIZAR ALGUNO DE LOS EJERCICIOS ENCARGADOS EN LA UNIDAD 2.



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
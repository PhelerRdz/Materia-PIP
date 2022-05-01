import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P1_EjemploCombobox.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.comboBox.addItem("Gato","matricula1") #Texto, data
        self.comboBox.addItem("Cuyo", 2)  # Texto, data
        self.comboBox.addItem("Perro", "matricula3")  # Texto, data

        self.txt_totalElementos.setEnabled(False)

        totElementos = self.comboBox.count()
        self.txt_totalElementos.setText(str(totElementos))

        self.comboBox.currentIndexChanged.connect(self.cambio)

        self.comboBox.setCurrentIndex(-1)
        #self.comboBox.setCurrentIndex(0)
        #self.comboBox.setCurrentIndex(1)

    def cambio(self):
        nombre = self.comboBox.currentText()
        indice = self.comboBox.currentIndex()
        data = self.comboBox.currentData()

        if indice != -1:
            self.txt_nombre.setText(nombre)
            self.txt_indice.setText(str(indice))
            self.txt_data.setText(str(data))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P4_ListaAlumnos.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.alumnos = {
            "Rolando": ["Rolando",18, "Ing. en Mercadotecnia"],
            "Juan": ["Juan", 16, "Ing. Industrial"],
            "Fernando": ["Fernando", 21, "Ing. Civil"],
            "Jesus": ["Jesus", 19, "Ing. en Sistemas Computacionales"],
            "Julio": ["Julio", 20, "Ing. en Geomatica"]
        }

        self.lw_alumnos.addItem(self.alumnos.get("Rolando")[0])
        self.lw_alumnos.addItem(self.alumnos["Juan"][0])
        self.lw_alumnos.addItem(self.alumnos.get("Fernando")[0])
        self.lw_alumnos.addItem(self.alumnos.get("Jesus")[0])
        self.lw_alumnos.addItem(self.alumnos.get("Julio")[0])


        cant_elementos = self.lw_alumnos.count()
        self.txt_total.setText(str(cant_elementos))

        self.lw_alumnos.currentRowChanged.connect(self.cambioFila)

        self.btn_eliminar.clicked.connect(self.eliminar)


    def eliminar(self):
        indice = self.lw_alumnos.currentRow()
        print(indice)
        if indice != -1:
            ##Cuidado al poner las Lineas 43-44 despues de la linea 46 <---
            texto = self.lw_alumnos.currentItem().text()
            self.alumnos.pop(texto) #elimina el elemento del diccionario

            self.lw_alumnos.takeItem(indice) #elimina al elemento del listwidget

            print(self.alumnos)


    def cambioFila(self):
        try:
            indice = self.lw_alumnos.currentRow()
            texto = self.lw_alumnos.currentItem().text()
            print("indice: ", indice , "  texto: ", texto)

            #clave = indice + 1
                                     #clave
            nombre = self.alumnos.get(texto)[0] #nombre
            edad =  self.alumnos.get(texto)[1]  #edad
            carrera = self.alumnos.get(texto)[2] #carrera

            self.txt_nombre.setText(nombre)
            self.txt_edad.setText(str(edad))
            self.txt_carrera.setText(carrera)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
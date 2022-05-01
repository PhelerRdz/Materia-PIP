import sys

from PyQt5 import uic, QtWidgets, QtCore

qtCreatorFile = "P7_CalificacionAlumno.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        ##########################################################################sd
        ###LEER ARCHIVO

        archivo = open("Archivos/Datos_Calificaciones.txt", "r")
        contenido = archivo.readlines()  # leer el contenido completo del archivo
        print(contenido)

        # Listas de comprensión
        self.lista = [linea.split("\t") for linea in contenido]
        print(self.lista)

        self.lista = [[registro[0], int(registro[1])] for registro in self.lista]
        print(self.lista)


        for i in self.lista:


            self.lw_alumnos.addItem(i[0])  #se añade únicamente el nombre del alumno


        self.lw_alumnos.currentRowChanged.connect(self.cambioFila)


    def cambioFila(self):
        try:
            indice = self.lw_alumnos.currentRow()
            print("indice: ", indice)

            calificacion = self.lista[indice][1] #calificacion

            self.txt_calificacion.setText(str(calificacion))

        except Exception as e:
            print(e)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


    #Práctica. Realizar una interfaz gráfica basada en el programa 7, que permita
    # aplicar un analisis estadistico sencillo a los datos del archivo
    #
    #Añadir botones para:
    #   Obtener calificación y nombre del alumno con menor calificacion
    #   Obtener calificación y nombre del alumno con mayor calificacion
    #   Obtener calificación y nombres de los alumnos con calificacion arriba del promedio
    #   Obtener calificación y nombres de los alumnos con calificacion abajo del promedio
    #   Calcular el promedio del grupo
    #   Calcular la Desviación Estandar y Varianza del Grupo

    
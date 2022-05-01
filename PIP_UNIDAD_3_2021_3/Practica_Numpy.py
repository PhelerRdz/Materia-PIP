import sys
import numpy as n

from PyQt5 import uic, QtWidgets

qtCreatorFile = "Practica_Numpy.ui"  # Nombre del archivo

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals
        self.Bagregar.clicked.connect(self.agre)
        self.Bagregar_2.clicked.connect(self.agre2)
        self.simular.clicked.connect(self.main)

        ##########################################################################

        self.ListaNum = []
        self.ListaNum2 = []

    # Área de los Slots
    def main(self):
        listaM = [self.ListaNum, self.ListaNum2]
        matriz = n.array(listaM)
        self.matrizbase.setText(str(matriz))
        ##########################################################################
        F, C = matriz.shape  # obtiene el orde de la matriz

        print("Filas:", F)
        print("Columnas:", C)

        matrizrand = n.random.randint(10, size=(F, C))
        self.matrizrandom.setText(str(matrizrand))
        ##########################################################################
        matrizT = matriz.T
        self.transpuesta.setText(str(matrizT))
        ##########################################################################
        print(matriz)
        print(matrizrand)
        suma=matriz+matrizrand
        self.suma.setText(str(suma))
        ##########################################################################
        multiplicacion = matriz * matrizrand
        self.multiplicacion.setText(str(multiplicacion))
        ##########################################################################
        matriz2 = n.random.randint(10, size=(F, C))
        self.continua_2.setText(str(matriz2))
        matrizrand2 = n.random.randint(10, size=(C, F+1))
        self.continua_3.setText(str(matrizrand2))
        continua = matriz2.dot(matrizrand2)
        self.continua.setText(str(continua))
        ##########################################################################
        try:
            matriz_inv = n.linalg.inv(matriz)
            self.inversa.setText(str(matriz_inv))

        except Exception as e:
            self.inversa.setText("TU MATRIZ\n NO ES CUADRADA")
        ##########################################################################
        try:
            self.redondeada.setText(str(n.around(matriz_inv)))
        except Exception as e:
            self.redondeada.setText("TU MATRIZ\n NO ES CUADRADA")
        ##########################################################################
        try:
            determinante=n.linalg.det(matriz)
            self.determinante.setText(str(n.around(determinante)))
        except Exception as e:
            self.determinante.setText("TU MATRIZ\n NO ES CUADRADA")
        ##########################################################################
        try:
            eclineales = n.linalg.solve(matriz, matrizrand)
            self.eclineales.setText(str(n.around(eclineales)))
        except Exception as e:
            self.determinante.setText("TU MATRIZ\n NO ES CUADRADA")
        ##########################################################################


    def agre2(self):
        num = int(self.Agregar_2.text())
        self.Agregar_2.clear()
        self.ListaNum2.append(num)
        self.Lista_2.setText(str(self.ListaNum2))

    def agre(self):
        num = int(self.Agregar.text())
        self.Agregar.clear()
        self.ListaNum.append(num)
        self.Lista.setText(str(self.ListaNum))



    #self.textEdit.setText(str(matrizT))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())


#PRACTICA 2. EJEMPLIFICAR LA FUNCIONALIDAD DEL MÓDULO NUMPY PARA CADA UNO DE LOS
# PUNTOS VISTOS EN CLASE. EMPLEAR INTERFACES GRÁFICAS CON PYQT5 (AL MENOS UNA INTERFAZ)

#TAREA-INVESTIGACIÓN: MÓDULO MATPLOTLIB
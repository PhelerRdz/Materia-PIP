import sys

from PyQt5 import QtWidgets, QtCore
from TProyecto_Ejemplo_JuegoGrafica import Plantilla_Juego as grafica

import matplotlib.pyplot as plt


class MyApp(QtWidgets.QMainWindow, grafica.Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        grafica.Ui_MainWindow.__init__(self)
        self.setupUi(self)

        # Área de los Signals / Configuracion
        self.btn_action.clicked.connect(self.action)
        self.rb_normal.setChecked(True)
        self.btn_arriba.clicked.connect(self.arriba)
        self.btn_izquierda.clicked.connect(self.izquierda)
        self.btn_derecha.clicked.connect(self.derecha)
        self.btn_abajo.clicked.connect(self.abajo)

        self.vel=0
        self.seg = 0
        self.min = 0

        self.segundoPlano = QtCore.QTimer()
        self.segundoPlano.timeout.connect(self.temporizador)

        ################################################################################
        ##LIMITES DEL TABLERO

        val = 10

        self.xMin = -val
        self.xMax = val

        self.yMin = -val
        self.yMax = val

        #################################################################################
        #                Jugador  Computadora
        #                   X  Y    X  Y
        self.personajes = [[0, 0], [0, 0]]

        ##############################################

        self.limpiar()

    # Área de los Slots
    def temporizador(self):
        self.limpiar()

        # POSICIONAR A LA MÁQUINA/COMPUTADORA EN UNA UBICACIÓN ALEATORIA
        import random as rnd
        xAleatoria = rnd.randrange(self.xMin, self.xMax)
        yAleatoria = rnd.randrange(self.yMin, self.yMax)
        self.personajes[1] = [xAleatoria, yAleatoria]  # Computadora se posiciona en ubicacion aleatoria

        self.graficar()

        if self.min != 0 and self.seg == 0:
            self.min -= 1
            self.seg = 59
            self.segundos.setText(str(self.seg))
            self.minutos.setText(str(self.min))
        elif self.min == 0 and self.seg == 0:
            self.segundoPlano.stop()
            m = QtWidgets.QMessageBox()
            m.setText("Has Ganado")
            m.exec_()
            self.btn_action.setText("INICIAR")
            self.limpiar()
        else:self.seg -= 1
        self.segundos.setText(str(self.seg))
        self.minutos.setText(str(self.min))

    def action(self):
        if self.btn_action.text() == "INICIAR":
            if self.rb_dificil.isChecked()==True:
                self.min=2
                self.seg=30
                self.vel=480
            elif self.rb_normal.isChecked()==True:
                self.min=1
                self.vel=800
            else:
                self.seg=30
                self.vel=1000
            self.segundos.setText(str(self.seg))
            self.minutos.setText(str(self.min))
            self.btn_action.setText("DETENER")
            self.segundoPlano.start(self.vel)
            self.personajes[0] = [0, 0]  # JUGADOR SE POSICIONA EN LA UBICACIÓN DE INICIO

        else:  # DETENER
            self.segundoPlano.stop()
            self.btn_action.setText("INICIAR")
            self.limpiar()

    def arriba(self):
        # Tener presente:
        # self.personajes[0]  = jugador
        # self.personajes[0][0]   ->>  X
        # self.personajes[0][1]   ->>  Y

        self.personajes[0][1] = self.personajes[0][1] + 1  # Actualiza la posicion del personaje

        self.limpiar()
        self.graficar()

    def izquierda(self):
        # Tener presente:
        # self.personajes[0]  = jugador
        # self.personajes[0][0]   ->>  X
        # self.personajes[0][1]   ->>  Y

        self.personajes[0][0] -= 1  # Actualiza la posicion del personaje

        self.limpiar()
        self.graficar()

    def derecha(self):
        # Tener presente:
        # self.personajes[0]  = jugador
        # self.personajes[0][0]   ->>  X
        # self.personajes[0][1]   ->>  Y

        self.personajes[0][0] += 1  # Actualiza la posicion del personaje

        self.limpiar()
        self.graficar()

    def abajo(self):
        # Tener presente:
        # self.personajes[0]  = jugador
        # self.personajes[0][0]   ->>  X
        # self.personajes[0][1]   ->>  Y

        self.personajes[0][1] -= 1  # Actualiza la posicion del personaje

        self.limpiar()
        self.graficar()

    def limpiar(self):
        plt.cla()  # lIMPIA AL LIENZO COMPLETO

        x = [i for i in range(self.xMin, self.xMax + 1)]
        y = [i for i in range(self.yMin, self.yMax + 1)]

        self.ax.set_xticks(y)
        self.ax.set_yticks(y)

        # Establecer los limites
        self.ax.set_xlim(self.xMin, self.xMax)
        self.ax.set_ylim(self.yMin, self.yMax)

        plt.grid(True)

        self.canvas.draw()

    def graficar(self):

        # Tener presente:
        # self.personajes[1]  = computadora
        # self.personajes[1][0]   ->>  X
        # self.personajes[1][1]   ->>  Y

        self.ax.plot(self.personajes[1][0], self.personajes[1][1],
                     marker="o",  # o . *  x   1
                     markersize=8,
                     markerfacecolor="green",  # color interno del marcador
                     markeredgewidth=1,  # tamaño del borde del marcador
                     markeredgecolor="black",  # color del borde del marcador
                     )

        # Tener presente:
        # self.personajes[0]  = jugador
        # self.personajes[0][0]   ->>  X
        # self.personajes[0][1]   ->>  Y

        self.ax.plot(self.personajes[0][0], self.personajes[0][1],
                     marker="o",  # o . *  x   1
                     markersize=8,
                     markerfacecolor="yellow",  # color interno del marcador
                     markeredgewidth=1,  # tamaño del borde del marcador
                     markeredgecolor="black",  # color del borde del marcador
                     )

        self.canvas.draw()

        # si x del personaje es igual a x de la computadora Y y del personaje es igual a y de la computadora
        # entonces el jugador gana...
        if self.personajes[0][0] == self.personajes[1][0] and self.personajes[0][1] == self.personajes[1][1]:
            self.segundoPlano.stop()
            m = QtWidgets.QMessageBox()
            m.setText("Has Perdido")
            m.exec_()
            self.btn_action.setText("INICIAR")
            self.limpiar()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())

# Consideraciones para el trabajo final
#
# 1.- Añadir una funcionalidad que extienda o cambie la actual
# 2.- Añadir un temporizador o un contador de tiempo
# 3.- Modificar la interfaz gráfica para añadirle estilo e imagenes
# 4.- El juego debe continuar hasta que se cumpla alguna condición de gane o perdida
#	(Es decir, no realizar una única ejecución)

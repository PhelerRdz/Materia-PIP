
import numpy as n

listaM = [[1, 2, 4],[3, 5, 6]]
print(listaM)

print()
matriz = n.array(listaM)
print(matriz)


# Pasa las columnas de una matriz a ser las filas de la matriz y viceversa

print()
matrizT = matriz.T
print(matrizT)


# OPERACIONES CON MATRICES Y ESCALARES
#       SUMA-RESTA
#       MULTIPLICACION
#       INVERSA             numpy.linalg.inv()
#       DETERMINANTE        numpy.linalg.det
#       POTENCIA            ** or power

#---> Gauss Jordan o Determinantes:
#               * Solucionar Sistemas de Ecuaciones Lineales        numpy.linalg.solve
#               * Inversa de una Matriz
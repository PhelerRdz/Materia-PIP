import numpy as n

# creacion de la listas que serán utilizadas para la obtención de las matrices con numpy
matrizCoef = [[1, 3], [-3, 4]]
matrizTI = [22, -1]
print(matrizCoef)
print(matrizTI)

print()  # para hacer espacio

# obtención de las matrices a partir de la listas de python
C = n.array(matrizCoef)
T = n.array(matrizTI)
print(C)
print(T)
print()

raices = n.linalg.solve(C, T)
print("Raices:")
print(raices)


#PRACTICA 2. EJEMPLIFICAR LA FUNCIONALIDAD DEL MÓDULO NUMPY PARA CADA UNO DE LOS
# PUNTOS VISTOS EN CLASE. EMPLEAR INTERFACES GRÁFICAS CON PYQT5 (AL MENOS UNA INTERFAZ)

#TAREA-INVESTIGACIÓN: MÓDULO MATPLOTLIB

import numpy as n

listaM = [[1, 2, 4],[3, 5, 6]]
print(listaM)

print()
matriz = n.array(listaM)
print(matriz)


F, C = matriz.shape  #obtiene el orde de la matriz

print("Filas:", F)
print("Columnas:", C)

print()

Filas = matriz.shape[0]   # 0 = Filas   1 = Columnas
print("Filas:", Filas)
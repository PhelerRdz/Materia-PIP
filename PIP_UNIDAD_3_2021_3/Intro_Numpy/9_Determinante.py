import numpy as n

# creacion de la listas que serán utilizadas para la obtención de las matrices con numpy
matrizA = [[3, -1, -1], [2, 1, 0], [3, 1, 2]]
print(matrizA)

print()  # para hacer espacio

# obtención de las matrices a partir de la listas de python
A = n.array(matrizA)
print(A)
print()


#Determinante de A
A_det = n.linalg.det(A)

print("Determinante: ")
print(n.round(A_det))

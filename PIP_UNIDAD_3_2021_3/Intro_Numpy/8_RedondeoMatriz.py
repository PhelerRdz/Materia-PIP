import numpy as n

# creacion de la listas que serán utilizadas para la obtención de las matrices con numpy
matrizA = [[5, 8, 6], [2, 9, 12], [3, 7, 8]]
print(matrizA)

print()  # para hacer espacio

# obtención de las matrices a partir de la listas de python
A = n.array(matrizA)
print(A)
print()


#Matriz Inversa de A
A_inv = n.linalg.inv(A)

print("Inversa: ")
print(A_inv)

print()
inv_redondeada = n.around(A_inv,4)
print(inv_redondeada)


#Comprobación
print()
print("Comprobación: ")
c = n.around(A.dot(inv_redondeada))
print(c)
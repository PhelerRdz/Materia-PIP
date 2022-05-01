import numpy as n

# creacion de la listas que serán utilizadas para la obtención de las matrices con numpy
matrizA = [[1, 2, 4], [3, 5, 6]]
matrizB = [[5, 8, 6], [2, 9, 12], [3, 7, 8]]
print(matrizA)
print(matrizB)

print()  # para hacer espacio

# obtención de las matrices a partir de la listas de python
A = n.array(matrizA)
B = n.array(matrizB)
print(A)
print()
print(B)

#REQUISITO PARA OBTENER LA MATRIZ INVERSA:
    # que la matriz origen sea cuadrada

# Consideraciones:   A es una matriz rectangular y B es una matriz cuadrada

#A_inv = n.linalg.inv(A)   # no se puede porque es rectangular

B_inv = n.linalg.inv(B)
print()
print("Resultado de B inversa:")
print(B_inv)


#comprobación: B * Binv  = Binv * B = I  (I =  matriz identidad)

#La matriz identidad es aquella que su diagonal principal tiene 1s y el resto de elementos son 0

print()
print("Comprobación 1: ")
print(n.ndarray.round(B.dot(B_inv),2))


print()
print("Comprobación 2: ")
print(B_inv.dot(B))

#Tarea: Como aplicar redondeo con arreglos en numpy
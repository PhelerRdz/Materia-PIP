import numpy as n

# creacion de la listas que serán utilizadas para la obtención de las matrices con numpy
matrizA = [[3, 2, 1], [1, 1, 3], [0, 2, 1]]
matrizB = [[2, 1], [1, 0], [3, 2]]

print(matrizA)
print(matrizB)

print()  # para hacer espacio

# obtención de las matrices a partir de la listas de python
A = n.array(matrizA)
B = n.array(matrizB)
print(A)
print()
print(B)

#REQUISITO PARA MULTIPLICAR MATRICES:
#   el número de columnas de la primera matriz debe ser igual al número de filas de la segunda

# Es decir,....

#C = A * B    La primera matriz es A y la segunda es B

#C = B * A    La primera matriz es B y la segunda es A

#En nuestro ejemplo: A => orden 3 x 3   y B => orden 3 x 2  Entonces, se pueden multiplicar


C = A.dot(B)   #Correcta forma de realizar la multiplicación de matrices


print()
print("Resultado de A*B")
print(C)


import numpy as n

# creacion de la listas que serán utilizadas para la obtención de las matrices con numpy
matrizA = [[1, 2, 4], [3, 5, 6]]
matrizB = [[5, 8, 6], [2, 9, 12]]
print(matrizA)
print(matrizB)

print()  # para hacer espacio

# obtención de las matrices a partir de la listas de python
A = n.array(matrizA)
B = n.array(matrizB)
print(A)
print()
print(B)

C = A * B             #este procedimiento no corresponde a la multiplicacion de matrices
print()
print("Resultado de A*B")
print(C)


#REQUISITO PARA MULTIPLICAR MATRICES:
#   el número de columnas de la primera matriz debe ser igual al número de filas de la segunda

# Es decir,....

#C = A * B    La primera matriz es A y la segunda es B

#C = B * A    La primera matriz es B y la segunda es A

#En nuestro ejemplo: A => orden 2 x 3   y B => orden 2 x 3  No se pueden multiplicar



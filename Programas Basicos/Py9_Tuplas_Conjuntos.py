# Las tuplas almacenan series de elementos
# Las tuplas son inmutables, una vez creadas no es posible modificarlas
a = (1, 2, 3)
b = 4, 5, 6
print("Tupla A: ", a)
print("Tupla B: ", b)
c = ("A", "B", "C")
print("Tupla C: ", c)
d = (1, "A", 2, "B")
print("Tupla D: ", d)
vect = []
vect = d
print("Vector: ", vect)

# Los conjutos son una serie de datos no ordenados y además no tienen elementos repetidos.
# Se crean con la instruccion set
numeros = [1, 2, 3, 4, 5, 3, 4, 5]
conjunto_numeros = set(numeros)
print("Conjunto de numeros: ", conjunto_numeros)

texto = "sin repeticiones"
letras = set(texto)
print("Conjunto de letras: ", letras)

# Se pueden realizar operaciones de conjuntos
texto1 = set("primer texto")
texto2 = set("segundo texto")
texto3 = texto1 - texto2  # letras de texto1 que no estan en texto2
print(texto3)
texto3 = texto1 | texto2  # letras en texto1 o en texto2
print(texto3)
texto3 = texto1 & texto2  # letras en texto1 y texto2 a la vez
print(texto3)
texto3 = texto1 ^ texto2  # letras en texto1 o texto2 pero no en ambos
print(texto3)

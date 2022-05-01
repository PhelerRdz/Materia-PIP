semana = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
print(semana)

semana.append('Sabado')  # añade el elemento x al final de la lista
print(semana)
semana.remove('Sabado')  # elimina el elemento x de la lista
print(semana)
semana.extend(['Sabado', 'Domingo'])  # añade la lista x al final de la lista
print(semana)
semana.pop()  # elimina y retorna con el elemento de la posicion x. Si no se indica x la operacion se realiza sobre el ultimo elemento de la lista
print(semana)
semana.insert(6, 'Domingo')  # inserta el elemento x en la posicion i de la lista
print(semana)

print(semana.index('Jueves'))  # devuelve el indice cuyo valor sea x
print(semana.count('Lunes'))  # devuelve el numero de ocurrencias del elemeto x en la lista

semana.reverse()  # inierte el orden de los elementos de una lista
print(semana)

semana.sort()  # ordena los elementos de una lista
print(semana)

numeros = [1, 2, 3, 4]
numeros.append(5)
print(numeros)
numeros.pop()
print(numeros)
print(numeros.index(3))
numeros.reverse()
print(numeros)
numeros.sort()
print(numeros)

tam = len(numeros)
for i in range(tam):
    num = numeros[i]
    num = num * 2
    numeros[i] = num

print(numeros)
# del lista[1] borra el elemento 1 de la lista
# del lista[2:4] borra del elemento 2 al 4 de la lista
# del lista[3:] borra los elementos a partir de la posicion 3
# del lista[:3] borra los elementos hasta la posicion 3
# del lista[:] borra toda la lista

numeros = ['1', '2', '3', '4', '5']
print(numeros[0])
print(numeros[2:4])
print(numeros[2:])
print(numeros[:3])
del numeros[1]
print("Funcion del")
print(numeros)

# Lista de listas -Matrices-
datos = [[]]
datos = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(datos)
print(datos[2][2])

# recorrer una matriz y acceder a los datos
tam = len(datos)
for x in range(tam):  # calculamos filas
    for y in range(tam):  # calculamos columnas
        t = datos[x][y]  # almacenar dato de una posicion dada
        datos[x][y] = t  # modificar datos de una posicion dada
        print(datos[x][y], end=" ")
    print("")
# transpuesta
transp = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tam = len(datos)
for x in range(tam):
    for y in range(tam):
        transp[y][x] = datos[x][y]

print(transp)
# identidad
for x in range(tam):
    for y in range(tam):
        if (x == y):
            transp[x][y] = 0

print(transp)

diag1 = transp
diag2 = transp
# triangular
for x in range(tam):
    for y in range(tam):
        if (x >= y):
            diag1[x][y] = 0
        print(str(diag1[x][y]), end=" ")
    print("")
print("")
for x in range(tam):
    for y in range(tam):
        if (x <= y):
            diag2[x][y] = 0
        print(str(diag2[x][y]), end=" ")
    print("")

data = [90, 67, 87, 64, 73, 92, 91, 91, 91, 90]
size = int(len(data))
data.sort()
print("Data: ", data)
sum = 0
mean = 0
moda = 0
for x in range(size):
    sum = sum + data[x]
    print(str(data[x]), end=" ")
print("")
mean = int(sum / size)
if (size % 2 == 0):
    index = int(size / 2)
    middle = (data[index] + data[index + 1]) / 2
else:
    index = int(size / 2)
    middle = data[index]
print("Mean: %f" % mean)
print("Median: %d" % middle)

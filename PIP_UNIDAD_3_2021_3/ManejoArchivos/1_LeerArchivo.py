
archivo = open("../Archivos/datos.txt", "r")

contenido = archivo.readlines()  #leer el contenido completo del archivo
print(contenido)

listaNums = list(map(int, contenido))
print(listaNums)

suma = sum(listaNums)
print(suma)

archivo = open("../Archivos/Datos_Calificaciones.txt", "r")

contenido = archivo.readlines()  #leer el contenido completo del archivo
print(contenido)

#Listas de comprensión
lista = [linea.split("\t") for linea in contenido]
print(lista)

lista = [[registro[0], int(registro[1])] for registro in lista]
print(lista)




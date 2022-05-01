print("Introduzca una palabra: ")
palabra = input()
i = len(palabra)
print("Tamaño de la cadena: %d" % i)
while i > 0:
    print(palabra[i - 1], end=" ")
    i = i - 1
print(" ")
cont = 0
while True:
    sensor = input("Ingrese valor de sendor:")
    cont += 1
    if int(sensor) > 100:
        print("Alto!")
        break

print("Contador: %d" % cont)

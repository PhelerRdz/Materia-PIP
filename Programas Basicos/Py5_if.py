print("Introduce edad: ")

edad = input()

if int(edad) >= 18:
    print("Ya eres mayor de edad!")
else:
    print("Aun no eres mayor de edad!")

entrada = input("Ingrese un numero:")
numero = int(entrada)
if (numero % 2 == 0) & (numero < 10):
    print("Numero es par o menor a 10")

print("Fuera de if")

print("Seleccione el valor para mantenimiento")
numero = input()
if int(numero) < 100:
    print("Mantenimiento A")
elif int(numero) < 150:
    print("Mantenimiento B")
elif int(numero) < 200:
    print("Mantenimiento C")
else:
    print("Mantenimiento D")

entrada = input("Ingrese numero:")
numero = int(entrada)
if (numero != 0) & (numero > 0):
    # codigo
    if numero < 100:
        print("Mantenimiento A")
    elif numero < 150:
        print("Mantenimiento B")
    elif numero < 200:
        print("Mantenimiento C")
    else:
        print("Mantenimiento D")
else:
    print("Numero ingresado no es valido!")

texto1 = "ASCII"
texto2 = "ascii"

if (texto1 == texto2):
    print("Cadenas iguales")
else:
    print("No iguales!")

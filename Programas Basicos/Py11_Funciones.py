def potencia(base, exponente=2):
    return int(base) ** exponente


base = input("Ingrese la base: ")
result = potencia(base)
print("Resultado: " + str(result))

print(potencia(2, 3))
print(potencia(2))


def solicita_nombre(cont, nombres):
    n = input('Nombre ' + str(cont) + ": ")
    if n not in nombres:
        nombres.append(n)
        return True
    else:
        return False


nombres = []
for i in range(3):
    if not solicita_nombre(i, nombres):
        exit('Repetido')

print(nombres)

ventas = {'ratones': 10, 'teclados': 13, 'CDs': 200, 'DVDs': 150}
print(ventas)

ventas['impresoras'] = 2
print(ventas)

del ventas['impresoras']
print(ventas)

print(ventas['ratones'])

flag = 'teclados' in ventas
print(flag)

for clave in ventas.keys():
    print(clave + " = " + str(ventas[clave]))

print("")
for clave, valor in ventas.items():
    print(clave + " = " + str(valor))

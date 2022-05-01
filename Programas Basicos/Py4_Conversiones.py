lenguaje = 'python'
print("Yo utilizo %s desde hace %d dias" % (lenguaje, 5))
edad = 24
print("Tengo %d dias" % (edad * 365))
print("Tengo %.2f dias" % (edad * 365))

print("tengo %03d años" % 30)  # tres cifras
print("tengo %-5d años" % 30)  # justifica 5 caracteres a la izquierda
print("tengo % 5d años" % 30)  # justifica 5 caracteres a la derecha

print(lenguaje[1])  # caracer 1 del string
c1 = lenguaje[0].upper()
c2 = lenguaje[1]
c3 = lenguaje[2]
c4 = lenguaje[3]
c5 = lenguaje[4]
c6 = lenguaje[5]
print("%s % 1s % 1s % 1s % 1s % 1s" % (c1, c2, c3, c4, c5, c6))


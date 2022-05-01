texto = "Hola, soy un string"
print(texto.count('o'))  # cuenta el numero de o's
print(texto.find('un'))  # busca la posicion de 'un'
print(texto.replace('un', 'el'))  # cambia 'un' por 'el'
txt = texto.upper()
print(txt)
txt = texto.lower()
print(txt)
# length
tam = len(texto)
print("Tam: " + str(tam))
print(texto.isalpha())
print(texto.isdigit())
print(texto.isnumeric())
print(texto.isalnum())

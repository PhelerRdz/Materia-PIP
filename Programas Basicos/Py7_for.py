import string

personas = ['Tere', 'Guillermo', 'Lars']
print(personas)

for p in personas:
    print(p)

# range(9) >> [0,1,2,4,5,6,7,8]
# range(2,8) >> [2,3,4,5,6,7]
# range(1,9,2) >> [1,3,5,7]
# range(10,0,-1) >> [10,9,8,7,6,5,4,3,2,1]
# range(10,0,-2) >> [10,8,6,4,2]
print(string.ascii_letters)
print(string.digits)
print("Introduzca tabla del 0 al 9:")
n = input()
if len(n) == 1 and n in string.digits:
    tabla = int(n)
    for i in range(1, 11):
        print(str(i) + " * " + str(n) + " = " + str(i * tabla))

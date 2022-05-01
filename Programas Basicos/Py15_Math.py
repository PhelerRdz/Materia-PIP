matrix = []
dim = int(input("Dimension de la matriz: "))
for x in range(0, dim):
    row = []
    for y in range(0, dim):
        # print("x: %d y: %d" % (x, y))
        if y == x or (x + y) == (dim - 1):
            row.append(1)
        else:
            row.append(0)
    matrix.append(row)

for row in matrix:
    print(row)
print("")
count = 0
for row in range(0, dim):
    count += 1
    matrix[0][row] = count

for row in matrix:
    print(row)

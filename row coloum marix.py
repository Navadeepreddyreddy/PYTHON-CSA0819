rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter the element at position ({i}, {j}): "))
        row.append(element)
    matrix.append(row)

print("Matrix:", matrix)

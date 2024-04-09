start = float(input("Enter the starting number: "))
lines = int(input("Max number of lines to print: "))

i = start
for l in range(lines):
    for j in range(l+1):
        print(round(i,1), end=' ')
        i += 0.1
    print()
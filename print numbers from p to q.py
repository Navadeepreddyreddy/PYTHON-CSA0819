P = int(input("Enter P: "))
Q = int(input("Enter Q: "))
R = int(input("Enter R: "))

print("Numbers are: ", end="")
for i in range(P, Q+1):
    if str(R) not in str(i):
        print(i, end=", ")
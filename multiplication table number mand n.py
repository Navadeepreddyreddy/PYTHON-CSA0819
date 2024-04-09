m = int(input("Input a number: m = "))
n = int(input("n = "))

print(f"Multiplication table of {m} from 1 to {n}:")

for i in range(1, n+1):
    result = m * i
    print(f"{m} x {i} = {result}")
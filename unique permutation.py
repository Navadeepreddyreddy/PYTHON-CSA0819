from itertools import permutations

number = input("Enter a number: ")

perms = set([int(''.join(p)) for p in permutations(number)])

print("Permutations are:")
for perm in perms:
    print(perm)
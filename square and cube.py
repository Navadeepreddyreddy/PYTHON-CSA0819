def squre_and_cube(num):
    square = num ** 2
    cube = num ** 3
    return square,cube

number = float(input("enter a decimal number:"))
square,cube = squre_and_cube(number)
print(f"the square of {number} is {square}")
print(f"the cube of {number} is {cube}")

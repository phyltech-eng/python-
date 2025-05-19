#a program tha is usd to swap two numbers
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("Before swapping: a =", a, ", b =", b)
temp = a
a = b
b = temp
print("After swapping: a =", a, ", b =", b)
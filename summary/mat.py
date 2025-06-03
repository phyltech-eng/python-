import math

print(math.pi)  # printing the value of pi
print(math.e)  # printing the value of e
print(math.sqrt(16))  # printing the square root of 16
print(math.pow(2, 3))  # printing 2 raised to the power of 3

#calculating the cuircumference of a circle

radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {round(circumference):.2f} units")
area = math.pi * radius ** 2
print(f"The area of the circle is: {round(area, 2)} square units")
#hypotenuse of a right triangle
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
hypotenuse = math.sqrt(a ** 2 + b ** 2)
print(f"The length of the hypotenuse is: {round(hypotenuse, 2)} units")


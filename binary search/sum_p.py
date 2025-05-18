#addition
num1=float(input("Enter first number: "))
num2=float(input("Enter second number: "))


def add(num1,num2):
    return num1+num2
#subtraction

def subtract(num1,num2):
    return num1-num2
#multiplication

def multiply(num1,num2):
    return num1*num2
#division
def divide(num1,num2):
    if num2==0:
        return "Error! Division by zero."
    else:
        return num1/num2
    
print(f"Addition: {add(num1, num2)}")    
 
print(f"Subtraction: {subtract(num1, num2)}")
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division: {divide(num1, num2)}")
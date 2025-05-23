#a function is a block of code that only runs when it is called


#create a function called my_function
def my_function():
    print("Hello from my function!")

#call the function
my_function()
#function with parameters:this is a function that takes parameters
def my_function_with_parameters(name):
    print("Hello " + name + " how are you?")

#call the function
my_function_with_parameters("John")
 #lambda function: this is a small anonymous function
#syntax: lambda arguments: expression
#creating a lambda function

my_lambda_function = lambda x: x + 1
#calling the lambda function
print(my_lambda_function(5))
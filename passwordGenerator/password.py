import random
print("Welcome to the password generator!")


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

number = int(input("How many passwords do you want to generate? "))
length = int(input("How long do you want your passwords to be? "))




print("Here are your passwords:")
for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)
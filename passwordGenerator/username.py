import random

print("Welcome to the username generator!")

chars= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"

number=int(input("How many usernames do you want to generate? "))

length=int(input("How long do you want your usernames to be? "))

print("Here are your usernames:")
for user in range(number):
    username= ""
    for l in range(length):
        username +=random.choice(chars)
        print(username)
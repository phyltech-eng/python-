#if/else condition are used to do something based on something being true or false

x = 10
y = 20


# if x < y:
#     print("x is less than y")
# elif x > y:
# #     print("x is greater than y")
# #nested if/else statements
# if x < y:
#     print("x is less than y")
#     if x == 10:
#         print("x is equal to 10")
#     else:
#         print("x is not equal to 10")
# elif x > y:
#     print("x is greater than y")
#     if x == 20:
#         print("x is equal to 20")
#     else:
#         print("x is not equal to 20")        

#membership operators:these operators are used to test if a sequence is present in an object
# in and not in operators
members = [1, 2, 3, 4, 5]
if 3 in members:
    print("3 is in the list")
if 6 not in members:
    print("6 is not in the list")

    #identity operators:these operators are used to compare the memory location of two objects

x = [1, 2, 3]
y = [1, 2, 3]
if x is y:
    print("x and y are the same object")
elif x is not y:
    print("x and y are not the same object")
 

 #loops:loops are used to iterate over a sequence (list, tuple, set, dictionary, string) or other iterable objects
# for loop: this loop is used to iterate over a sequence
peaple = ["John", "Jane", "Jim"]
for person in peaple:
    if person == "Jane":
        print(person)
#break statement: this statement is used to break out of a loop
    if person == "Jim":
        break
    print(person)
#continue statement: this statement is used to skip the current iteration of a loop
for person in peaple:
    if person == "Jane":
        continue
    print(person)
    #range function: this function is used to generate a sequence of numbers
    for i in range(len(peaple)):
        print(peaple[i])
for i in range(0,10):
    print (i)
#while loop: this loop is used to execute a block of code as long as a condition is true
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

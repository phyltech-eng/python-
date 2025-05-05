#string concsntination is how dtrings are put together 
#string interpolation is how strings are put together with variables
#string formatting is how strings are put together with variables and formatting


# #ways of achieving string concantination is in 2 ways:
# # 1. using the + operator
# example = "hello" + " " + "world"
# print(example) # hello world
# # use of format method
# example = "hello {} {}".format("world", "!")
# print(example) # hello world !
# # 2. using f-strings (formatted string literals)
# example = f"hello {'world'} {'!'}"
# print(example) # hello world !
place = input("Enter a place: ")
adjective1 = input("Enter an adjective: ")
emotion1 = input("Enter an emotion: ")
plural_noun1 = input("Enter a plural noun: ")
plural_noun2 = input("Enter another plural noun: ")
adjective2 = input("Enter another adjective: ")
animal = input("Enter an animal: ")
verb1 = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
famous_person = input("Enter a famous person: ")

madlib= f"Last summer, my family and I took a trip to {place}. The weather was really {adjective1} and I felt so {emotion1}.\
      We packed our bags with {plural_noun1}and {plural_noun2} before leaving.\
      On the way, we saw a {adjective2} {animal} crossing the road.\
        My brother tried to {verb1} but ended up falling into a {noun1}.\
            Everyone laughed, especially {famous_person} who was traveling with us!"
 
print(madlib)
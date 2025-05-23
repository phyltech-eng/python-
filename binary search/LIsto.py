numbers =[1, 2, 3, 4, 5]
 
 #creating a constractor
number2= list((1, 2, 3, 4, 5))

#creating a list
fruits = ["apple", "banana", "cherry"]
 # getting the length of the list
length = len(fruits)
print(length)
#adding an item to the list
fruits.append("orange")
#removing an item from the list
# fruits.remove("banana")
#inserting an item at a specific position
fruits.insert(1, "kiwi")
#sorting the list
fruits.sort()
#reversing the list
fruits.reverse()


print(fruits)
#tuple:this is a collection of ordered and unchangeable items
#creating a tuple
fruits_tuple = ("apple", "banana", "cherry")
#creating a tuple with one item
print((fruits_tuple))
#set :is a collection of unordered and unindexed items
#creating a set
fruits_set = {"apple", "banana", "cherry"}
#checking if an item is in the set
print("apple" in fruits_set)
#adding an item to the set
fruits_set.add("orange")
#removing an item from the set
fruits_set.remove("banana")

#dictionary: is a collection of unordered, changeable and indexed items
#creating a dictionary
fruits_dict = {
    "apple": 1,
    "banana": 2,
    "cherry": 3
}
#accessing an item in the dictionary
print(fruits_dict["apple"])
#adding an item to the dictionary
fruits_dict["orange"] = 4
#get dictionary keys
print(fruits_dict.keys())

print(fruits_dict)
#copying a dictionary
fruits_dict_copy = fruits_dict.copy()
#updating a dictionary
fruits_dict.update({"banana": 5})
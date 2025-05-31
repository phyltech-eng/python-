item = input("Enter the item you want to buy: ")
price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity you want to buy: "))
total_cost = price * quantity
print(f"You bought {quantity} {item}(s) at ${price:.2f} each. Total cost: ${total_cost:.2f}")

#madlibs
# Create a simple madlib game
print(f"today I went to the {item} store and bought {quantity} {item}(s) for ${price:.2f} each. It was a great deal!")
# Create a shopping list
shopping_list = []''

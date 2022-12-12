

cart = {}
prices = []
total = 0


# Stores user input into a dictionary
for i in range(10):
    # Takes in an input
    cart_item = input('Enter Item: ')
    item_price = float(input('Enter Price: $'))
    cart[cart_item.title()] = item_price
    prices.append(item_price)
    #The program Loops until user 'quits'
    proceed = input("add another item? (y/n): ")
    if proceed.lower() == 'n':
        break

# The User can see current shopping list
# Upon quiting the program, prints out a receipt of the items with total and quantity.
print('<---- YOUR CART ---->')
for k,v in cart.items():
    print(k,'-',v)

for price in prices:
    total += price
print(f'Your total is: ${total}')
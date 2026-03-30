inventory = {
    "apples": 5,
    "bananas": 10,
    "oranges": 8
}

user_bought = input('What did you buy?: ').strip().lower()
if user_bought in inventory:
    bought_amount = int(input(f'How many {user_bought} did you buy?: '))
    if bought_amount <= inventory[user_bought]:
        inventory[user_bought] -= bought_amount
        print(f'You bought {bought_amount} {user_bought}.')
        print(f'Thank you for shopping with us!')
    else:
        print(
            f'Sorry, we only have {inventory[user_bought]} {user_bought} left.')
else:
    print("Sorry, We don't sell that!")

print("\n --- Current Inventory ---")
for item, quantity in inventory.items():
    print(f'{item.capitalize()}: {quantity}')

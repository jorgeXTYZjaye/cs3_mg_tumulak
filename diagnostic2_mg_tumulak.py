toppings = ["Pepperoni", "Mushrooms", "Extra Cheese"]
topping_choice = ''
topping_count = 0

def calculate_total(topping_count):
    base_price = 10.00
    topping_price = 1.50
    total_price = base_price + (topping_count * topping_price)
    return total_price

def topping_menu():
    print("Topping Menu:")
    for i, topping in enumerate(toppings, start=1):
        print(f"{i}. {topping}")

while True:
    topping_menu()
    print("Enter toppings to add to your pizza (1-3). Type 'done' when finished:")
    topping_choice = input()
    if topping_choice == 'done':
        break
    elif topping_choice in ['1', '2', '3']:
        print(f"Added {toppings[int(topping_choice) - 1]} to your pizza.")
        topping_count += 1
    if topping_choice not in ['1', '2', '3', 'done']:
        print("Invalid choice. Not in the menu or type 'done'.")

total_price = calculate_total(topping_count)
print(f"Total price of your pizza with {topping_count} toppings is: ${total_price:.2f}")
class PizzaParlor:

    def __init__(self, pizza, topping, topping_count, total):
        self.pizza = pizza
        self.topping = topping
        self.topping_count = topping_count
        self.total =  total

    def display_info(self):
            print("Pizza: ", self.pizza)
            print("Topping: ", self.topping)
            print("Topping Count: ", self.topping_count)
            print("Total: ", self.total)
    
    def topping_menu():
        print ("Topping Menu: ")
        return "Pepperoni, Mushroom, Cheese"
        
pizza1 = PizzaParlor("Mushroom Pizza", "Mushroom", "1", "$11.50")
pizza2 = PizzaParlor("Cheesy Pepperoni", "Pepperoni, Cheese", "2", "$13.00")

pizza1.display_info()
print("-----------")
pizza2.display_info()
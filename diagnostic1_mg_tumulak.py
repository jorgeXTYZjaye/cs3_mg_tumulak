


def calculate_space_weight(earth_weight, destination):

    if destination == "mars":
        print(earth_weight * 0.38)

    elif destination == "jupiter":
        print(earth_weight * 2.34)

    elif destination == "moon":
        print(earth_weight * 0.16)

    else:
        print("Invalid destination. Please choose 'mars', 'jupiter', or 'moon'.")

print("Enter your weight on Earth (in kilograms):")
earth_weight = float(input())
print("Enter your destination (mars, jupiter, or moon):")
destination = input()

calculate_space_weight(earth_weight, destination)
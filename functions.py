#Imports
from menu import MENU, resources

#Initial profit
profit = 0


#Function to check each resource
def check_resources(ingredients):
    for item in ingredients:
        if ingredients[item] > resources[item]:
            print(f'Sorry, not enough {item}')
            return False
    return True


# Function to process the payment
def process_coins():
    total = 0
    print("Please, insert coins.")
    while True:
        try:
            total += int(input("How many quartes?: ")) * 0.25
            total += int(input("How many dimes?: ")) * 0.1
            total += int(input("How many nickles?: ")) * 0.05
            total += int(input("How many pennies?: ")) * 0.01
            break
        except:
            print("Not a valid value. Any money inserted will be refunded. Please, try again.")
            return False
    return total


# Function to check if payment is enough
def transaction(money,drink_cost):
    if money >= drink_cost:
        if money > drink_cost:
            change = money - drink_cost
            print(f"Here is your ${change:.2f} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


# Make the coffee, subtract the resources needed and add the payment to the cashier.
def make_coffee(drink_name, ingredients):
    for item in ingredients:
        resources[item] -= ingredients[item]
    print(f'Here is your {drink_name} ☕️Enjoy it!')
#Imports
from functions import *

#Condition to keep coffee machine on
coffee_machine = True


#Main program
while coffee_machine:
    choice = input("What would you like? (espresso / latte / capuccino): ").lower()     #Coffee options
    if choice == "off":                                                                 #Turn off the machine
        coffee_machine = False
    elif choice == "report":                                                            #Shows to user all available resources
       print(f"Water: {resources['water']}ml")
       print(f"Milk: {resources['milk']}ml")
       print(f"Coffee: {resources['coffee']}g")
       print(f"Money: ${profit}")
    elif choice in MENU.keys():                                                        #Access necessary resources to make the drink
        drink = MENU[choice]
        if check_resources(drink["ingredients"]):                                      #Checks if there are sufficient resources
            payment = process_coins()                                                  #Receive the payment
            if transaction(payment,drink["cost"]):                                     #Process the payment, then make the coffee
                profit += drink["cost"]
                make_coffee(choice,drink["ingredients"])
    elif choice == "manual":                                                           #Shows to user all valid inputs.
        print('''        ------------------------------------------------------
        [Off] - To turn off the machine.
        [Report] - To show available resources
        [Espresso] / Latte / Capuccino - To choose your drink
        [Manual] - To show this again.
        ------------------------------------------------------''')
    else:
        print("Not a valid answer.")




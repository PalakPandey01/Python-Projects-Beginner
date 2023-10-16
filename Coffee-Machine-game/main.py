import data
print("☕️Welcome to THE COFFEE MACHINE!!☕️")
money = 0
choice_input = "on"


def processing_order(order):
    water_required = data.MENU[order]["ingredients"]["water"]
    milk_required = data.MENU[order]["ingredients"]["milk"]
    coffee_required = data.MENU[order]["ingredients"]["coffee"]
    water_available = data.resources["water"]
    milk_available = data.resources["milk"]
    coffee_available = data.resources["coffee"]
    if water_available >= water_required and milk_available >= milk_required and coffee_available >= coffee_required:
        data.resources["water"] = water_available - water_required
        data.resources["milk"] = milk_available - milk_required
        data.resources["coffee"] = coffee_available - coffee_required
        return ("True")
    else:
        if water_available<water_required:
            return ("Water")
        if milk_available<milk_required:
            return ("Milk")
        if coffee_available<coffee_required:
            return ("Coffee")


def payment(order):
    global money
    to_pay = data.MENU[order]["cost"]
    print("Please Insert Coins")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickels = float(input("How many nickels?: "))
    pennies = float(input("How many pennies?: "))
    total_amount_given = ((quarters * 25)+(dimes * 10)+(nickels * 5)+(pennies * 1)) * 0.01
    print(f"Paid: {total_amount_given}")
    if total_amount_given == to_pay:
        money += to_pay
        change = 0.0
        print(f"Your Change: {change}.\nEnjoy your {order}!!")
    elif total_amount_given < to_pay:
        print("Insufficient coins given.Money Refunded!")
        data.resources["water"] += data.MENU[order]["ingredients"]["water"]
        data.resources["milk"] += data.MENU[order]["ingredients"]["milk"]
        data.resources["coffee"] += data.MENU[order]["ingredients"]["coffee"]
    else:
        money += to_pay
        change = total_amount_given-to_pay
        print(f"Your Change: {change}.\nEnjoy your {order}!!")


while choice_input != "off":
    choice_input = input("What would you like to order?(cappuccino,espresso,latte): ")
    if choice_input == "report":
        print(f"Water: {data.resources["water"]}ml\nMilk: {data.resources["milk"]}ml\nCoffee: {data.resources["coffee"]}gm\nMoney: ${money}")
    elif choice_input == "cappuccino" or choice_input == "espresso" or choice_input == "latte":
        ans = processing_order(choice_input)
        if ans == "True":
            payment(choice_input )
        else:
            ran_out_of = ans
            print(f"Sorry we ran out of {ran_out_of}!")
    if choice_input == "off":
        print("Coffee Machine going to sleep now! Gunnittee")
        break


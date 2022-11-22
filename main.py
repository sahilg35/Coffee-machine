MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
profit = 0

def sufficient_ingredients(order_ingredients):
  for item in order_ingredients:
    if order_ingredients[item] > resources[item]:
      print(f"Sorry there is not enough {item}.")
      return False
  return True

def charges():
  print("Please insert coins.")
  quarters = int(input("How many quarters?: "))
  dimes = int(input("How many dimes?: "))
  nickles = int(input("How many nickles?: "))
  pennies = int(input("How many pennies?: "))
  total = float((quarters*0.25)+(dimes*.10)+(nickles*0.05)+(pennies*0.01))
  return total

def drink_price(choice):
  money = float(MENU[drink]['cost'])
  return money

def result(input_money,actual_money):
  if input_money >= actual_money:
    left_money =  round(input_money - actual_money,2)
    print (f"Here is ${left_money} in change.")
    global profit
    profit += actual_money
    return True
  if input_money < drink_price(drink):
    print("Sorry there is not enough money.")
    return False

def make_coffee(choice,order_ingredients):
  for item in order_ingredients:
    resources[item] -= order_ingredients[item]
  print(f"Here is your {choice} ☕️. Enjoy!")

  
is_on = True

while is_on:
  choice = input("What would you like?(espresso/latte/cappuccino): ")
  if choice == "off":
    is_on = False
  elif choice == "report":
    water = (print(f"Water: {resources['water']}ml"))
    milk = print(f"Milk: {resources['milk']}ml")
    coffee = print(f"Coffee: {resources['coffee']}ml")
    money = print(f"Money: ${profit}")
  else:
    drink = MENU[choice]
    if sufficient_ingredients(drink["ingredients"]):
      payment = charges()
      if result(payment,drink["cost"]):
        make_coffee(choice,drink["ingredients"])






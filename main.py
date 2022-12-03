from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


my_coffee_machine = CoffeeMaker()
my_menu = Menu()
my_money_machine = MoneyMachine()

is_run = True
while is_run:
    choice = input(f"what u want {my_menu.get_items()}")
    if choice == "report":
        my_coffee_machine.report()
        my_money_machine.report()
    elif choice == "off":
            is_run = False
    elif my_menu.find_drink(choice):
        my_order = my_menu.find_drink(choice)
        # print(f"myorder {my_order}")
        # print (my_order.ingredients)
        if my_coffee_machine.is_resource_sufficient(my_order):
            if my_money_machine.make_payment(my_order.cost):
                my_coffee_machine.make_coffee(my_order)
        # print(my_order.cost)


# Author: Samuel Bennett
# Date: 4/7/2021
# Description: Prints the amount of change and for a value less then a dollar

print("This program gives the amount of change for values less then a dollar.")
change = int(input("Please enter amount of change 0 to 99: "))

def coin(amount, name, value):
    num_coins = 0
    while amount >= value:
        num_coins += 1
        amount -= value
    print(num_coins, name + ("s"))
    return amount


change = coin(change, "quarter", 25)
change = coin(change, "dime", 10)
change = coin(change, "nickle", 5)
change = coin(change, "penny", 1)

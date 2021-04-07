# Author: Samuel Bennett
# Date: 4/7/2021
# Description: Prints the amount of change and for a value less then a dollar
print("This program gives the amount of change on a value less then a dollar")
change=int(input("Please enter an value between 0-99: "))

print("quarters:", change//25)
change = change%25

print("dimes:", change//10)
change =change%10

print("nickles:", change//5)
change = change%5

print("pennies:", change//1)
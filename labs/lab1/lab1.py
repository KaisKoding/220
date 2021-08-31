"""
Name: <Derek Kai Oriee>
lab1.py

Problem: This function calculates the area of a rectangle
"""


def calc_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)

def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Area =", volume)

def shooting_percentage():
    shotsTotal = eval(input("Enter the total amount of shots: "))
    shotsMade = eval(input("Enter the total amount of shots made: "))
    percentage = ( shotsMade / shotsTotal ) * 100
    print("Your Accuracy is", percentage,"%")

def coffee():
    pounds = eval(input("Enter the total amount of pounds of coffee purchased: "))
    coffee = 10.50 * pounds
    shipping = 0.86 * pounds
    fixedCost = 1.50
    totalCost = coffee + shipping + fixedCost
    print("Your total will be", totalCost, "$")

def kilometers_to_miles():
    miles = 0.621371 * eval(input("Enter how many kilometers you will travel"))
    print(miles, "miles will be traveled.")


"""
Name: <Derek Kai Oriee>
<lab3>.py

Certificate of Authenticity:
I certify this assignment is entirely my own work

"""

import math


def average():
    homework_1, homework_2, homework_3, homework_4, homework_5, homework_6, homework_7, homework_8 = eval(
        input("Please input "
              "grades for "
              "Homework 1, "
              "Homework 2, "
              "Homework 3, "
              "Homework 4, "
              "Homework 5, "
              "Homework 6, "
              "Homework 7, "
              "and Homework "
              "8"))

    # Ask the user for their grades for each assignment

    homework = homework_1, homework_2, homework_3, homework_4, homework_5, homework_6, homework_7, homework_8

    avggrade = sum(homework, 0) / 8

    # Add all the grades together and divide the sum by 8

    print("Your average grade is: ", avggrade)

    # Print the average


def tip_jar():
    money = 0

    for jar in range(1, 6):  # Loop 5 times
        money = eval(input("Would you like to add a donation? If not, enter 0. : ")) + money
    # Ask user for how much they will donate
    # Add the amount the user donated

    print(money)  # Print the total amount in the jar once the loop is done


def newton():
    x = eval(input("Please insert x: "))  # Ask user for x
    approx = eval(
        input("Please insert how many times you would like to improve the approximation"))  # Ask user how many times
    # to improve the approximation
    for method in range(1, approx + 1):  # Make formula for Newtons Method
        approx = (approx + (x / approx)) / 2

    print(approx)  # Print the total


def sequence():
    uinput = eval(input("What number would you like?: "))  # Ask the user for what number they would like the list to
    # go to

    i = 1

    for num in range(0, uinput):
        rem = num % 2
        i = i + 2 * rem
        print(i, end="")


def pi():
    pi = math.pi  # Add a Pi variable

    n = eval(input("How many times would you like to repeat"))  # Ask the user how many times they would like to repeat

    i = 1

    for num in range(0, n):  # Create the sequence
        rem = num % 2
        i = pi / (i + 2 * rem)
        print(i, end="")  # I don't understand

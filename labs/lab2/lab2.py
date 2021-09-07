"""
Name: Derek "Kai" Oriee
<lab2>.py
"""

import math

def sum_of_threes():
    upperbound = eval(input("Please input upper bound: "))
    x = 0
    for num in range(3, upperbound + 1, 3):
            x = x + num
            print(x)
            #end of loop


def multiplicaton_table():
    for table in range (1, 11):
        print(table, table * 2, table * 3, table * 4, table * 5, table * 6, table * 7, table * 8, table * 9, table * 10)


def triangle_area():
    a = eval(input("Please enter side a: "))
    b = eval(input("Please enter side b: "))
    c = eval(input("Please enter side c: "))

    s = ((a + b + c) / 2)

    A = math.sqrt(s*(s - a)*(s - b)*(s - c))

    print("Your answer is: ", A)


def sumSquares():
    rangeStart = eval(input("Please enter the start of the range"))
    rangeEnd = eval(input("Please enter the end of the range: "))
    x = 0

    for square in range(rangeStart, rangeEnd + 1):
        x = x + square ** 2
        print(x)
        #end loop

def power():
    base = eval(input("Please enter your number: "))
    exponent = eval(input("Plese enter power: "))
    x = 1

    for power in range(exponent):
        x = x * base
        print(x)
        #end loop


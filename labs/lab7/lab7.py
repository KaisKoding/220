"""
Name: <Kai Oriee>
Partner: <your partner's name goes here – first and last>
lab7.py


Certificate of Authenticity:
I certify this assignment is entirely my own work
"""

from math import *


def cash_conversion():
    user_input = float(input("Please enter an integer: "))
    conversion = "{:.2f}".format(user_input)
    print(conversion)


def encode():
    user_input = str(input("Please insert a message: "))
    key = eval(input("Please insert key: "))
    cipher_message = []
    encoded_message = ""

    for i in user_input:
        cipher_message.append(ord(i) + key)

    for i in cipher_message:
        encoded_message += chr(i)

    print(encoded_message)


def sphere_area(radius):
    area = 4 * pi * (radius ** 2)
    return round(area, 2)


def sphere_volume(radius):
    volume = (4 / 3) * pi * (radius ** 3)
    return round(volume, 2)


def sum_n(n):
    sum_of_numbers = 0
    for i in range(n):
        sum_of_numbers += (i + 1)

    return sum_of_numbers


def sum_n_cubes(n):
    sum_of_numbers = 0
    for i in range(n):
        sum_of_numbers += (i + 1) ** 3

    return sum_of_numbers


def encode_better():
    user_input = str(input("Please insert a message: "))
    key = str(input("Please insert key: "))
    key_ordinal = []
    cipher_message = []
    encoded_message = ""

    for i in key:
        key_ordinal.append(ord(i) - 97)

    for i in range(len(user_input)):
        cipher_message.append(ord(user_input[i]) + key_ordinal[(i % len(key_ordinal))])

    for i in cipher_message:
        encoded_message += chr(i)

    print(encoded_message)




def main():
    # cash_conversion()
    encode()
    #encode_better()
    pass


main()

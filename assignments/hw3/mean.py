"""
Name: Derek Kai Oriee

Purpose: A program that asks for input, does arithmetic, and provides output

Certificate of Authenticity:
I certify this assignment is entirely my own work
"""

import math


def main():
    # get user input
    global ui
    ui = eval(input("Enter the values to be answered: "))

    # Create a loop that gets the sum of all entered values for rms mean operation

    rms_sum_of_values = 0

    for rms in range(0, ui):
        rms_sum_of_values = eval(input("Enter value:")) ** 2 + rms_sum_of_values

    # Create rms mean operation
    rms_mean_of_values = math.sqrt(rms_sum_of_values / ui)

    print(round(rms_mean_of_values, 3))

    hm_sum_of_values = 0

    for hm in range(0, ui):
        hm_sum_of_values = 1 / eval(input("Enter value:")) + hm_sum_of_values

    harmonic_mean = ui / hm_sum_of_values

    print(harmonic_mean)

    gm_sum_of_values = 0

    for gm in range(0, ui):
        gm_sum_of_values = eval(input("Enter value:")) + gm_sum_of_values

    geometeic_mean = math.sqrt(gm_sum_of_values) ** 1 / ui

    print(geometeic_mean)

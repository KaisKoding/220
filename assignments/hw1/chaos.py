"""

Name: Derek Kai Oriee
chaos.py

Purpose: this program illustrates a chaotic function

Certificate of Authenticity:
I certify this assignment is entirely my own work
"""

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("enter a number between 0 and 1: "))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print(x)

main()
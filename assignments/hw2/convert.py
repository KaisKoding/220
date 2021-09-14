"""

Name: Derek "Kai" Oriee
convert.py

Problem: convert Celsius to Fahrenheit

Certificate of Authenticity:
I certify this assignment is entirely my own work
"""


def main():
    celsius = eval(input("What is the temperature in Celsius?"))  # I get user input in celcius
    fahrenheight = (celsius * 9 / 5 + 32)  # I convert input from Celsius to Fahrenheit (celsius * 9/5 + 32)
    print("The temperature is:",fahrenheight, "degrees Fahrenheight. Awesome!") # Display result


main()


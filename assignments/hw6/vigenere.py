"""

Name: Derek Kai Oriee
chaos.py

Certificate of Authenticity:
I certify this assignment is entirely my own work
"""

from graphics import *

def main():

    width = 400
    height = 400
    win = GraphWin("Vigenere", width, height)

    message_pt = (150, 50)
    message = Text(message_pt, "Message to code")
    message.draw(win)

    # user_input = str(input("Please insert a message: "))
    #key = str(input("Please insert key: "))
    #key_ordinal = []
    #cipher_message = []
    #encoded_message = ""

    #for i in key:
     #   key_ordinal.append(ord(i) - 97)

    #for i in range(len(user_input)):
     #   cipher_message.append(ord(user_input[i]) + key_ordinal[(i % len(key_ordinal))])

    #for i in cipher_message:
     #   encoded_message += chr(i)

    #print(encoded_message)

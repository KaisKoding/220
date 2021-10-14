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

    message_pt = Point(75, 50)
    message = Text(message_pt, "Message to code")
    message.draw(win)
    user_input_pt = Point(265, 50)
    user_input = Entry(user_input_pt, 25)
    user_input.draw(win)
    sentence = str(user_input.getText())

    key_message_pt = Point(75, 100)
    key_message = Text(key_message_pt, "Enter keyword")
    key_message.draw(win)
    key_point = Point(265, 100)
    key = Entry(key_point, 25)
    key.draw(win)
    key_text = str(key.getText())

    key_ordinal = []
    cipher_message = []
    encoded_message = ""

    win.getMouse()

    for i in key_text:
        key_ordinal.append(ord(i) - 97)

    for i in range(len(sentence)):
        cipher_message.append(ord(sentence[i]) + key_ordinal[(i % len(key_ordinal))])

    for i in cipher_message:
        encoded_message += chr(i)

    result_message_pt = Point(200, 300)
    result_message = Text(result_message_pt, "Resulting Message")
    result_message.draw(win)

    vigenere_pt = Point(100, 100)
    vigenere = Text(vigenere_pt, encoded_message)
    vigenere.draw(win)

    win.getMouse()
    win.close()


if __name__ == "__main__":
    main()
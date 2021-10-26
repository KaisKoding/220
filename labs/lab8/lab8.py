"""
Name: Derek Kai Oriee
lab8.py

Certificate of Authenticity:
I certify this assignment is entirely my own work
"""
from encryption import encode, encode_better

def number_words(in_file_name, out_file_name):
    walrus_file = open(in_file_name, "r")
    output = open(out_file_name, "w")
    walrus = walrus_file.read()
    walrus = walrus.split()

    for letter in range(len(walrus)):
        print(letter + 1, walrus[letter], file=output)


def hourly_wages(in_file_name, out_file_name):
    hourly_wage_file = open(in_file_name, "r")
    output = open(out_file_name, "w")
    hourly_wage = hourly_wage_file.read()
    hourly_wage = hourly_wage.split("\n")

    for line in hourly_wage:
        split_line = line.split()
        name = split_line[0] + " " + split_line[1]
        pay = (eval(split_line[2]) + 1.65) * eval(split_line[3])
        print(name, "pay for the week:", pay, file=output)


def calc_check_sem(isbn):

    number = 10
    isbn_output = 0
    for num in range(number):
        subtractor = number - num
        isbn_output = isbn_output + (int(isbn[num]) * subtractor)

    print(isbn_output)


def send_message(file, friend):
    message_file = open(file, "r")
    output_file = open(friend, "w")
    message = message_file.read()
    print(message, file=output_file)


def send_safe_message(file, friend, key):
    message_file = open(file, "r")
    output_file = open(friend, "w")
    message = message_file.read()

    user_input = str(message)
    cipher_message = []
    encoded_message = ""

    for i in user_input:
        cipher_message.append(ord(i) + key)

    for i in cipher_message:
        encoded_message += chr(i)

    print(encoded_message, file=output_file)


def send_uncrackable_message(file, friend, pad):
    output_file = open(friend, "w")
    output_file.write(encode_better(file, pad))


def main():
    # number_words("Walrus.txt", "walrus_output.txt")
    # hourly_wages("hourly_wages.txt", "wages_output.txt")
    # calc_check_sem("0072946520")
    # send_message("message.txt", "friend.txt")
    # send_safe_message("message.txt", "safe_friend.txt", 1)
    send_uncrackable_message("safest_message.txt", "safest_friend.txt", "pad")
    pass


main()

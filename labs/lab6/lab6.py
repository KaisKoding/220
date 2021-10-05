"""
Name: Derek Kai Oriee
lab6.py
"""


def name_reverse():
    """
    Read a name in first-last order and display it in last-comma-first order.
    """
    name = input(" What is your name, first-last: ")
    reversed_name = name.split()
    print(reversed_name[::-1])


def company_name():
    internet_domain = input(" Please insert domain name: ")
    front_removal = internet_domain.lstrip("www.")
    company = front_removal.rstrip(".com")
    print(company)


def initials():
    for s in range(3):
        student = input("Please insert Student %s's first name:" % (s + 1))
        last_name = input("Insert %s's last name:" % student)
        print(student[0] + last_name[0])


def names():
    students = input("Please enter a list of student names, separated by commas: ")
    student_names = students.split(",")
    for i in range(len(student_names)):
        names = student_names[i].split()[0][0]
        lastnames = student_names[i].split()[1][0]
        print(names, lastnames, end=" ")


def thirds():
    text = input("Please enter a sentence")
    text_length = len(text)

    for i in range(2, text_length, 3):
        thirds = text[i]
        print(thirds, end=" ")


def word_average():
    sentence = input("Insert your sentence: ")
    sentence_split = sentence.split()

    length_of_sentence = len(sentence_split)
    sum_of_words = 0

    for i in range(length_of_sentence):
        sum_of_words += len(sentence_split[i])

    avg_words = sum_of_words / length_of_sentence

    print(avg_words)


def pig_latin():
    text = input("Insert sentence: ")




def main():
   # name_reverse()
   # company_name()
   # initials()
   # names()
   # thirds()
   # word_average()

    pass
main()

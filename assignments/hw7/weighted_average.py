"""
Name: Derek Kai Oriee

Certificate of Authenticity:
I certify this assignment is entirely my own work
"""


def weighted_average(in_file_name, out_file_name):
    grades_file = open(in_file_name, "r")
    grades_list = str(grades_file.read())
    grades_list = grades_list.split("\n")
    output = open(out_file_name, "w")

    class_grade = 0
    for line in grades_list:
        split_line = line.split(":")
        name = split_line[0]
        numbers = split_line[1].split()

        grades = 0
        weights = 0
        for i in range(0, len(numbers), 2):
            weight = int(numbers[i])
            grade = int(numbers[i + 1])
            weights = round(weights + weight, 2)
            grades = round(grades + (weight * grade), 2)

        if weights != 100:
            print("Error: the weights are less than 100.", file=output)

        else:
            avg_file = open(out_file_name, "w")
            avg = grades / 100
            print(name + ":" + str(avg), file=output)

            class_grade = class_grade + avg


def main():
    weighted_average("grades.txt", "avg.txt")


main()

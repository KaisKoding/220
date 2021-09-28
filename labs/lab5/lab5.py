"""
Name: Derek Kai Oriee
lab5.py
"""
import math

from graphics import *


def target():
    win_width = 500
    win_height = 500
    win = GraphWin("Archery Target", win_width, win_height)

    # Add code here to get the dimensions and draw the target

    # Wait for another click to exit
    win.getMouse()
    win.close()


def triangle():
    win_width = 500
    win_height = 500
    win = GraphWin("Draw a Triangle", win_width, win_height)

    # Instructions
    text_pt = Point(win_width / 2, win_height - 10)
    text = Text(text_pt, "Please select three points")
    text.draw(win)

    # Add code here to accept the mouse clicks, draw the triangle.
    ui1 = win.getMouse()
    ui1.draw(win)
    ui2 = win.getMouse()
    ui2.draw(win)
    ui3 = win.getMouse()
    ui3.draw(win)

    triangleshape = Polygon(ui1, ui2, ui3)
    triangleshape.draw(win)

    # and display its area in the graphics window.
    dx1 = (ui2.getX() - ui1.getX())
    dy1 = (ui2.getY() - ui1.getY())
    a = math.sqrt((dx1 ** 2) + (dy1 ** 2))

    dx2 = (ui3.getX() - ui2.getX())
    dy2 = (ui3.getY() - ui2.getY())
    b = math.sqrt((dx2 ** 2) + (dy2 ** 2))

    dx3 = (ui1.getX() - ui3.getX())
    dy3 = (ui1.getY() - ui3.getY())
    c = math.sqrt((dx3 ** 2) + (dy3 ** 2))

    s = (a + b + c) / 2

    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    text.undraw()
    areamessage = Text(text_pt, "Your area is %s" % round(area, 2))
    areamessage.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def color_shape():
    '''Create code to allow a user to color a shape by entering rgb amounts'''

    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_text.setTextColor("red")
    red_entry_pt = Point(win_width / 2 - 10, win_height / 2 + 40)
    red_entry = Entry(red_entry_pt, 5)

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_text.setTextColor("green")
    green_entry_pt = red_entry_pt.clone()
    green_entry_pt.move(14, 30)
    green_entry = Entry(green_entry_pt, 5)

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_text.setTextColor("blue")
    blue_entry_pt = red_entry_pt.clone()
    blue_entry_pt.move(14, 60)
    blue_entry = Entry(blue_entry_pt, 5)

    # display rgb text
    red_text.draw(win)
    red_entry.draw(win)
    green_text.draw(win)
    green_entry.draw(win)
    blue_text.draw(win)
    blue_entry.draw(win)

    # get int values from user input
    for c in range(5):
        win.getMouse()

        red = red_entry.getText()

        green = green_entry.getText()

        blue = blue_entry.getText()

        # re-color circle
        color = color_rgb(eval(red), eval(green), eval(blue))

        shape.setFill(color)

    # end message
    inst.undraw()
    endmsg = "Please click again to end the program."
    endmessage = Text(Point(win_width / 2, win_height - 20), endmsg)
    endmessage.draw(win)

    # Wait for another click to exit
    win.getMouse()
    win.close()


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, 7.2]

    x = values[1] + values[3]
    print(x)
    x = values[0] + values[2]
    print(x)
    x = values[1] + values[1] + values[1] + values[1] + values[1]
    print(x)
    x = [2.5, "there", pt]
    print(x)
    x = [2.5, "there", 5]
    print(x)
    x = [2.5, 5, 7.2]
    print(x)
    x = sum(x)
    print(x)
    x = len(values)
    print(x)


def another_series():
    terms = eval(input("Please input a number"))

    for i in range(terms):
        adder = (i + terms) % 2
        print(i + adder, end="")

        # Could there be an explanation for this one, please?


def main():
    # target()
    # triangle()
    # color_shape()
    # process_list()
    # another_series()
    pass


main()

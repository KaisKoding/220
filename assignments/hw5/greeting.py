"""
Name: Derek Kai Oriee

Certificate of Authenticity:
I certify this assignment is entirely my own work
"""

from graphics import *


def greeting():
    global valentines, point1
    point1 = Point(width / 2, 375)
    valentines = Text(point1, "Happy Valentines Day!")
    valentines.draw(win)


def heart():
    polygon1 = Polygon(Point((width / 2), 350), Point(75, 200), Point(335, 200))
    polygon1.setFill("red")
    polygon1.setOutline("red")
    polygon1.draw(win)
    circle1 = Circle(Point(130, 150), 75)
    circle1.setFill("red")
    circle1.setOutline("red")
    circle1.draw(win)
    circle2 = Circle(Point(280, 150), 75)
    circle2.setFill("red")
    circle2.setOutline("red")
    circle2.draw(win)
    circle3 = Circle(Point(200, 200), 60)
    circle3.setFill("red")
    circle3.setOutline("red")
    circle3.draw(win)


def arrow():
    global i
    subtractor = 400
    for i in range(0, 400):
        arrow_base = Rectangle(Point((50 - subtractor) + i, height / 2), Point((350 - subtractor + i), (height / 2) + 10))
        arrow_base.setFill("brown")
        arrow_base.setOutline("black")
        arrow_base.draw(win)

        arrow_head = Polygon(Point((350 - subtractor) + i, (height / 2) - 10), Point((350 - subtractor) + i, (height / 2) + 20), Point((370 - subtractor) + i, (height / 2) + 5))
        arrow_head.setOutline("black")
        arrow_head.setFill("white")
        arrow_head.draw(win)
        time.sleep(0.01)

    valentines.undraw()
    end_message = Text(point1, "Click to close")
    end_message.draw(win)


def main():
    global width, height, win
    width = 400
    height = 400
    win = GraphWin("Greeting", width, height)

    greeting()
    heart()
    arrow()
    win.getMouse()
    win.close()


main()
"""
Name: Derek Oriee
lab4.py

Certificate of Authenticity:
I certify this assignment is entirely my own work
"""

from graphics import *


def squares():
    """  <---  You can use tripled quotes to write a multi-line comment....

    Modify the following function to:

    Draw squares (20 X 20) instead of circles. Make sure that the center of the square
    is at the point where the user clicks. Make the window 400 by 400.

    Have each successive click draw an additional square on the screen (rather
    than just moving the existing one).

    Display a message on the window "Click again to quit" after the loop, and
    wait for a final click before closing the window.
    """
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Lab 4", width, height)

    # number of times user can move circle
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move circle")
    instructions.draw(win)

    # builds a circle
    shape = Rectangle(Point(0, 0), Point(20, 20))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the circle
    for i in range(num_clicks):
        p = win.getMouse()
        c = shape.getCenter()  # center of circle

        # move amount is distance from center of circle to the
        # point where the user clicked
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx, dy)
        clone = shape.clone()
        clone.draw(win)

    # Create end message
    instructions.undraw()
    endmessage = Text(inst_pt, "Click again to quit")
    endmessage.draw(win)

    win.getMouse()
    win.close()


def rectangle():
    """
    This program displays information about a rectangle drawn by the user.
    Input: Two mouse clicks for the opposite corners of a rectangle.
    Output: Draw the rectangle.
         Print the perimeter and area of the rectangle.
    Formulas: area = (length)(width)   and    perimeter = 2(length+width)
    """

    # Create the graphics window
    width = 400
    height = 400
    win = GraphWin("Rectangle", width, height)

    # Give instructions
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Please click on two points")
    instructions.draw(win)

    # Get user input for rectangle points
    ui1 = win.getMouse()
    ui1.draw(win)
    ui2 = win.getMouse()
    ui2.draw(win)

    # Create the rectangle
    rect = Rectangle(ui1, ui2)
    rect.setFill("red")
    rect.setOutline("red")
    rect.draw(win)

    # Calculate perimeter and area
    length = ui2.getX() + ui1.getX()
    width = ui2.getY() + ui1.getY()

    print(length * width)


    win.getMouse()


def main():
    # squares()
    rectangle()
    # circle()
    # pi2()


main()

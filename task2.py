import turtle
import math


def pythagoras_tree(t, order, size, angle):
    if order == 0:
        return

    t.forward(size)

    t.left(angle)
    pythagoras_tree(t, order - 1, size / math.sqrt(2), angle)

    t.right(2 * angle)
    pythagoras_tree(t, order - 1, size / math.sqrt(2), angle)

    t.left(angle)
    t.backward(size)


def draw_pythagoras_tree(angle=45, size=100):
    try:
        order = int(input("Please enter number of recursion(int): "))
    except ValueError:
        print("Invalid input. Please enter an integer.")
        return

    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed("fastest")
    t.left(90)
    t.color("red")
    t.penup()
    t.goto(0, -size)
    t.pendown()

    pythagoras_tree(t, order, size, angle)

    window.mainloop()


if __name__ == "__main__":
    draw_pythagoras_tree()

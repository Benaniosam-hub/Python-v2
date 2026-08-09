import turtle

def draw(array):
    colours = {
        1: "red",
        2: "white",
        3: "yellow",
        4: "orange",
        5: "green",
        6: "blue",
        7: "purple",
        8: "cyan",
        9: "magenta",
        0: "black",
    }

    n = len(array)

    CELL_SIZE = 100

    screen = turtle.Screen()
    screen.bgcolor("grey")

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.pensize(5)

    def draw_square(x, y, colour):
        """Draw one coloured square with its top-left corner at x, y."""
        pen.penup()
        pen.goto(x, y)
        pen.setheading(0)
        



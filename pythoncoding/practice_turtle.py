import turtle

screen = turtle.Screen()
pen = turtle.Turtle()

def draw_square(x,y, colour):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

    pen.pencolor(colour)
    pen.fillcolor(colour)

    pen.begin_fill()

    for _ in range(4):
        pen.forward(100)
        pen.right(90)

    pen.end_fill()

draw_square(-50, 50, "blue")

turtle.done()
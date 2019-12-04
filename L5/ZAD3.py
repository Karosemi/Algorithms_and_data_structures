import turtle

# wn = turtle.Screen()
# wn.bgcolor("lightgreen") # Set the window background color
# # wn.title("Hello, Tess!") # Set the window title
# tess = turtle.Turtle()
# tess.color("blue") # Tell tess to change her color
# tess.pensize(3) # Tell tess to set her pen width
# tess.forward(50)
# tess.backward(50)
# tess.left(120)
# tess.forward(50)
# wn.exitonclick()

from time import sleep

def left_hilbert_curve(n, tess):
    if n == 1:
        tess.forward(25)
        tess.left(90)
        tess.forward(25)
        tess.left(90)
        tess.forward(25)
    else:
        # tess.left(90)
        hilbert_curve(n - 1, tess)
        # hilbert_curve(n-1, tess)
        tess.left(90)
        tess.forward(25)
        left_hilbert_curve(n - 1, tess)
        tess.right(90)
        tess.forward(25)
        tess.right(90)
        left_hilbert_curve(n - 1, tess)
        tess.forward(25)
        tess.left(90)
        hilbert_curve(n - 1, tess)
        # tess.forward(25)
        # wn.exitonclick()



def hilbert_curve(n, tess):

    if n == 1:
        # tess.left(250)
        # sleep(1)
        tess.right(90)
        sleep(1)

        tess.forward(25)
        # sleep(1)
        tess.right(90)
        tess.forward(25)
        # sleep(1)
        tess.right(90)
        tess.forward(25)
        # wn.exitonclick()
    else:
        tess.right(90)
        left_hilbert_curve(n-1, tess)
        hilbert_curve(n-1, tess)
        tess.right(90)
        tess.forward(25)
        tess.right(90)
        hilbert_curve(n - 1, tess)
        tess.left(90)
        tess.forward(25)
        tess.left(90)
        hilbert_curve(n-1, tess)
        tess.forward(25)
        tess.right(90)
        left_hilbert_curve(n-1,tess)
        # tess.forward(25)
        # wn.exitonclick()

wn = turtle.Screen()
tess = turtle.Turtle()
tess.color("black")
tess.pensize(3)
tess.left(90)
hilbert_curve(2, tess)




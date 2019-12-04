import turtle
from time import sleep

class HilbertCurve:

    def __init__(self, n):
        self.wn = turtle.Screen()
        self.tess = turtle.Turtle()
        self.tess.color("black")
        self.tess.pensize(3)
        self.tess.left(90)
        self.distance = 10
        self.angle = 90

    def r5_hilbert(self, n): #4
        self.tess.left(self.angle)
        self.r_hilbert_curve(n-1)
        self.tess.left(self.angle)
        self.tess.forward(self.distance)
        self.l_hilbert_curve(n-1)
        self.tess.right(self.angle)
        self.tess.forward(self.distance)
        self.tess.right(self.angle)
        self.l_hilbert_curve(n-1)
        self.tess.forward(self.distance)
        self.tess.left(self.angle)
        self.r_hilbert_curve(n-1)
        self.wn.exitonclick()

#parzyste roznia se tylko tym ze na poczatku jest kat

    def hilbert(self, n): #4
        self.tess.right(self.angle)
        self.l_hilbert_curve(n-1)
        self.tess.right(self.angle)
        self.tess.forward(self.distance)
        self.r_hilbert_curve(n-1)
        self.tess.left(self.angle)
        self.tess.forward(self.distance)
        self.tess.left(self.angle)
        self.r_hilbert_curve(n-1)
        self.tess.forward(self.distance)
        self.tess.right(self.angle)
        self.l_hilbert_curve(n-1)
        self.wn.exitonclick()

    def l_hilbert_curve(self, n): #3
        self.right_hilbert_curve(n-1)
        self.tess.forward(self.distance)
        self.tess.left(self.angle)
        self.left_hilbert_curve(n-1)
        self.tess.forward(self.distance)
        self.left_hilbert_curve(n - 1)
        self.tess.left(self.angle)
        self.tess.forward(self.distance)
        self.right_hilbert_curve(n - 1)
        # self.wn.exitonclick()

    def r_hilbert_curve(self,n): #3
        # self.tess.left(self.angle)
        self.left_hilbert_curve(n-1)
        self.tess.forward(self.distance)
        self.tess.right(self.angle)
        self.right_hilbert_curve(n-1)
        self.tess.forward(self.distance)
        self.right_hilbert_curve(n-1)
        self.tess.right(self.angle)
        self.tess.forward(self.distance)
        self.left_hilbert_curve(n-1)
        # self.wn.exitonclick()

    def right_hilbert_curve(self,n):#1,2
        if n == 1:
            # sleep(3)
            self.tess.forward(self.distance)
            self.tess.right(self.angle)
            self.tess.forward(self.distance)
            self.tess.right(self.angle)
            self.tess.forward(self.distance)
        else:
            self.left_hilbert_curve(n-1)
            self.tess.right(self.angle)
            self.tess.forward(self.distance)
            self.right_hilbert_curve(n-1)
            self.tess.left(self.angle)
            self.tess.forward(self.distance)
            self.tess.left(self.angle)
            self.right_hilbert_curve(n-1)
            self.tess.forward(self.distance)
            self.tess.right(self.angle)
            self.left_hilbert_curve(n-1)


    def left_hilbert_curve(self, n):
        if n == 1:
            # sleep(3)
            self.tess.forward(self.distance)
            self.tess.left(self.angle)
            self.tess.forward(self.distance)
            self.tess.left(self.angle)
            self.tess.forward(self.distance)
        else:
            self.right_hilbert_curve(n-1)
            self.tess.left(self.angle)
            self.tess.forward(self.distance)
            self.left_hilbert_curve(n-1)
            self.tess.right(self.angle)
            self.tess.forward(self.distance)
            self.tess.right(self.angle)
            self.left_hilbert_curve(n-1)
            self.tess.forward(self.distance)
            self.tess.left(self.angle)
            self.right_hilbert_curve(n-1)

if __name__ == '__main__':
    hil = HilbertCurve(1)
    hil.right_hilbert_curve(2)
    hil.wn.exitonclick()
    # hil.l_hilbert_curve(3)
    # hil.r5_hilbert(4)
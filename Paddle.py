from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,cor_):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.goto(cor_)

    def up(self):
        y_pos = self.ycor() + 30
        self.goto(self.xcor(), y_pos)

    def down(self):
        y_pos = self.ycor() - 30
        self.goto(self.xcor(), y_pos)



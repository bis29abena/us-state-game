from turtle import Turtle

class State(Turtle):
    def __init__(self, x, y, state):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(arg=state, align="center", font=("Arial", 10, "normal"))


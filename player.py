from turtle import Turtle
import time
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

RAINBOW = ["#F9B3B4", "#FACEA1", "#FCFCBE", "#B9FACF", "#B5D1FF", "#D6ADF7", "#FAC1F8",
          "#F9B3B4", "#FACEA1", "#FCFCBE", "#B9FACF", "#B5D1FF", "#D6ADF7", "#FAC1F8"]

CHECKERBOARD = '''
▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀
▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀
▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀
'''

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.shapesize(1.2, 1.2)
        self.setheading(90)
        self.penup()
        self.goto(0, 240)
        self.color("#D9D9D9")
        self.write(CHECKERBOARD, False, "center", ("Arial", 8, "normal"))
        self.color("#D9D9D9")
        self.goto(STARTING_POSITION)
        # Debugging: self.write(f"{self.ycor()}", False, "left", ("courier", 12, "normal"))

    def move(self):
        self.forward(50)
        # Debugging: self.write(f"{self.ycor()}", False, "left", ("courier", 12, "normal"))

    def player_wins(self):
        self.goto(STARTING_POSITION)

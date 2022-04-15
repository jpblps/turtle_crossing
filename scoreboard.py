from turtle import Turtle

FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.color("#D9D9D9")
        self.level = 1

    def player_loses(self):
        self.goto(0, -5)
        self.color("coral")
        self.write(f"LOSER!", False, "center", ("courier", 28, "bold"))

    def track_level(self):
        self.goto(-245, -290)
        self.clear()
        self.write(f"Level: {self.level}", False, "center", FONT)
from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

        def __init__(self):
            super().__init__()
            self.level=1
            self.color("white")
            self.penup()
            self.goto(-270,320)
            self.write(f"Level: {self.level} ", align="center", font=FONT)
            self.hideturtle()
            self.update()

        def update(self):
            self.write(f"Level: {self.level} ", align="center", font=FONT)


        def level_up(self):
            self.level+=1
            self.clear()
            self.update()

        def gameover(self):
            self.goto(0,0)
            self.write("Game Over", align="center", font=FONT)
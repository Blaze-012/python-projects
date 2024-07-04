from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.current_level = 1
        self.penup()
        self.hideturtle()
        self.clear()
        self.goto(-275, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.current_level}", align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", align="center", font=FONT)

    def level_up(self):
        self.current_level += 1
        self.update()


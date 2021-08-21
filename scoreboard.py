from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('high_score.txt') as f:
            self.high_score = int(f.read())

        self.color('white')
        self.penup()
        self.goto(0, 267)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} High score: {self.high_score}', move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open('high_score.txt', mode='w') as f:
            f.write(f'{self.high_score}')

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


from turtle import Turtle

X_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in X_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        square = Turtle(shape='square')
        square.penup()
        square.speed('slowest')
        square.color('white')
        square.goto(position)
        self.segments.append(square)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() == 0.0:
            self.head.left(90)
        elif self.head.heading() == 180.0:
            self.head.right(90)

    def down(self):
        if self.head.heading() == 0.0:
            self.head.right(90)
        elif self.head.heading() == 180.0:
            self.head.left(90)

    def left(self):
        if self.head.heading() == 90.0:
            self.head.left(90)
        elif self.head.heading() == 270.0:
            self.head.right(90)

    def right(self):
        if self.head.heading() == 90.0:
            self.head.right(90)
        elif self.head.heading() == 270.0:
            self.head.left(90)

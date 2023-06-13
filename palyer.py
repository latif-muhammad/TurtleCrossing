from turtle import Turtle


STARTING_POS = (0, -240)
MOVE_DIS = 10
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POS)
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DIS)

    def go_down(self):
        if self.ycor() >= STARTING_POS[1]:
            self.backward(MOVE_DIS)

    def go_to_start(self):
        self.goto(STARTING_POS)

    def reached_finished(self):
        if self.ycor() >= FINISH_LINE:
            return True
        return False


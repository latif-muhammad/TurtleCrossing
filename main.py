from turtle import Screen
from palyer import Player
from scoreboard import Scoreboard
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "w")
screen.onkey(player.go_down, "s")

in_game = True
while in_game:
    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            in_game = False
            scoreboard.game_over()

    if player.reached_finished():
        player.go_to_start()
        scoreboard.increase_level()
        car_manager.increase_speed()

    screen.update()


screen.exitonclick()


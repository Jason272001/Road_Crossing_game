import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=750, height=750)
screen.bgcolor("black")
screen.tracer(0)
player=Player()
car=CarManager()
score=Scoreboard()
screen.listen()

screen.onkey(player.up,"Up")
screen.onkey(player.down,"Down")
screen.onkey(player.left_move,"Left")
screen.onkey(player.right,"Right")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    for c in car.cars:
       if c.distance(player)<25:
            game_is_on=False
            score.gameover()


    if player.finish_line():
        player.goto_start()
        car.speed_up()
        score.level_up()

screen.exitonclick()
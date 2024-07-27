from turtle import Screen
from createcar import CreateCar
from player import Player
from scoreboard import Score
import time

#Setting up screen
screen = Screen()
screen.setup(800, 700)
screen.bgpic("racetrack.png")
screen.tracer(0)

#Creating objects of the classes
car = CreateCar()
player = Player()
score = Score()
game_is_on = True

#Binding keys with keyboard keys
screen.onkeypress(player.move_up, "Up")
screen.onkeypress(player.move_down, "Down")
screen.listen()

#Main loop of the game
while game_is_on:
    score.show_score()                                  #Show score on the screen
    car.generate_car()                                  #Create a car
    car.move_car()                                      #Move it
    screen.update()                                     #Update the screen

    if player.ycor() >= 320:                            #If player reaches the top of the screen
        score.score_total += 5                          #Increment its score
        score.level += 1                                #Increment its level
        car.level_up()                                  #Increase speed of the cars
        player.reset()                                  #Send the player back to its original position

    for cars in car.all_cars:
        if cars.distance(player) < 20:                  #If player hits any car
            score.game_over()                           #Print "game over"
            game_is_on = False                          #Turn the game flag to false

    time.sleep(0.03)

screen.exitonclick()

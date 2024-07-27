from turtle import Turtle

#Declaring constants
X_POS = 0
Y_POS = -320
MOVE_DISTANCE = 10


class Player(Turtle):                                       #Creating Player class
    def __init__(self):
        super().__init__()                                  #Turtle as its super class
        self.penup()                                        #Turtle should not leave trace lines
        self.shape("turtle")                                #Shape of the turtle/player will be turtle
        self.color("black")                                 #Color will be black
        self.shapesize(1.5, 1.5)                            #Resizing the turtle to make it a little bigger
        self.goto(X_POS, Y_POS)                             #The turtle/player will be found at these co-ordinates initially
        self.setheading(90)                                 #Its heading will be set towards north

    def move_up(self):                                      #When u press the "up" key, turtle/player will move up 10 paces
        self.forward(MOVE_DISTANCE)

    def move_down(self):                                    #If turtle/player's y-coordinate is greater than -270 only then the back key will work
        if self.ycor() >= -320:
            self.backward(MOVE_DISTANCE)

    def reset(self):                                        #Sends the turtle/player back to its original position
        self.goto(X_POS, Y_POS)

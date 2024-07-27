from turtle import Turtle


class Score(Turtle):                                        #Creating Score class
    def __init__(self):
        super().__init__()                                  #Turtle as its super class
        self.hideturtle()                                   #Hide the turtle
        self.penup()                                        #Turtle should not leave trace lines
        self.goto(-300, 320)                                #Move the score/turtle to top left on the screen
        self.color("black")                                 #Color will be black
        self.score_total = 0                                #Initially the score will be zero
        self.level = 0                                      #Initially the level will be zero

    def show_score(self):                                   #Function to display score
        self.clear()
        self.write(f"Score = {self.score_total}, Level = {self.level}", False, align="center", font=('Arial', 15, 'normal'))

    def game_over(self):                                    #Function to display game_over
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=('Arial', 20, 'bold'))

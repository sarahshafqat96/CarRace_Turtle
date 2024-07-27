from turtle import Turtle
import random

#Declaring constants
car_list = ["racecar1.gif", "racecar2.gif", "racecar3.gif", "racecar4.gif", "racecar5.gif", "racecar6.gif"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CreateCar:                                                              #Creating CreateCar Class
    def __init__(self):
        self.all_cars = []                                                    #List variable to store the cars generated
        self.car_speed = STARTING_MOVE_DISTANCE                               #Variable to store car speed

    def generate_car(self):
        y_pos = random.randint(-250, 270)                                     #Y-coordinate will be chosen randomly from this range
        while y_pos in range(65, 135) or y_pos in range(-130, -65):           #Y-coordinate should not fall in these ranges because it will create the car on white lines of the road
            y_pos = random.randint(-270, 270)
        car_prob = random.randint(1, 6)                                       #Only create a car when random_chance = 1
        if car_prob == 1:
            new_car = Turtle()                                                #The car will be an object of class Turtle will be square
            new_car.penup()                                                   #The car/turtle should not leave nay traces
            turtle_shape = random.choice(car_list)                            #The shape will be selected randomly from "car_list" initialized above
            new_car.screen.addshape(turtle_shape)                             #That shape will be added to the screen
            new_car.shape(turtle_shape)                                       #And assigned to the turtle
            new_car.goto(340, y_pos)                                          #The car/turtle will go to these co-ordinates
            self.all_cars.append(new_car)                                     #Add that car to the all-cars list

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)                                      #Cars will move forward with this speed of "car_speed" v

    def level_up(self):
        self.car_speed += MOVE_INCREMENT                                      #Increment the speed with 5


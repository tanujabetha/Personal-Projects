from turtle import Turtle
import random as rd

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.newLocation()
        
        
    def newLocation(self):
        x = rd.randint(-280,280)
        y = rd.randint(-280,280)
        self.goto(x,y)

        
        
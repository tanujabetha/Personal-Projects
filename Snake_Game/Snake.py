from turtle import Turtle, Screen
import time
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVING_SPACES = 20
UP= 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.snake_list=[]
        self.createSnake()
        self.head = self.snake_list[0]
    
    def createSnake(self):
        for position in STARTING_POSITIONS:
            snake = Turtle("square")
            snake.penup()
            snake.color("red")
            snake.goto(position)
            self.snake_list.append(snake) 
    
    
    def AddSegment(self,position):
        snake = Turtle("square")
        snake.penup()
        snake.color("red")
        snake.goto(position)
        self.snake_list.append(snake)
        
    
    def extend(self):
        #Gets the position of the last segment of snake
        self.AddSegment(self.snake_list[-1].position())
            
    def move(self):
            for snakePart in range(len(self.snake_list)-1, 0 , -1):
                new_x = self.snake_list[snakePart-1].xcor()
                new_y = self.snake_list[snakePart-1].ycor()
                self.snake_list[snakePart].goto(new_x,new_y)
            self.head.forward(MOVING_SPACES)
            
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading()!= LEFT:
            self.head.setheading(RIGHT)
            
    def reset(self):
        for seg in self.snake_list:
            seg.goto(1000,1000)
        self.snake_list.clear()
        self.createSnake()
        self.head = self.snake_list[0]
            


        

    
    


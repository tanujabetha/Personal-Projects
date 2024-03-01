from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_value = 0
        with open("HighScore.txt") as file:
            highscore = int(file.read())
            self.high_score = highscore
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_value} High score is {self.high_score}", align="center", font=("Arial", 12, "normal"))

    def increase_score(self):
        self.score_value += 1
        self.update_scoreboard()
    
    def reset(self):
        if self.high_score > self.score_value:
            self.high_score = self.score_value
            with open("HighScore.txt","w") as file:
                file.write(f"{self.high_score}")
        self.score_value = 0
        self.update_scoreboard() 

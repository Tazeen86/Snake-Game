from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count=0
        self.color("White")
        self.penup()
        self.shape(None)
        self.goto(0,270)
        self.hideturtle()
        self.write("Score: 0",align="center",font=("Arial",24,"bold"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Arial",24,"bold"))
    def increaseCount(self):
       self.count+=1
       self.clear()
       self.write("Score:"+str(self.count),align="center",font=("Arial",24,"bold"))
from turtle import Turtle , Screen
from random import randint


screen = Screen()
screen.setup(width=500 , height=400)
user_bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win? Enter a color: ")
colors = ["yellow","red","black","blue","green"]
race_turtles ={}
count = 0
winner = "1"

for i in range(len(colors)):
    race_turtles[colors[i]] =Turtle('turtle')
    race_turtles[colors[i]].color(colors[i])
    race_turtles[colors[i]].penup()
    race_turtles[colors[i]].goto(x=-230,y=-100 + (i*40))


for _ in range(2000):
    race_turtles[colors[count]].forward(randint(0,10))
    count+=1
    if count == len(colors):
        count=0
    if race_turtles[colors[count]].xcor()>=250:
        winner = colors[count]
        break

if user_bet == winner:
    print(" you have won ")
else:
    print("you have lost")




screen.exitonclick()

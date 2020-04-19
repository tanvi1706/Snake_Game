import turtle
import time
import random
delay = 0.1
#variables
score = 0
high_score = 0
#seting up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #turns off the animation on screen (turns off the screen updates)
#snake head turtle head
head = turtle.Turtle()
head.speed(0) #fastest animation speed
head.shape("square")
head.color("black")
head.penup() #do not draw on screen
head.goto(0,0) 
head.direction = "stop"
#body building
segments = []
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score: 0 High Score: 0", align = "center", font=("Courier", 24, "normal"))



#Snake food
food = turtle.Turtle()
food.speed(0) #fastest animation speed
food.shape("circle")
food.color("red")
food.penup() #do not draw on screen
food.goto(0,100) 


#functions
def go_up(): #the only way I can go up is when im not going down
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def go_left():
    if head.direction != "right":
        head.direction = "left"  

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

#keyboard bindings
wn.listen()
wn.onkeypress(go_up, 'Up')
wn.onkeypress(go_down, 'Down')
wn.onkeypress(go_left, 'Left')
wn.onkeypress(go_right, 'Right')
#main game loop
while True:
    wn.update()
    #check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        # hide the segments
        for segment in segments:
            segment.goto(1000,1000)
        # clear the segments list
        segments.clear()
        delay = 0.1
        # Reset Score
        score = 0
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font=("Courier", 24, "normal"))



    #check for a collision with the food
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)
        #add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font=("Courier", 24, "normal"))

    # move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x,y)

    # move the segment 0 after where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)


    move()

    #check for self-collisions 
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            # hide the segments
            for segment in segments:
                segment.goto(1000,1000)
            # clear the segments list
            segments.clear()
            score = 0
            pen.clear()
            pen.write("Score: {} High Score: {}".format(score, high_score), align = "center", font=("Courier", 24, "normal"))

            delay = 0.1



    time.sleep(delay)

wn.mainloop() #will keep the screen open
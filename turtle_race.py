import turtle
import random
import time

WIDTH,HEIGHT = 500,500
colors = ['red','blue','green','yellow','pink','black','orange','violet','purple','cyan','brown']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input('enter the numbers of racers between (2-10) :' )
        if racers.isdigit():
            racers = int(racers)
        else:
            print('Input is not numeric..')
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print('Racers numbers are not between 2-10')


def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH,HEIGHT)
    screen.title('Turtle Race..')

def race(color):
    turtles = create_turtle(color)

    while True:
        for racers in turtles:
            distance = random.randrange(1,20)
            racers.forward(distance)

            x,y = racers.pos()
            if y >= HEIGHT//2 -10:
                return color[turtles.index(racers)]


def create_turtle(colors):
    turtles = []
    spacingx = WIDTH // (len(colors)+1)

    for i,color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(-WIDTH//2 + (i+1) * spacingx, -HEIGHT//2 + 20)
        racer.pendown()
        turtles.append(racer)

    return turtles

racers = get_number_of_racers()
init_turtle()

random.shuffle(colors)
color = colors[:racers]
# create_turtle(color)
winner = race(color)
print('winner is the',winner,'colored.')
time.sleep(5)


from tkinter import *
from time import *
import random

tk = Tk()
s = Canvas(tk, width=800,height=800, background="yellow")
s.pack()

#Initializes variables
xStart = 100
yStart = 400
xSpeed = 30
ySpeed = -20

xStart2 = 200
yStart2 = 500
xSpeed2 = 40
ySpeed2 = -30

#Function for a random hexadecimal to use as a colour
def hexadecimal():
    hexadecimal = "#"
    for i in range(0, 6):
        a = random.randint(48, 70)
        while 58 <= a <= 64:
            a = random.randint(48,70)
        hexadecimal += chr(a)
    return hexadecimal

#Initializes variables
colour1 = hexadecimal()
colour2 = hexadecimal()

counter = 0
Width = 100
Width2 = 150
time = 0
time2 = 0

#Loops infinitely  
while True:

    #The variable time goes up by 1 in each frame and it gets reset to 0 at every collision
    time += 1
    time2 += 1
    
    #Calculate the position of the balls
    x1 = xSpeed * time + xStart
    y1 = ySpeed * time + yStart

    x3 = xSpeed2 * time2 + xStart2
    y3 = ySpeed2 * time2 + yStart2
    
    
    x2 = x1 + Width 
    y2 = y1 + Width

    x4 = x3 + Width2
    y4 = y3 + Width2

    if y2 > 750: #if the ball hits the floor
       time = 0 #reset the clock to 0 with every wall collision, so that the formula x1 = xSpeed * time + xStart is reset at time = 0
       xStart = x1
       yStart = y1
       ySpeed = -1*ySpeed #reverse the y-speed
       


    if x1 < 50: #if the ball hits the left wall
       time = 0
       xStart = x1
       yStart = y1
       xSpeed = -1*xSpeed #reverse the x-speed
       


    if y1 < 50: #if the ball hits the ceiling
       time = 0
       xStart = x1
       yStart = y1
       ySpeed = -1*ySpeed #reverse the y-speed
       


    if x2 > 750: #if the ball hits the right wall
       time = 0
       xStart = x1
       yStart = y1
       xSpeed = -1*xSpeed #reverse the x-speed


    # BALL 2    
    if y4 > 750: #if the ball hits the floor
       time2 = 0 #reset the clock to 0 with every wall collision, so that the formula x1 = xSpeed * time + xStart is reset at time = 0
       xStart2 = x3
       yStart2 = y3
       ySpeed2 = -1*ySpeed2 #reverse the y-speed
       


    if x3 < 50: #if the ball hits the left wall
       time2 = 0
       xStart2 = x3
       yStart2 = y3
       xSpeed2 = -1*xSpeed2 #reverse the x-speed
       


    if y3 < 50: #if the ball hits the ceiling
       time2 = 0
       xStart2 = x3
       yStart2 = y3
       ySpeed2 = -1*ySpeed2 #reverse the y-speed
       


    if x4 > 750: #if the ball hits the right wall
       time2 = 0
       xStart2 = x3
       yStart2 = y3
       xSpeed2 = -1*xSpeed2 #reverse the x-speed

    #Create the balls
    Ball = s.create_oval(x1, y1, x2, y2, fill=colour1, outline="black")
    Ball2 = s.create_oval(x3, y3, x4, y4, fill = colour2, outline = "black")

    #overlap returns a tuple of overlapping stuff in s
    overlap = s.find_overlapping(x1, y1, x2, y2)
    #If any stuff is overlapping in s then change colours
    if len(overlap) > 1:
        #Counter makes sure balls don't change colour more than once when they intersect
        if counter == 0:
            counter += 1
            #New random colours
            colour1 = hexadecimal()
            colour2 = hexadecimal()
    #overlap always returns a tuple with len 1 (has an incrementing number)
    #If it does this then there is nothing overlapping and counter can be reset to 0
    elif len(overlap) == 1:
        counter = 0
    #Update!
    s.update()
    #Sleep!
    sleep(0.07)
    #Delete!
    s.delete(Ball, Ball2)


from tkinter import *
from time import *
# intput is a function that forces the user to enter a positive integer as the input
def intput(x):
    try:
        y = int(input(x))
        if y > 0:
            return y
        else:
            print("Invalid Input!", end = " ")
            return(intput(x))
    except ValueError:
        print("Invalid Input!", end = " ")
        return(intput(x))

#variables to use for making screen
width = 800
height = 800
#Initializes screen
root = Tk()
screen = Canvas(root, width=width, height=height, background = "deep sky blue" )
screen.pack()

#Initializes variables
cur = 0 #current ball number
recth = 50 #height of ground

#Introduces program and gets user input
print("Welcome to the snow ball stack generator!")
d = intput("Enter starting diameter (natural numbers only): ")
deltaD = intput("Enter rate of shrinking (natural numbers only): ")

#Creates ground
screen.create_rectangle(-10, height-recth, width + 10, height + 10, fill = "white")
#Loops from d to 0 in increments of -deltaD
for i in range(d, 0, -deltaD):
    #Updates current ball number
    cur += i
    #Calculates x and y values of the current ball and draws it
    x1 = width/2 - i/2
    x2 = width/2 + i/2
    y1 = height - cur - recth
    y2 = height - cur + i - recth
    screen.create_oval(x1, y1, x2, y2, fill = "white")
screen.update()

#NOTE: I will hand in the formula for the height and its reasoning on Tuesday

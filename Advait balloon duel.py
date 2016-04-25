import time
from tkinter import *
import math
from math import pi
import cmath, math
myInterface = Tk()
s = Canvas(myInterface, width=800, height=800, background="yellow")
s.pack()
# intput is a function that forces the user to enter a positive float as the input
def intput(x):
    try:
        y = float(input(x))
        if y > 0:
            return y
        else:
            print("Invalid Input!", end = " ")
            return(intput(x))
    except ValueError:
        print("Invalid Input!", end = " ")
        return(intput(x))

print("Welcome to the water balloon duel game! Players will take turns trying to hit each other's bases (marked in red) with water balloons by entering the desired horizontal velocity and the desired initial vetical velocity. Have fun!")
#Helper function that calculates the smaller angle between two lines
def angle(m1, m2):
    if isPerpendicular(m1, m2) == True:
        return 90
    elif m1 == "undefined" or m2 == "undefined":
        if m1 == "undefined" and m2 == "undefined":
            return 0
        elif m1 == "undefined":
            tanAngle = abs(m2)
            angleRadians = math.atan(tanAngle)
            angleDegrees = angleRadians * (180/pi)
            return angleDegrees
        else:
            tanAngle = abs(m1)
            angleRadians = math.atan(tanAngle)
            angleDegrees = angleRadians * (180/pi)
            return angleDegrees
    else:
        tanAngle = abs((m1 - m2) / (1 + m1 * m2))
        angleRadians = math.atan(tanAngle)
        angleDegrees = angleRadians * (180/pi)
        return angleDegrees
#Helper function that returns whether two lines are perpendicular or not (True or False)
def isPerpendicular(m1, m2):
    if m1 == "undefined" or m2 == "undefined":
        if m1 == 0 or m2 == 0:
            return True
        else:
            return False
    else:
        if m1 * m2 == -1:
            return True
        else:
            return False
#Setting the scene (ground and player bases)
s.create_rectangle(-50, 700, 850, 850, fill = "green")
s.create_rectangle(0, 700, 100, 750, fill = "red")
s.create_rectangle(700, 700, 800, 750, fill = "red")
s.update()
#Player 1 is always on left side
turn = "l"
#Runs infinitely until broken (a player wins)
while True:
    #Takes input from user
    vix = intput("Please enter the horizontal velocity: ")
    viy = intput("Please enter the initial vertical velocity: ")
    #Initializing variables
    x = 0
    y = 0
    #Find final time using a projectile motion formula
    ft = -2*viy/-9.8
    #Checking whose turn it is
    #NOTE: I have commented the Player 1's turn part of the program only since the Player 2's turn part of the program is very similar
    if turn  == "l":
        #Setting final x coordinate
        fx = vix*ft
        for i in range(0, int(fx) + 1):
            #Checks if ball not viewable on screen (if so then stop displaying and calculating)
            if x <= 820:
                #t is time 
                t = ft/fx * i
                #Find current x and y values using projectile motion formulas
                x = vix * t + 50
                y = -1*(viy * t + 0.5*-9.8*t**2) + 700
                #If on frame one or 2 then save x and y coordinates to calculate the cannon angle
                if i == 0:
                    x1 = x
                    y1 = y
                elif i == 1:
                    x2 = x
                    y2 = y
                    #Slope of the line between the first two frames' coordinates 
                    ml12 = (y2-y1)/(x2-x1)
                    #Slope of the ground
                    mg = 0
                    #Angle between ground and line
                    anglec = angle(ml12, mg)
                    #Coordinates of base rectangle for cannon
                    x1c = 50
                    y1c = 700
                    x2c = 100
                    y2c = 700
                    x3c = 100
                    y3c = 675
                    x4c = 50
                    y4c = 675
                    #anglec in radians
                    rangle = anglec * pi/180.0
                    #list of the coordinates of the base rectangle for cannon
                    coordinates = [[x1c, y1c], [x2c, y2c], [x3c, y3c], [x4c, y4c]]
                    #anglec expressed as a complex number (to do calculations
                    cangle = cmath.exp(-rangle*1j)
                    #Point of rotation expressed as a complex number 
                    center = complex(50, 700)
                    #Initialiaze new coordinates list for the coordinates of the cannon
                    newcoords = []
                    #Loop through (x,y) pairs in the list
                    for x, y in coordinates:
                        #v consists of the x and y values of the rotated coordinate in its real and imaginary parts respectively
                        v = cangle * (complex(x, y) - center) + center
                        #Add the (x,y) pair to the coordinates list
                        newcoords.append([v.real, v.imag])
                    #Draw a wheel (always the same)
                    wheel = s.create_oval(37.5, 675, 62.5, 700, fill = "black")
                    #Draw the cannon using newcoords list
                    cannon = s.create_polygon(newcoords, fill = "brown")
                #Draw the balloon using calculated (x,y) coordinates
                balloon = s.create_oval(x-5, y-5, x+5, y+5, fill = "deep sky blue")
                #Update, sleep and delete 
                s.update()
                time.sleep(0.002)
                s.delete(balloon)
            else:
                break
        #At the end of turn delete cannon and wheel
        s.delete(cannon, wheel)
        s.update()
    else:
        vix = -vix
        fx = 650 - vix*ft
        for i in range(0, int(fx) + 1):
            if x >= -20:
                t = ft/fx * i
                x = vix * t + 750
                y = -1*(viy * t + 0.5*-9.8*t**2) + 700
                if i == 0:
                    x1 = x
                    y1 = y
                elif i == 1:
                    x2 = x
                    y2 = y
                    ml12 = (y2-y1)/(x2-x1)
                    mg = 0
                    anglec = angle(ml12, mg)
                    x1c = 750
                    y1c = 700
                    x2c = 700
                    y2c = 700
                    x3c = 700
                    y3c = 675
                    x4c = 750
                    y4c = 675
                    rangle = anglec * pi/180.0
                    coordinates = [[x1c, y1c], [x2c, y2c], [x3c, y3c], [x4c, y4c]]
                    cangle = cmath.exp(rangle*1j)
                    center = complex(750, 700)
                    newcoords = []
                    for x, y in coordinates:
                        v = cangle * (complex(x, y) - center) + center
                        newcoords.append([v.real, v.imag])
                    wheel = s.create_oval(737.5, 675, 762.5, 700, fill = "black")
                    cannon = s.create_polygon(newcoords, fill = "brown")
                balloon = s.create_oval(x-5, y-5, x+5, y+5, fill = "deep sky blue")
                s.update()
                time.sleep(0.0001)
                s.delete(balloon)
            else:
                break
        s.delete(cannon, wheel)
        s.update()
    #Checks if the player playing his/her turn has won
    if turn == "l":
        if 700 <= x <= 800:
            print("Player 1 Wins!")
            break
    elif turn == "r":
        if 0 <= x <= 100:
            print("Player 2 Wins!")
            break
    #Checks whose turn it is 
    if turn == "r":
        turn = "l"
        print("Player 1's turn!")
    else:
        turn = "r"
        print("Player 2's turn!")

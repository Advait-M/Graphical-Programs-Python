from tkinter import *

root = Tk()
screen = Canvas(root, width=800, height=800, background = "white" )
screen.pack()

# intput is a function that forces the user to enter a positive integer less than 8 as the input
def intput(x):
    try:
        y = int(input(x))
        if y < 8 and y > 0:
            return y
        else:
            print("Invalid Input!", end = " ")
            return(intput(x))
    except ValueError:
        print("Invalid Input!", end = " ")
        return(intput(x))

#Takes input from user
rows = intput("Enter number of rows (max is 7): ")
#Initializes variables
wallWidth = 600
wallHeight = rows * 100
boxHeight = wallHeight/rows
textSize = 45
#Loops through rows
for rowNum in range(0, rows + 1):
    #Checks if first row (dont want to divide by 2^-1)
    if rowNum == 0:
        boxWidth = wallWidth
    else:
        boxWidth = wallWidth / (2**(rowNum-1))
    #Sets the y values of the boxes in the row
    y1 = boxHeight * (rowNum-1)
    y2 = y1 + boxHeight
    #Sets the y values of the text in the row
    texty = (y1 + y2) / 2
    #The following line uses dynamic textSize (not linear) based on the box
##    textSize = int(min(boxWidth, boxHeight) * 0.5)
    #Increments textSize
    textSize -= 5
    #Makes font variable that dictates type of text displayed
    font = "Times " + str(textSize) + " bold"
    #Loops through columns
    for colNum in range(0, 2**(rowNum)):
        #Sets x values of boxes
        x1 = boxWidth * (colNum-1)
        x2 = x1 + boxWidth
        #Makes sure boxes don't go beyond width of the wall
        if x2 <= wallWidth:
            #Creates boxes and inserts text into their centers 
            screen.create_rectangle(x1, y1, x2, y2, fill = "yellow", outline = "blue")
            textx = (x1 + x2) / 2
            screen.create_text(textx, texty, text = str(colNum), font = font)
            screen.update()
        

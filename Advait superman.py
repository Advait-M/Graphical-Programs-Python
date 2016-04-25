from tkinter import *
import time
myInterface = Tk()
s = Canvas(myInterface, width=800, height=800, background="deep sky blue")
s.pack()

spacing = 50
for x in range(0, 800, spacing): 
    s.create_line(x, 10, x, 800, fill="black")
    s.create_text(x, 0, text=str(x), font="Times 8", anchor = N)

for y in range(0, 800, spacing):
    s.create_line(20, y, 800, y, fill="black")
    s.create_text(4, y, text=str(y), font="Times 8", anchor = W)
#s.create_polygon(100, 100, 150, 50, 200, 75, 200, 100, 250, 125, 200, 150, 175, 175, 125, 150, fill = "white", smooth = "true")
def cloud(x, y, col):
    s.create_oval(125+x, 50+y, 175+x, 100+y, fill = col, outline = col)
    s.create_oval(100+x, 75+y, 150+x, 125+y, fill = col, outline = col)
    s.create_oval(125+x, 100+y, 175+x, 150+y, fill = col, outline = col)
    s.create_oval(150+x, 50+y, 200+x, 100+y, fill = col, outline = col)
    s.create_oval(150+x, 100+y, 200+x, 150+y, fill = col, outline = col)
    s.create_oval(175+x, 75+y, 225+x, 125+y, fill = col, outline = col)
    s.create_oval(125+x, 75+y, 200+x, 125+y, fill = col, outline = col)

def bush(x, y, col):
    s.create_oval(125+x, 50+y, 175+x, 100+y, fill = col, outline = col)
    s.create_oval(100+x, 75+y, 150+x, 125+y, fill = col, outline = col)
    s.create_oval(150+x, 50+y, 200+x, 100+y, fill = col, outline = col)
    s.create_oval(175+x, 75+y, 225+x, 125+y, fill = col, outline = col)
    s.create_oval(125+x, 75+y, 200+x, 125+y, fill = col, outline = col)
    s.create_rectangle(100+x, 100+y, 225+x, 125+y, fill = col, outline = col)
s.create_oval(700, 50, 800, 150, fill = "yellow", outline = "yellow")
s.create_rectangle(-10, 700, 810, 810, fill = "light green", outline = "green")
cloud(0, 0, "white")
cloud(100, 100, "white")
cloud(300, 50, "white")
cloud(400, 200, "white")
cloud(500, 75, "white")
#bush(50, 575, "green")
#bush(500, 575, "green")

def building(x1, y1, x2, y2, bcol, wcol, wheight, wwidth, steph, stepw):
    s.create_rectangle(x1, y1, x2, y2, fill = bcol)
    for e in range(y1 + 5, y2 - 10, steph):
        for f in range(x1 + 5, x2 - 10, stepw):
            s.create_rectangle(f, e, f + wwidth, e + wheight, fill = wcol)
building(100, 250, 200, 700, "purple", "yellow", 10, 7, 20, 20)
building(300, 400, 450, 700, "black", "yellow", 7, 10, 20, 15)
building(600, 350, 700, 700, "gray", "yellow", 10, 10, 15, 20)
building(500, 75, 550, 700, "brown", "yellow", 7, 10, 20, 15)

s.update()
x1 = -25
x2 = x1 + 100
y1 = 100
y2 = y1 + 50
p = 1

for i in range(0, 600):
    if i  >= 399:
        while y2 <= 700:
            y1 += p
            y2 += p
            p += 1
            xh2 = x2 + 25
            yh1 = y1 + 15
            yh2 = yh1 + 20
            
            xl1 = x1 - 75
            yl1 = y1 + 10
            yl2 = yl1 + 20

            xa1 = x1 + 30
            xa2 = xa1 + 60
            ya1 = y1 + 10
            ya2 = ya1 + 15

            xe1 = x2 + 17
            xe2 = xe1 + 5
            ye1 = y1 + 20
            ye2 = ye1 + 5

            xc1 = x1 - 10
            yc1 = y1 - 30
            xc2 = x2
            yc2 = y1
            xc3 = x2 - 20
            yc3 = y1
            xc4 = xc1
            yc4 = yc1 + 10

            xs1 = x2 - 20
            ys1 = y2 - 10
            xs2 = xs1 - 10
            ys2 = ys1 - 5
            xs3 = xs2
            ys3 = ys2 + 5
            xs4 = xs3 - 10
            ys4 = ys3 - 5

            box = s.create_rectangle(x1, y1, x2, y2, fill = "blue")
            head = s.create_rectangle(x2, yh1, xh2, yh2, fill = "blanched almond")
            eye = s.create_rectangle(xe1, ye1, xe2, ye2, fill = "black")
            legs = s.create_rectangle(xl1, yl1, x1, yl2, fill = "red")
            arm = s.create_rectangle(xa1, ya1, xa2, ya2, fill = "blanched almond")
            cape = s.create_polygon(xc1, yc1, xc2, yc2, xc3, yc3, xc4, yc4, fill = "red")
            slogo = s.create_line(xs1, ys1, xs2, ys2, xs3, ys3, xs4, ys4, fill = "red", width = 4)
            s.update()
            time.sleep(0.01)
            if y2 >= 700:
                pass
            else:
                s.delete(box, head, legs, arm, eye, cape, slogo)#topLeg, bottomLeg)
    else:
        x1 += 1
        x2 += 1
        
        xh2 = x2 + 25
        yh1 = y1 + 15
        yh2 = yh1 + 20
        
        xl1 = x1 - 75
        yl1 = y1 + 10
        yl2 = yl1 + 20

        xa1 = x1 + 30
        xa2 = xa1 + 60
        ya1 = y1 + 10
        ya2 = ya1 + 15

        xe1 = x2 + 17
        xe2 = xe1 + 5
        ye1 = y1 + 20
        ye2 = ye1 + 5

        xc1 = x1 - 10
        yc1 = y1 - 30
        xc2 = x2
        yc2 = y1
        xc3 = x2 - 20
        yc3 = y1
        xc4 = xc1
        yc4 = yc1 + 10

        xs1 = x2 - 20
        ys1 = y2 - 10
        xs2 = xs1 - 10
        ys2 = ys1 - 5
        xs3 = xs2
        ys3 = ys2 + 5
        xs4 = xs3 - 10
        ys4 = ys3 - 5

        box = s.create_rectangle(x1, y1, x2, y2, fill = "blue")
        head = s.create_rectangle(x2, yh1, xh2, yh2, fill = "blanched almond")
        eye = s.create_rectangle(xe1, ye1, xe2, ye2, fill = "black")
        legs = s.create_rectangle(xl1, yl1, x1, yl2, fill = "red")
        arm = s.create_rectangle(xa1, ya1, xa2, ya2, fill = "blanched almond")
        cape = s.create_polygon(xc1, yc1, xc2, yc2, xc3, yc3, xc4, yc4, fill = "red")
        slogo = s.create_line(xs1, ys1, xs2, ys2, xs3, ys3, xs4, ys4, fill = "red", width = 4)
        s.update()
        time.sleep(0.01)
        s.delete(box, head, legs, arm, eye, cape, slogo)#topLeg, bottomLeg)

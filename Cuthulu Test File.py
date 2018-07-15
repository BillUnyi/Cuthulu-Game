from graphics import *
from vlc import *

def main():
    win = GraphWin("Cuthulu", 1920, 1080)
    win.setBackground("Black")
    title = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Title Screen.png")
    background1 = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Background1.png")
    background2 = Image(Point(win.getWidth() // 2, win.getHeight() // 2 - 1080), "Background2.png")
    background3 = Image(Point(win.getWidth() // 2, win.getHeight() // 2 - 1080), "Background3.png")
    ground1 = Image(Point(win.getWidth() // 2, 1000), "ground1.png")
    ground2 = Image(Point(win.getWidth() // 2, 1000 - 2000), "ground2.png")
    tomR = Image(Point(win.getWidth() // 2, 835), "Tom Hernandez R.png")
    tomL = Image(Point(win.getWidth() // 2, 835 - 1080), "Tom Hernandez L.png")
    timer = 0
    title.draw(win)
    while win.checkMouse() == None:
        timer += 1
    title.undraw()
    background1.draw(win)
    background2.draw(win)
    background3.draw(win)
    ground1.draw(win)
    ground2.draw(win)
    tomR.draw(win)
    tomL.draw(win)
    x = 0
    b = 1
    g = 1
    p = "r"
    jump = False
    counter = 0
    while True:
        if win.checkKey() == "a" and x > -1540:
            if p == "r":
                tomR.move(0, -1080)
                tomL.move(0, 1080)
            background1.move(2, 0)
            background2.move(2, 0)
            background3.move(2, 0)
            ground1.move(10, 0)
            ground2.move(10, 0)
            x -= 2
            p = "l"
            print(x)
        elif win.checkKey() == "d" and x < 1540:
            if p == "l":
                tomL.move(0, -1080)
                tomR.move(0, 1080)
            background1.move(-2, 0)
            background2.move(-2, 0)
            background3.move(-2, 0)
            ground1.move(-10, 0)
            ground2.move(-10, 0)
            x += 2
            p = "r"
            print(x)
        if win.checkMouse() and jump == False:
            jump = True
        if jump == True:
            if counter < 25:
                tomR.move(0, -10)
                tomL.move(0, -10)
            elif counter < 30:
                tomR.move(0, -8)
                tomL.move(0, -8)
            elif counter < 35:
                tomR.move(0, -6)
                tomL.move(0, -6)
            elif counter < 40:
                tomR.move(0, -4)
                tomL.move(0, -4)
            elif counter < 45:
                tomR.move(0, -2)
                tomL.move(0, -2)
            elif counter < 50:
                tomR.move(0, 0)
                tomL.move(0, 0)
            elif counter < 55:
                tomR.move(0, 2)
                tomL.move(0, 2)
            elif counter < 60:
                tomR.move(0, 4)
                tomL.move(0, 4)
            elif counter < 65:
                tomR.move(0, 6)
                tomL.move(0, 6)
            elif counter < 70:
                tomR.move(0, 8)
                tomL.move(0, 8)
            elif counter < 94:
                tomR.move(0, 10)
                tomL.move(0, 10)
            else:
                counter = 0
                jump = False
            counter += 1

        if win.checkKey() == "1" and b != 1:
            background1.move(0, 1080)
            ground1.move(0, 2000)
            ground2.move(0, -2000)
            if b == 2:
                background2.move(0, -1080)
            elif b == 3:
                background3.move(0, -1080)
            b = 1
            g = 1
        elif win.checkKey() == "2" and b != 2:
            background2.move(0, 1080)
            if b == 1:
                background1.move(0, -1080)
                ground1.move(0, -2000)
                ground2.move(0, 2000)
            elif b == 3:
                background3.move(0, -1080)
            b = 2
            g = 2
        elif win.checkKey() == "3" and b != 3:
            background3.move(0, 1080)
            if b == 1:
                background1.move(0, -1080)
                ground1.move(0, -2000)
                ground2.move(0, 2000)
            elif b == 2:
                background2.move(0, -1080)
            b = 3
            g = 2
        time.sleep(.02)

main()

from graphics import *
from vlc import *
import random

def main():
    win = GraphWin("Cuthulu", 1920, 1080)
    win.setBackground("Black")
    menuTheme = MediaPlayer("Downlink - Gamma Ray Burst.wav")
    title = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Title Screen.png")
    start = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Start.png")
    nightTheme = MediaPlayer("Night Theme.wav")
    background1 = Image(Point(win.getWidth() // 2, win.getHeight() // 2 - 1080), "Background1.png")
    background2 = Image(Point(win.getWidth() // 2, win.getHeight() // 2), "Background2.png")
    background3 = Image(Point(win.getWidth() // 2, win.getHeight() // 2 - 1080), "Background3.png")
    ground1 = Image(Point(win.getWidth() // 2, 1000 - 2000), "ground1.png")
    ground2 = Image(Point(win.getWidth() // 2, 1000), "ground2.png")
    tomR = Image(Point(win.getWidth() // 2, 830), "Tom Hernandez R.png")
    tomL = Image(Point(win.getWidth() // 2, 830 - 1080), "Tom Hernandez L.png")
    dayTheme = MediaPlayer("Virtual Riot - Energy Drink.mp3")
    cuthuluTheme = MediaPlayer("Cuthulu Theme.mp3")
    title.draw(win)
    start.draw(win)
    Start = False
    X = 0
    Y = 0
    timer = 0
    menuTheme.play()
    while not Start:
        Z = X
        W = Y
        x = random.randrange(7) - 3
        y = random.randrange(7) - 3
        X += x
        Y += y
        if 50 > X > -50 and 50 > Y > -50:
            title.move(x, y)
            timer += 1
            if timer % 1900 == 1899:
                menuTheme.stop()
                menuTheme.play()
            time.sleep(.01)
        else:
            X = Z
            Y = W
        pos = win.checkMouse()
        if pos != None:
            if 1095 > pos.getX() > 825 and 585 > pos.getY() > 490:
                Start = True
    title.undraw()
    start.undraw()
    menuTheme.stop()
    background1.draw(win)
    background2.draw(win)
    background3.draw(win)
    ground1.draw(win)
    ground2.draw(win)
    tomR.draw(win)
    tomL.draw(win)
    x = 0
    y = 0
    b = 2
    g = 2
    p = "r"
    Wave = 1
    jump = False
    floor = True
    ceiling = False
    wallL = False
    wallR = False
    counter = 0
    timer = 0
    Timer = "2"
    if timer % 100 == 0:
        hour = (timer // 6000) % 12
        minute = (timer // 100) % 60
        if timer % 144000 < 72000:
            ampm = "AM"
        else:
            ampm = "PM"
        if hour == 0:
            hour = "12"
        if minute < 10:
            minute = "0" + str(minute)
        clock = Text(Point(120, 40), str(hour) + ":" + str(minute) + " " + str(ampm))
        clock.setTextColor("White")
        clock.setSize(36)
        clock.setFace("times roman")
        clock.setStyle("bold italic")
        clock.draw(win)
    while True:
        if win.checkKey() == "a" and x > -1540 and wallL == False:
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
        elif win.checkKey() == "d" and x < 1540 and wallR == False:
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
        if win.checkMouse() and jump == False:
            jump = True
            floor = False
        if jump == True:
            if counter < 25 and ceiling == False:
                tomR.move(0, -10)
                tomL.move(0, -10)
                y += 10
            elif counter < 30 and ceiling == False:
                tomR.move(0, -8)
                tomL.move(0, -8)
                y += 8
            elif counter < 35 and ceiling == False:
                tomR.move(0, -6)
                tomL.move(0, -6)
                y += 6
            elif counter < 40 and ceiling == False:
                tomR.move(0, -4)
                tomL.move(0, -4)
                y += 4
            elif counter < 45 and ceiling == False:
                tomR.move(0, -2)
                tomL.move(0, -2)
                y += 2
            elif counter < 50:
                tomR.move(0, 0)
                tomL.move(0, 0)
            elif counter < 55 and floor == False:
                tomR.move(0, 2)
                tomL.move(0, 2)
                y -= 2
            elif counter < 60 and floor == False:
                tomR.move(0, 4)
                tomL.move(0, 4)
                y -= 4
            elif counter < 65 and floor == False:
                tomR.move(0, 6)
                tomL.move(0, 6)
                y -= 6
            elif counter < 70 and floor == False:
                tomR.move(0, 8)
                tomL.move(0, 8)
                y -= 8
            elif floor == False:
                tomR.move(0, 10)
                tomL.move(0, 10)
                y -= 10
            else:
                counter = 0
                jump = False
            counter += 1
        if timer == 36000:
            Timer = "1"
        elif timer == 120000:
            Timer = "2"
        elif timer == 144000:
            Timer = "3"
        if Timer == "1" and b != 1:
            background1.move(0, 1080)
            ground1.move(0, 2000)
            ground2.move(0, -2000)
            if b == 2:
                background2.move(0, -1080)
            elif b == 3:
                background3.move(0, -1080)
            b = 1
            g = 1
        elif Timer == "2" and b != 2:
            background2.move(0, 1080)
            if b == 1:
                background1.move(0, -1080)
                ground1.move(0, -2000)
                ground2.move(0, 2000)
            elif b == 3:
                background3.move(0, -1080)
            b = 2
            g = 2
        elif Timer == "3" and b != 3:
            background3.move(0, 1080)
            if b == 1:
                background1.move(0, -1080)
                ground1.move(0, -2000)
                ground2.move(0, 2000)
            elif b == 2:
                background2.move(0, -1080)
            b = 3
            g = 2
        if y <= 0:
            floor = True
        if timer % 100 == 0:
            hour = (timer // 6000) % 12
            minute = (timer // 100) % 60
            if timer % 144000 < 72000:
                ampm = "AM"
            else:
                ampm = "PM"
            if hour == 0:
                hour = "12"
            if minute < 10:
                minute = "0" + str(minute)
            clock.undraw()
            clock = Text(Point(120, 40), str(hour) + ":" + str(minute) + " " + str(ampm))
            clock.setTextColor("White")
            clock.setSize(36)
            clock.setFace("times roman")
            clock.setStyle("bold italic")
            clock.draw(win)

        if timer == 144000:
            wave = Text(Point(80, 90), "Wave " + str(Wave))
            wave.setTextColor("White")
            wave.setSize(20)
            wave.setFace("times roman")
            wave.setStyle("bold italic")
            wave.draw(win)

        if timer >= 144000:
            if (timer - 144000) % 1000 == 998:
                Wave += 1
                wave.undraw()
                wave = Text(Point(80, 90), "Wave " + str(Wave))
                wave.setTextColor("White")
                wave.setSize(20)
                wave.setFace("times roman")
                wave.setStyle("bold italic")
                wave.draw(win)
        if b == 1:
            if (timer - 36000) % 30000 == 2:
                dayTheme.stop()
                dayTheme.play()
        else:
            dayTheme.stop()
        if b == 2:
            if timer % 8700 == 2:
                nightTheme.stop()
                nightTheme.play()
        else:
            nightTheme.stop()
        if b == 3:
            if (timer - 144000) % 21000 == 2:
                cuthuluTheme.stop()
                cuthuluTheme.play()
        else:
            cuthuluTheme.stop()
        timer += 2
        time.sleep(.02)

main()

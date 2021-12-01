from tkinter import *
from turtle import TurtleScreen
import Utils
import MainGUI
import Drawings

def drawGUI(daydate):
    #                            Create frame                               #

    root = Tk()

    #                 Initialisation of some useful variables                #

    lastClickX = 0
    lastClickY = 0

    movePicture = PhotoImage(file=Utils.getResourcesPath("resources\\drawing_move.png"))

    reducePicture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\drawing_reduce.png"))
    closePicture = PhotoImage(file=Utils.getResourcesPath("resources\\buttons\\drawing_close.png"))

    #                Initialisation of some useful functions                #

    def moveFrame(event):
        x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
        root.geometry("+%s+%s" % (x, y))

    def mappedFrame(event):
        root.overrideredirect(True)

    def reduceFrame():
        Utils.buttonClick()
        root.state('withdrawn')
        root.overrideredirect(False)
        root.state('iconic')

    def closeFrame():
        Utils.buttonClick()
        root.destroy()
        MainGUI.mainGUI()

    #                      Set frame basics parameters                       #

    root.wm_attributes("-topmost", 1)
    root.geometry("600x400")
    root.resizable(width=False, height=False)
    root.iconbitmap(Utils.getResourcesPath("resources\\icons\\icon.ico"))
    root.bind("<Map>", mappedFrame)

    #                        Add components to frame                         #

    background = Canvas(height=400, width=600, highlightthickness=0)
    background.place(x=0, y=0)

    move_area = Label(background, image=movePicture, width=20, height=20, bd=0)
    move_area.place(x=0, y=0)
    move_area.bind("<B1-Motion>", moveFrame)

    button_reduce = Button(background, image=reducePicture, bd=0, highlightthickness=0, padx=30, pady=20, command=reduceFrame)
    button_reduce.place(x=550, y=0)

    button_close = Button(background, image=closePicture, bd=0, highlightthickness=0, padx=20, pady=20, command=closeFrame)
    button_close.place(x=580, y=0)

    drawArea = TurtleScreen(background)
    drawArea.bgpic(Utils.getResourcesPath("resources\\drawing_background.png"))

    try:
        if daydate == 1:
            Drawings.title(drawArea, -150, 0, 25)
        elif daydate == 2:
            Drawings.snowStar(drawArea, 0, 0, 0.5)
        elif daydate == 3:
            Drawings.fractalChristmasTree(drawArea, 0, 0, 30)
        elif daydate == 4:
            Drawings.starStyle2(drawArea, 0, 0, 0.5)
        elif daydate == 5:
            Drawings.snowMan(drawArea, 0, -20, 1)
        elif daydate == 6:
            Drawings.startStyle1(drawArea, -80, 30, 2)
        elif daydate == 7:
            Drawings.geometricChristmasTree(drawArea, 0, 20, 1.5, "green")
        elif daydate == 8:
            pass
        elif daydate == 9:
            pass
        elif daydate == 10:
            pass
        elif daydate == 11:
            pass
        elif daydate == 12:
            pass
        elif daydate == 13:
            pass
        elif daydate == 14:
            pass
        elif daydate == 15:
            pass
        elif daydate == 16:
            pass
        elif daydate == 17:
            pass
        elif daydate == 18:
            pass
        elif daydate == 19:
            pass
        elif daydate == 20:
            pass
        elif daydate == 21:
            pass
        elif daydate == 22:
            pass
        elif daydate == 23:
            pass
        elif daydate == 24:
            Drawings.finalCard(drawArea, -300, -200)

    except:
        pass

    #                          Loop the frame                           #

    root.mainloop()
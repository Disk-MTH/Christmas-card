import tkinter
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
            Drawings.title(drawArea, 25)
        if daydate == 2:
            Drawings.fractalChristmasTree(drawArea, 30)
        if daydate == 3:
            Drawings.starStyle2(drawArea, 0.5)
        if daydate == 4:
            Drawings.snowStar(drawArea, 0.5)
        if daydate == 5:
            Drawings.snowMan(drawArea, 1)
        if daydate == 6:
            pass
        if daydate == 7:
            pass
        if daydate == 8:
            pass
        if daydate == 9:
            pass
        if daydate == 10:
            pass
        if daydate == 11:
            pass

    except:
        pass

    #                          Loop the frame                           #

    root.mainloop()
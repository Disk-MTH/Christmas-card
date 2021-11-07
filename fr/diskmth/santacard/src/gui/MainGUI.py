from tkinter import *
from fr.diskmth.santacard.src.utils import Utils


def mainGUI():

    #                               Create frame                             #

    root = Tk()

    #                 Initialisation of some useful variables                #

    lastClickX = 0
    lastClickY = 0

    iconImage = PhotoImage(file=Utils.getResourcesPath() + "\\icon.png")
    backgroundImage = PhotoImage(file=Utils.getResourcesPath() + "\\background.png")
    titleBarImage = PhotoImage(file=Utils.getResourcesPath() + "\\title_bar.png")

    moveImage = PhotoImage(file=Utils.getResourcesPath() + "\\move.png")
    configImage = PhotoImage(file=Utils.getResourcesPath() + "\\config.png")
    reduceImage = PhotoImage(file=Utils.getResourcesPath() + "\\reduce.png")
    closeImage = PhotoImage(file=Utils.getResourcesPath() + "\\close.png")

    day1Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_1.png")
    day2Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_2.png")
    day3Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_3.png")
    day4Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_4.png")
    day5Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_5.png")
    day6Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_6.png")
    day7Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_7.png")
    day8Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_8.png")
    day9Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_9.png")
    day10Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_10.png")
    day11Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_11.png")
    day12Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_12.png")
    day13Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_13.png")
    day14Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_14.png")
    day15Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_15.png")
    day16Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_16.png")
    day17Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_17.png")
    day18Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_18.png")
    day19Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_19.png")
    day20Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_20.png")
    day21Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_21.png")
    day22Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_22.png")
    day23Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_23.png")
    day24Image = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\day_24.png")

    #                Initialisation of some useful functions                #

    def moveFrame(event):
        x, y = event.x - lastClickX + root.winfo_x(), event.y - lastClickY + root.winfo_y()
        root.geometry("+%s+%s" % (x, y))

    def mappedFrame(event=None):
        root.overrideredirect(True)

    def reduceFrame():
        root.state('withdrawn')
        root.overrideredirect(False)
        root.state('iconic')

    def closeFrame():
        root.destroy()

    def createAButton(image):
        return Button(image=image, bd=0, highlightthickness=0, padx=67, pady=67, command=None)

    #                      Set frame basics parameters                       #

    root.geometry("1000x650")
    root.resizable(width=False, height=False)
    root.iconphoto(True, iconImage)
    root.bind("<Map>", mappedFrame)

    #                        Add components to frame                         #

    background = Label(root, image=backgroundImage, width=1000, height=650)
    background.place(x=0, y=0, relwidth=1, relheight=1)

    title_bar = Label(root, image=titleBarImage, width=1000, height=45, bd=0)
    title_bar.place(x=0, y=0)
    title_bar.bind("<B1-Motion>", moveFrame)

    move_area = Label(root, image=moveImage, width=43, height=43, bd=0)
    move_area = 

    button_config = Button(image=configImage, bd=0, highlightthickness=0, padx=35, pady=40, command=None)
    button_config.place(x=875, y=0)

    button_reduce = Button(image=reduceImage, bd=0, highlightthickness=0, padx=45, pady=40, command=reduceFrame)
    button_reduce.place(x=915, y=0)

    button_close = Button(image=closeImage, bd=0, highlightthickness=0, padx=40, pady=40, command=closeFrame)
    button_close.place(x=960, y=0)

    button_day_1 = createAButton(day1Image)
    button_day_1.place(x=549, y=70)

    button_day_2 = createAButton(day2Image)
    button_day_2.place(x=50, y=215)

    button_day_3 = createAButton(day3Image)
    button_day_3.place(x=216, y=215)

    button_day_4 = createAButton(day4Image)
    button_day_4.place(x=383, y=364)

    button_day_5 = createAButton(day5Image)
    button_day_5.place(x=383, y=513)

    button_day_6 = createAButton(day6Image)
    button_day_6.place(x=550, y=220)

    button_day_7 = createAButton(day7Image)
    button_day_7.place(x=714, y=69)

    button_day_8 = createAButton(day8Image)
    button_day_8.place(x=549, y=362)

    button_day_9 = createAButton(day9Image)
    button_day_9.place(x=216, y=508)

    button_day_10 = createAButton(day10Image)
    button_day_10.place(x=714, y=362)

    button_day_11 = createAButton(day11Image)
    button_day_11.place(x=50, y=508)

    button_day_12 = createAButton(day12Image)
    button_day_12.place(x=882, y=221)

    button_day_13 = createAButton(day13Image)
    button_day_13.place(x=882, y=362)

    button_day_14 = createAButton(day14Image)
    button_day_14.place(x=715, y=216)

    button_day_15 = createAButton(day15Image)
    button_day_15.place(x=382, y=69)

    button_day_16 = createAButton(day16Image)
    button_day_16.place(x=215, y=360)

    button_day_17 = createAButton(day17Image)
    button_day_17.place(x=881, y=69)

    button_day_18 = createAButton(day18Image)
    button_day_18.place(x=51, y=363)

    button_day_19 = createAButton(day19Image)
    button_day_19.place(x=383, y=215)

    button_day_20 = createAButton(day20Image)
    button_day_20.place(x=216, y=70)

    button_day_21 = createAButton(day21Image)
    button_day_21.place(x=50, y=70)

    button_day_22 = createAButton(day22Image)
    button_day_22.place(x=714, y=508)

    button_day_23 = createAButton(day23Image)
    button_day_23.place(x=879, y=507)

    button_day_24 = createAButton(day24Image)
    button_day_24.place(x=549, y=512)

    #                             Loop the frame                              #

    root.mainloop()
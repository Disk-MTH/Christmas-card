from tkinter import *
import Utils
import ConfigGUI

def mainGUI():

    #                      Create frame and init song                        #

    root = Tk()

    #                 Initialisation of some useful variables                #

    lastClickX = 0
    lastClickY = 0

    backgroundPicture = PhotoImage(file=Utils.getResourcesPath() + "\\main_background.png")
    titleBarPicture = PhotoImage(file=Utils.getResourcesPath() + "\\main_title_bar.png")
    movePicture = PhotoImage(file=Utils.getResourcesPath() + "\\main_move.png")
    creditsPicture = PhotoImage(file=Utils.getResourcesPath() + "\\main_credits.png")

    configPicture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\main_config.png")
    reducePicture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\main_reduce.png")
    closePicture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\main_close.png")

    day1Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_1.png")
    day2Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_2.png")
    day3Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_3.png")
    day4Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_4.png")
    day5Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_5.png")
    day6Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_6.png")
    day7Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_7.png")
    day8Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_8.png")
    day9Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_9.png")
    day10Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_10.png")
    day11Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_11.png")
    day12Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_12.png")
    day13Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_13.png")
    day14Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_14.png")
    day15Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_15.png")
    day16Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_16.png")
    day17Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_17.png")
    day18Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_18.png")
    day19Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_19.png")
    day20Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_20.png")
    day21Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_21.png")
    day22Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_22.png")
    day23Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_23.png")
    day24Picture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\days\\day_24.png")

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

    def openConfig():
        closeFrame()
        ConfigGUI.configGUI()

    def createAButton(image):
        return Button(image=image, bd=0, highlightthickness=0, padx=67, pady=67, command=None)

    #                      Set frame basics parameters                       #

    root.wm_attributes("-topmost", 1)
    root.geometry("1000x650")
    root.resizable(width=False, height=False)
    root.bind("<Map>", mappedFrame)

    #                        Add components to frame                         #

    background = Label(image=backgroundPicture, width=1000, height=650, bd=0)
    background.place(x=0, y=0)

    title_bar = Label(image=titleBarPicture, width=1000, height=45, bd=0)
    title_bar.place(x=0, y=0)

    credits = Label(image=creditsPicture, width=198, height=50, bd=0)
    credits.place(x=800, y=600)

    move_area = Label(image=movePicture, width=43, height=43, bd=0)
    move_area.place(x=0, y=0)
    move_area.bind("<B1-Motion>", moveFrame)

    button_config = Button(image=configPicture, bd=0, highlightthickness=0, padx=35, pady=40, command=openConfig)
    button_config.place(x=875, y=0)

    button_reduce = Button(image=reducePicture, bd=0, highlightthickness=0, padx=45, pady=40, command=reduceFrame)
    button_reduce.place(x=915, y=0)

    button_close = Button(image=closePicture, bd=0, highlightthickness=0, padx=40, pady=40, command=closeFrame)
    button_close.place(x=960, y=0)

    button_day_1 = createAButton(day1Picture)
    button_day_1.place(x=547, y=68)

    button_day_2 = createAButton(day2Picture)
    button_day_2.place(x=48, y=213)

    button_day_3 = createAButton(day3Picture)
    button_day_3.place(x=214, y=213)

    button_day_4 = createAButton(day4Picture)
    button_day_4.place(x=381, y=362)

    button_day_5 = createAButton(day5Picture)
    button_day_5.place(x=381, y=511)

    button_day_6 = createAButton(day6Picture)
    button_day_6.place(x=548, y=218)

    button_day_7 = createAButton(day7Picture)
    button_day_7.place(x=712, y=67)

    button_day_8 = createAButton(day8Picture)
    button_day_8.place(x=547, y=360)

    button_day_9 = createAButton(day9Picture)
    button_day_9.place(x=214, y=506)

    button_day_10 = createAButton(day10Picture)
    button_day_10.place(x=712, y=360)

    button_day_11 = createAButton(day11Picture)
    button_day_11.place(x=48, y=506)

    button_day_12 = createAButton(day12Picture)
    button_day_12.place(x=880, y=219)

    button_day_13 = createAButton(day13Picture)
    button_day_13.place(x=880, y=360)

    button_day_14 = createAButton(day14Picture)
    button_day_14.place(x=713, y=214)

    button_day_15 = createAButton(day15Picture)
    button_day_15.place(x=380, y=67)

    button_day_16 = createAButton(day16Picture)
    button_day_16.place(x=213, y=358)

    button_day_17 = createAButton(day17Picture)
    button_day_17.place(x=879, y=67)

    button_day_18 = createAButton(day18Picture)
    button_day_18.place(x=49, y=361)

    button_day_19 = createAButton(day19Picture)
    button_day_19.place(x=381, y=213)

    button_day_20 = createAButton(day20Picture)
    button_day_20.place(x=214, y=68)

    button_day_21 = createAButton(day21Picture)
    button_day_21.place(x=48, y=68)

    button_day_22 = createAButton(day22Picture)
    button_day_22.place(x=712, y=506)

    button_day_23 = createAButton(day23Picture)
    button_day_23.place(x=877, y=505)

    button_day_24 = createAButton(day24Picture)
    button_day_24.place(x=547, y=510)

    #                             Loop the frame                              #

    root.mainloop()
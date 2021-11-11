from tkinter import *
import Utils
import MainGUI

is_music_enable = True
if Utils.getSettingValue("music") == "enable":
    is_music_enable = True
elif Utils.getSettingValue("music") == "disable":
    is_music_enable = False

are_sound_effects_enable = True
if Utils.getSettingValue("sound_effects") == "enable":
    are_sound_effects_enable = True
elif Utils.getSettingValue("sound_effects") == "disable":
    are_sound_effects_enable = False

def configGUI():
    #                      Create frame and init song                        #

    root = Tk()

    #                 Initialisation of some useful variables                #

    lastClickX = 0
    lastClickY = 0

    backgroundPicture = PhotoImage(file=Utils.getResourcesPath() + "\\config_background.png")
    titleBarPicture = PhotoImage(file=Utils.getResourcesPath() + "\\config_title_bar.png")
    movePicture = PhotoImage(file=Utils.getResourcesPath() + "\\config_move.png")

    reducePicture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\config_reduce.png")
    closePicture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\config_close.png")
    soundOnPicture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\sound_on.png")
    soundOffPicture = PhotoImage(file=Utils.getResourcesPath() + "\\buttons\\sound_off.png")

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
        MainGUI.mainGUI()


    def toggleMusic():
        global is_music_enable
        if is_music_enable:
            toggle_music.config(image=soundOffPicture)
            Utils.setSettingValue("music", "turnOff")
            is_music_enable = False
        else:
            toggle_music.config(image=soundOnPicture)
            Utils.setSettingValue("music", "turnOn")
            is_music_enable = True

    def toggleSoundEffects():
        global are_sound_effects_enable
        if are_sound_effects_enable:
            toggle_sound_effects.config(image=soundOffPicture)
            Utils.setSettingValue("sound_effects", "turnOff")
            are_sound_effects_enable = False
        else:
            toggle_sound_effects.config(image=soundOnPicture)
            Utils.setSettingValue("sound_effects", "turnOn")
            are_sound_effects_enable = True

    def getPictureForButton(buttonName):
        if buttonName == "toggle_music":
            if is_music_enable is True:
                return soundOnPicture
            else:
                return soundOffPicture
        elif buttonName == "toggle_sound_effects":
            if are_sound_effects_enable is True:
                return soundOnPicture
            else:
                return soundOffPicture

    #                      Set frame basics parameters                       #

    root.wm_attributes("-topmost", 1)
    root.geometry("200x200")
    root.resizable(width=False, height=False)
    root.bind("<Map>", mappedFrame)

    #                        Add components to frame                         #

    background = Label(image=backgroundPicture, width=200, height=200, bd=0)
    background.place(x=0, y=0)

    title_bar = Label(image=titleBarPicture, width=200, height=30, bd=0)
    title_bar.place(x=0, y=0)

    move_area = Label(image=movePicture, width=28, height=28, bd=0)
    move_area.place(x=0, y=0)
    move_area.bind("<B1-Motion>", moveFrame)

    button_reduce = Button(image=reducePicture, bd=0, highlightthickness=0, padx=32, pady=28, command=reduceFrame)
    button_reduce.place(x=140, y=0)

    button_close = Button(image=closePicture, bd=0, highlightthickness=0, padx=28, pady=28, command=closeFrame)
    button_close.place(x=172, y=0)

    toggle_music = Button(image=getPictureForButton("toggle_music"), bd=0, highlightthickness=0, padx=40, pady=40, command=toggleMusic)
    toggle_music.place(x=30, y=50)

    toggle_sound_effects = Button(image=getPictureForButton("toggle_sound_effects"), bd=0, highlightthickness=0, padx=40, pady=40, command=toggleSoundEffects)
    toggle_sound_effects.place(x=30, y=80)

    #                          Loop the frame                           #

    root.mainloop()
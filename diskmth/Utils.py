from time import sleep
import pygame
import MainGUI

def getResourcesPath() :
    return "resources"

def getSettingValue(settingToGet) :
    with open(getResourcesPath() + "\\settings.txt", "r") as file:
        lines = file.read().split()
    if settingToGet == "music":
        return lines[2]
    elif settingToGet == "sound_effects":
        return lines[6]
    elif settingToGet == "volume":
        return lines[9]

def setSettingValue(settingToSet, toggleType):
    with open(getResourcesPath() + "\\settings.txt", "rt") as file:
        fileContent = file.read()

    if settingToSet == "music":
        if toggleType == "turnOn":
            with open(getResourcesPath() + "\\settings.txt", "wt") as file:
                fileContent = fileContent.replace("music : disable", "music : enable")
                file.write(fileContent)
        elif toggleType == "turnOff":
            with open(getResourcesPath() + "\\settings.txt", "wt") as file:
                fileContent = fileContent.replace("music : enable", "music : disable")
                file.write(fileContent)

    elif settingToSet == "sound_effects":
        if toggleType == "turnOn":
            with open(getResourcesPath() + "\\settings.txt", "wt") as file:
                fileContent = fileContent.replace("sound effects : disable", "sound effects : enable")
                file.write(fileContent)
        elif toggleType == "turnOff":
            with open(getResourcesPath() + "\\settings.txt", "wt") as file:
                fileContent = fileContent.replace("sound effects : enable", "sound effects : disable")
                file.write(fileContent)

def resetConfig():
    with open(getResourcesPath() + "\\settings.txt", "wt") as file:
        defaultSettings = ["music : enable\n", "sound effects : enable\n", "volume : 100\n"]
        index = 0
        for i in range(len(defaultSettings)):
            lineToWrite = defaultSettings[index]
            file.write(lineToWrite)
            index += 1

def launchGUI():
    MainGUI.mainGUI()


def launchSounds(GUIThread):
    isMusicActive = False
    pygame.mixer.init()
    while GUIThread.is_alive():
        if getSettingValue("music") == "enable" and isMusicActive is False:
            pygame.mixer.music.load(getResourcesPath() + "\\sounds\\background_music.mp3")
            pygame.mixer.music.play()
            isMusicActive = True
        if getSettingValue("music") == "disable" and isMusicActive is True:
            pygame.mixer.music.stop()
            isMusicActive = False
        sleep(0.25)

def testConfig(GUIThread):
    while GUIThread.is_alive():
        with open(getResourcesPath() + "\\settings.txt", "r") as file:
            lines = file.read().split()
            try:
                if lines[0] + " " + lines[1] + " " != "music : ":
                    resetConfig()
                if (lines[2] != "enable") and (lines[2] != "disable"):
                    resetConfig()
                if lines[3] + " " + lines[4] + " " + lines[5] + " " != "sound effects : ":
                    resetConfig()
                if (lines[6] != "enable") and (lines[6] != "disable"):
                    resetConfig()
                if lines[7] + " " + lines[8] + " " != "volume : ":
                    resetConfig()
                if (int(lines[9]) > 100) or (int(lines[9]) < 1):
                    resetConfig()
            except IndexError:
                resetConfig()
        sleep(0.25)
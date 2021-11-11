import MainGUI, Utils
import pygame
from threading import Thread
from time import sleep

def GUI():
    MainGUI.mainGUI()

def sounds():
    isMusicActive = False
    pygame.mixer.init()
    while SoundThread.is_alive() and GUIThread.is_alive():
        if Utils.getSettingValue("music") == "enable" and isMusicActive is False:
            pygame.mixer.music.load(Utils.getResourcesPath() + "\\sounds\\background_music.mp3")
            pygame.mixer.music.play()
            isMusicActive = True
        if Utils.getSettingValue("music") == "disable" and isMusicActive is True:
            pygame.mixer.music.stop()
            isMusicActive = False
        sleep(0.25)

if __name__ == '__main__':
    GUIThread = Thread(target=GUI, name="GUIThread")
    SoundThread = Thread(target=sounds, name="SoundThread")

    GUIThread.start()
    SoundThread.start()

    GUIThread.join()
    SoundThread.join()
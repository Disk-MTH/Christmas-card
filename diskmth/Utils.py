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
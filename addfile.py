import os

stageFileName = "stage.txt"


def addFile(folderPath, arg, currWorkingDir):
    global stageFileName

    if not (os.path.exists(folderPath + stageFileName)):
        stage = open(folderPath + stageFileName, 'w')
        stage.close()

    stage = open(folderPath + stageFileName, 'a')

    if os.path.exists(currWorkingDir + arg):
        stage.write(arg + "\n")
    else:
        print("File does not exist\n")


def removeStage(folderPath):
    global stageFileName
    os.remove(folderPath + stageFileName)

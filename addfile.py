import os

stageFileName = "stage.txt"

def addFile(folderPath, arg):
    global stageFileName

    if not (os.path.exists(folderPath + stageFileName)):
        stage = open(folderPath+stageFileName,'w')
        stage.close()

    stage = open(folderPath + stageFileName, 'a')
    stage.write(arg + "\n")


def removeStage(folderPath):
    global stageFileName
    os.remove(folderPath + stageFileName)


addFile("","tgjg")

removeStage("")
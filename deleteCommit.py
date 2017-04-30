import os
from shutil import *


def delete(logFilePath, logFileName, commitsFolderPath, commitNumber):
    folderPath = commitsFolderPath + commitNumber

    foundCommit = False
    versionsToDeleteFromLog = []
    if (os.path.exists(folderPath)):
        rmtree(folderPath)
        versionsToDeleteFromLog.append(int(commitNumber))
        foundCommit = True

    # delete all the commits after the commit specified by the user
    nextFolderNumber = int(commitNumber)
    while (True):
        nextFolderNumber = nextFolderNumber + 1
        commitFolderNumber = str(nextFolderNumber)
        folderPath = commitsFolderPath + commitFolderNumber
        if (os.path.exists(folderPath)):
            rmtree(folderPath)
            versionsToDeleteFromLog.append(int(nextFolderNumber))
        else:
            break

    if (not foundCommit):
        print("Invalid commit name")
    else:
        # remove from log
        removeFromLog(versionsToDeleteFromLog, logFilePath, logFileName)
    return foundCommit


def removeFromLog(commitVersionList, logFilePath, logFileName):
    logFile = open(logFilePath + logFileName, "r")
    lines = logFile.readlines()
    logFile.close()

    tmpFile = open(logFilePath + "tmp.txt", "w")
    tmpFile.truncate()
    for line in lines:
        tmpLine = line.split('|')
        if (int(tmpLine[0]) not in commitVersionList):
            tmpFile.write(line)

    tmpFile.close()
    os.remove(logFilePath + logFileName)
    os.rename(logFilePath + "tmp.txt", logFilePath + logFileName)

import os

def delete(logFilePath, logFileName, commitsFolderPath, commitNumber):
    fileNumber = int(commitNumber)
    commitFileName = str(commitNumber) + ".txt"
    filePath = commitsFolderPath + os.path.sep + commitFileName

    foundCommit = False
    versionsToDeleteFromLog = []
    if (os.path.exists(filePath)):
        os.remove(filePath)
        versionsToDeleteFromLog.append(int(fileNumber))
        foundCommit = True

    # delete all the commits after the commit specified by the user
    nextFileNumber = int(commitNumber)
    while (True):
        nextFileNumber = nextFileNumber+1
        commitFileName = str(nextFileNumber) + ".txt"
        filePath = commitsFolderPath + os.path.sep + commitFileName
        if (os.path.exists(filePath)):
            os.remove(filePath)
            versionsToDeleteFromLog.append(int(nextFileNumber))
        else:
            break

    if (not foundCommit):
        print("Invalid commit name")
    else:
        # remove from log
        removeFromLog(versionsToDeleteFromLog, logFilePath, logFileName)
    return foundCommit


def removeFromLog(commitVersionList, logFilePath, logFileName):
    logFile = open(logFilePath + os.path.sep + logFileName, "r")
    lines = logFile.readlines()
    logFile.close()


    tmpFile = open(logFilePath + os.path.sep + "tmp.txt", "w")
    tmpFile.truncate()
    for line in lines:
        tmpLine = line.split('|')
        if (int(tmpLine[0]) not in commitVersionList):
            tmpFile.write(line)

    tmpFile.close()
    os.remove(logFilePath + os.path.sep + logFileName)
    os.rename(logFilePath + os.path.sep + "tmp.txt", logFileName)


#delete(os.getcwd(), "log.txt",os.getcwd(), 1)

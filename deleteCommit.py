import os


def delete(logFilePath, logFileName, commitsFolderPath, commitNumber):
    print(logFilePath)
    fileNumber = int(commitNumber)
    commitFileName = str(commitNumber) + ".txt"
    filePath = commitsFolderPath + commitFileName

    foundCommit = False
    versionsToDeleteFromLog = []
    if (os.path.exists(filePath)):
        os.remove(filePath)
        versionsToDeleteFromLog.append(int(fileNumber))
        foundCommit = True

    # delete all the commits after the commit specified by the user
    nextFileNumber = int(commitNumber)
    while (True):
        nextFileNumber = nextFileNumber + 1
        commitFileName = str(nextFileNumber) + ".txt"
        filePath = commitsFolderPath + commitFileName
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
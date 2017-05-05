import os, datetime, time, linecache
from shutil import *
from reconstruct import *
from addfile import *


def initialCommitFile(commitFolder, userDir, file):
    filePath = userDir + os.path.sep + file
    if not os.path.exists(filePath):
        print(file + " does not exist")
        return False
    else:
        filePathInCommit = commitFolder + os.path.sep + file
        f = open(filePathInCommit, 'a')
        lines = [line.rstrip('\n') for line in open(filePath)]
        i = 0
        for line in lines:
            lineInCommitFile = "+|" + str(i) + "|" + line + '\n'
            i += 1
            f.write(lineInCommitFile)
        f.close()


def commit(username, commitMessage):
    cwd = os.getcwd()
    userDir = os.path.dirname(cwd) + os.path.sep + username
    repoDir = cwd + os.path.sep + "repo"
    commitDir = repoDir + os.path.sep + "commit"

    commitsInCommitDir = os.listdir(commitDir)
    commitsInCommitDir = [x for x in commitsInCommitDir if not x.startswith(".")]
    currCommitNum = len(commitsInCommitDir)

    stageFilePath = repoDir + os.path.sep + "stage.txt"
    if os.path.exists(stageFilePath):
        filesToBeCommitted = [line.rstrip('\n') for line in open(stageFilePath)]
    else:
        print("Error: Add files to commit")
        return False

    if filesToBeCommitted == 0:
        print("Error: No files added to be committed")
        return False

    else:
        commitFolder = commitDir + os.path.sep + str(currCommitNum)
        os.makedirs(commitFolder)
        if currCommitNum == 0:
            for file in filesToBeCommitted:
                initialCommitFile(commitFolder, userDir, file)
        else:
            prevCommitNumber = currCommitNum - 1
            for file in filesToBeCommitted:
                fileCreatedInCommitNumber = getFileCreationCommit(commitDir, file)
                if fileCreatedInCommitNumber == -1:
                    initialCommitFile(commitFolder, userDir, file)
                else:
                    tempFolder = repoDir + os.path.sep + "temp"
                    if os.path.exists(tempFolder):
                        rmtree(tempFolder)
                    reconstructCommit(int(fileCreatedInCommitNumber), int(fileCreatedInCommitNumber),
                                      int(prevCommitNumber), file)
                    filePathInTemp = tempFolder + os.path.sep + file
                    origialFilePath = userDir + os.path.sep + file
                    prevFile = open(filePathInTemp)
                    currFile = open(origialFilePath)

                    pLine = prevFile.readline()
                    cLine = currFile.readline()

                    commitLines = []

                    i = 0
                    while pLine != '' or cLine != '':
                        pLine = pLine.rstrip()
                        cLine = cLine.rstrip()

                        if pLine != '' and cLine != '':
                            if pLine != cLine:
                                commitLineDel = "-|" + str(i)
                                commitLineAdd = "+|" + str(i) + "|" + cLine.rstrip('\n')
                                commitLines.append(commitLineDel)
                                commitLines.append(commitLineAdd)
                        elif pLine == '' and cLine != '':
                            commitLineAdd = "+|" + str(i) + "|" + cLine.rstrip('\n')
                            commitLines.append(commitLineAdd)
                        elif pLine != '' and cLine == '':
                            commitLineDel = "-|" + str(i)
                            commitLines.append(commitLineDel)

                        pLine = prevFile.readline()
                        cLine = currFile.readline()

                        i += 1

                    prevFile.close()
                    currFile.close()
                    rmtree(tempFolder)

                    commitFile = commitFolder + os.path.sep + file
                    f = open(commitFile, 'a')
                    for l in commitLines:
                        f.write(l + '\n')
                    f.close()

    logFilePath = repoDir + os.path.sep + "log.txt"
    d = time.strftime("%d/%m/%Y")
    t = time.strftime("%H:%M:%S")
    timeStamp = str(d) + " " + str(t)
    writeLog(logFilePath, currCommitNum, username, timeStamp, commitMessage)
    removeStage(repoDir + os.path.sep)


def getFileCreationCommit(commitDir, file):
    listOfCommits = os.listdir(commitDir)
    listOfCommits = [x for x in listOfCommits if not x.startswith('.')]
    for commitNum in listOfCommits:
        commitFolder = commitDir + os.path.sep + commitNum
        listOfFilesInFolder = os.listdir(commitFolder)
        listOfFilesInFolder = [x for x in listOfFilesInFolder if not x.startswith('.')]
        if file in listOfFilesInFolder:
            return commitNum
    return -1


def writeLog(logiFilepath, commitNum, username, timeStamp, message):
    logFile = open(logiFilepath, 'a')
    logFile.write(str(commitNum) + "|" + str(username) + "|" + str(timeStamp) + "|" + str(message) + '\n')

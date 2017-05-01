import os, datetime, time, linecache
from shutil import *
from reconstruct import *


def initialCommit(commitDir, parentDir, files):
    for file in files:
        filePath = parentDir + os.path.sep + file
        if not os.path.exists(filePath):
            print(file + " does not exist")
            return False
        else:
            commitFolder = commitDir + os.path.sep + "0"
            os.makedirs(commitFolder)
            filePathInCommit = commitFolder + os.path.sep + file
            f = open(filePathInCommit, 'a')
            lines = [line.rstrip('\n') for line in open(filePath)]
            i = 0
            for line in lines:
                lineInCommitFile = "+|" + str(i) + "|" + line
                f.write(lineInCommitFile)
            f.close()


def commit(username, commitMessage):
    cwd = os.getcwd()
    parentDir = os.path.dirname(cwd)
    repoDir = cwd + os.path.sep + "repo"
    commitDir = repoDir + os.path.sep + "commit"

    commitsInCommitDir = os.listdir(commitDir)
    commitsInCommitDir = [x for x in commitsInCommitDir if not x.startswith(".")]
    currCommitNum = len(commitsInCommitDir)

    stageFilePath = repoDir + os.path.sep + "stage.txt"
    filesToBeCommitted = [line.rstrip('\n') for line in open(stageFilePath)]

    if filesToBeCommitted == 0:
        print("No files added to be committed")
        return False

    else:
        if currCommitNum == 0:
            initialCommit(commitDir, parentDir, filesToBeCommitted)

    logFilePath = repoDir + os.path.sep + "log.txt"
    d = time.strftime("%d/%m/%Y")
    t = time.strftime("%H:%M:%S")
    timeStamp = str(d) + " " + str(t)
    writeLog(logFilePath, currCommitNum, username, timeStamp, commitMessage)


def writeLog(logiFilepath, commitNum, username, timeStamp, message):
    logFile = open(logiFilepath + 'a')
    logFile.write(str(commitNum) + "|" + str(username) + "|" + str(timeStamp) + "|" + str(message))

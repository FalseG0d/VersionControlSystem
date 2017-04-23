import os, datetime, time, linecache


def commit(path, username, message):
    lastCommitNum = getLastCommitNumber(path)
    currCommitNum = lastCommitNum + 1

    writeLog(path, currCommitNum, username, message)

    lastCommitFile = open(path + str(lastCommitNum) + ".txt", 'r')
    currCommitFile = open(path + str(currCommitNum) + ".txt", "w")
    stagedFiles = getStagedFiles(path)

    homedirPath = str(path).replace(os.path.sep + "repo" + os.path.sep + "cmt" + os.path.sep, os.path.sep)


def getLastCommitNumber(path):
    return len(os.listdir(path))

def getLastCommitInfo(lastCommitFile, filename):
    lines = lastCommitFile.readLines()
    lastCommitInfo = []
    for line in lines:
        if line == filename:
            while (line != "---"):
                lastCommitInfo.append(line)

    return lastCommitInfo


def getStagedFiles(path):
    path = str(path).replace(os.path.sep + "cmt" + os.path.sep, os.path.sep)
    stagefile = open(path + "stage.txt")
    stagedFiles = stagefile.readlines()
    return stagedFiles


def writeLog(path, commitNum, username, message):
    path = str(path).replace(os.path.sep + "cmt" + os.path.sep, os.path.sep)
    logFile = open(path + "log.txt", "a")
    ts = time.time()
    timestamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    logFile.write(str(commitNum) + "|" + str(username) + "|" + str(timestamp) + "|" + message + "\n")
    logFile.close()

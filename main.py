import os
from user import *
from addfile import *
from log import *
from deleteCommit import *
from checkout import *

# initialize the repo when main.py is executed
cwd = os.getcwd()
repoDirectory = cwd + os.path.sep + "repo" + os.path.sep
if not os.path.exists(repoDirectory):
    os.makedirs(repoDirectory)
logFilePath = repoDirectory + "log.txt"
open(logFilePath, 'a')
cmtDirectory = repoDirectory + os.path.sep + "commit" + os.path.sep
if not os.path.exists(cmtDirectory):
    os.makedirs(cmtDirectory)

currentSessionUser = None

# commands
while True:
    command = str(input("> "))
    commandTokens = command.split(" ")
    if commandTokens[0] == "create":
        userName = commandTokens[1]
        createUser(userName, repoDirectory + os.path.sep + "user.txt")

    elif commandTokens[0] == "login":
        userName = commandTokens[1]
        if login(userName, repoDirectory + os.path.sep + "user.txt"):
            currentSessionUser = userName

    elif commandTokens[0] == "add":
        fileName = commandTokens[1]
        addFile(repoDirectory, fileName, os.path.dirname(cwd) + os.path.sep)

    elif commandTokens[0] == "exit":
        break

    elif commandTokens[0] == "log":
        log(logFilePath)

    elif commandTokens[0] == "delete":
        delete(repoDirectory, "log.txt", cmtDirectory, commandTokens[1])

    elif commandTokens[0] == "checkout":
        checkout(int(commandTokens[1]))

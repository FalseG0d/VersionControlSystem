import os
from user import *
from addfile import *
from log import *
from deleteCommit import *
from checkout import *
from commit import *
import getpass

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
        password = getpass.getpass("Password: ")
        createUser(userName, password, repoDirectory + os.path.sep + "user.txt")

    elif commandTokens[0] == "login":
        userName = commandTokens[1]
        password = getpass.getpass("Password: ")
        if login(userName, password, repoDirectory + os.path.sep + "user.txt"):
            currentSessionUser = userName
        else:
            print("Login failed!")

    elif commandTokens[0] == "add":
        if currentSessionUser is not None:
            fileName = commandTokens[1]
            addFile(repoDirectory, fileName, os.path.dirname(cwd) + os.path.sep)
        else:
            print("Please login!")

    elif commandTokens[0] == "exit":
        break

    elif commandTokens[0] == "log":
        if currentSessionUser is not None:
            log(logFilePath)
        else:
            print("Please login!")

    elif commandTokens[0] == "delete":
        if currentSessionUser is not None:
            delete(repoDirectory, "log.txt", cmtDirectory, commandTokens[1])
        else:
            print("Please login!")

    elif commandTokens[0] == "checkout":
        if currentSessionUser is not None:
            checkout(int(commandTokens[1]))
        else:
            print("Please login!")

    elif commandTokens[0] == "commit":
        if commandTokens[1] == "-m":
            if currentSessionUser is not None:
                commit(currentSessionUser, commandTokens[2])
            else:
                print("Please login!")
        else:
            print("Commit message missing")

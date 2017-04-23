import os
from user import *
from addfile import *

# initialize the repo when main.py is executed
cwd = os.getcwd()
repoDirectory = cwd + os.path.sep + "repo" + os.path.sep
if not os.path.exists(repoDirectory):
    os.makedirs(repoDirectory)

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
        addFile(repoDirectory, fileName, cwd + os.path.sep)

    elif commandTokens[0] == "exit":
        break

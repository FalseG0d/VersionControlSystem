import hashlib
import os


def login(userName, password, filePath):
    try:
        foundUser = False
        p = hashlib.sha256(password.encode()).hexdigest()
        lines = [line.rstrip('\n') for line in open(filePath)]
        line = userName + ',' + p
        if line in lines:
            foundUser = True

        return foundUser
    except IOError:
        return False


def createUser(userName, password, filePath):
    try:
        users = open(filePath, "a")
        p = hashlib.sha256(password.encode()).hexdigest()
        users.write(userName + "," + p)
        users.write("\n")
        cwd = os.getcwd()
        parentDir = os.path.dirname(cwd)
        userDir = parentDir + os.path.sep + userName
        if not os.path.exists(userDir):
            os.makedirs(userDir)
        return True
    except IOError:
        return False

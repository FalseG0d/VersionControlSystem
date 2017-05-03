import hashlib


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
        return True
    except IOError:
        return False

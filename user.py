def login(userName, password, filePath):
    try:
        foundUser = False
        lines = [line.rstrip('\n') for line in open(filePath)]
        line = userName + ',' + password
        if line in lines:
            foundUser = True

        return foundUser
    except IOError:
        return False


def createUser(userName, password, filePath):
    try:
        users = open(filePath, "a")
        users.write(userName + "," + password)
        users.write("\n")
        return True
    except IOError:
        return False

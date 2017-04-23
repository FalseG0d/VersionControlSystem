def login(userName, filePath):
    try:
        users = open(filePath, "r")
        foundUser = False
        for line in users:
            if (line.strip('\t\n') == userName):
                foundUser = True
                print("Login successful!")
                break

        return foundUser
    except IOError:
        return False


def createUser(userName, filePath):
    try:
        users = open(filePath, "a")
        users.write(userName)
        users.write("\n")
        return True
    except IOError:
        return False

# login("Paras")
# createUser("abc")

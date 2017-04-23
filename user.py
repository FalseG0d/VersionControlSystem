def login(userName):
    try:
        users = open("user.txt", "r")
        foundUser = False
        for line in users:
            if (line.strip('\t\n') == userName):
                foundUser = True
                break

        print(foundUser)
        return foundUser
    except IOError:
        return False
    
def createUser(userName):
    try:
        users = open("user.txt","a")
        users.write(userName)
        users.write("\n")
        return True
    except IOError:
        return False

#login("Paras")
#createUser("abc")

def login(userName):
        users = open("user.txt", "r")
        foundUser = False
        for line in users:
            if (line.strip('\t\n') == userName):
                foundUser = True
                break

        print(foundUser)
        return foundUser


login("Paras")

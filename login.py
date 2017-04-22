import sys


def login():
    if (len(sys.argv) < 2):
        print("Syntax of the program: python login.py your_user_name")
    else:
        users = open("user.txt", "r")
        foundUser = False
        for line in users:
            if (line.strip('\t\n') == sys.argv[1]):
                foundUser = True
                break

        print(foundUser)


login()

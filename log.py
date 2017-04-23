def log(filePath):
    lines = [line.rstrip('\n') for line in open(filePath)]
    for line in lines:
        print(line)

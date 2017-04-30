import os


def reconstructCommit(currentCommmitNumber, endCommitNumber, fileName):
    cwd = os.getcwd()
    tempDir = cwd + os.path.sep + "temp"
    if not os.path.exists(tempDir):
        os.makedirs(tempDir)

    commitFolderDir = cwd + os.path.sep + "commit"

    commmitFolder = commitFolderDir + os.path.sep + str(currentCommmitNumber)
    fileInCommitFolder = commmitFolder + os.path.sep + fileName
    fileInTempFolder = tempDir + os.path.sep + fileName

    lines = [line.rstrip('\n') for line in open(fileInCommitFolder)]

    linesInReconstructedFile = None

    if os.path.exists(fileInTempFolder):
        linesInReconstructedFile = [line.rstrip('\n') for line in open(fileInTempFolder)]
        os.remove(fileInTempFolder)

    f = open(fileInTempFolder, 'a')

    if currentCommmitNumber == 0:
        for line in lines:
            lineSplit = line.split("|", 2)
            f.write(lineSplit[2] + '\n')
    else:
        for line in lines:
            lineSplit = line.split("|", 2)
            lineNum = int(lineSplit[1])
            if lineSplit[0] == '-':
                linesInReconstructedFile[lineNum] = None
            else:
                if len(linesInReconstructedFile) > lineNum:
                    linesInReconstructedFile[lineNum] = lineSplit[2]
                else:
                    linesInReconstructedFile.append(lineSplit[2])

        for line in linesInReconstructedFile:
            if line is not None:
                f.write(line + '\n')

    f.close()

    if currentCommmitNumber < endCommitNumber:
        reconstructCommit(currentCommmitNumber + 1, endCommitNumber, fileName)


reconstructCommit(0, 1, "1.txt")

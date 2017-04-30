import os
from shutil import *


def reconstructCommit(currentCommitNumber, endCommitNumber, fileName):
    cwd = os.getcwd()
    tempDir = cwd + os.path.sep + "repo" + os.path.sep + "temp"
    if not os.path.exists(tempDir):
        os.makedirs(tempDir)

    commitFolderDir = cwd + os.path.sep + "repo" + os.path.sep + "commit"

    commitFolder = commitFolderDir + os.path.sep + str(currentCommitNumber)
    fileInCommitFolder = commitFolder + os.path.sep + fileName
    fileInTempFolder = tempDir + os.path.sep + fileName

    lines = [line.rstrip('\n') for line in open(fileInCommitFolder)]

    linesInReconstructedFile = None

    if os.path.exists(fileInTempFolder):
        linesInReconstructedFile = [line.rstrip('\n') for line in open(fileInTempFolder)]
        os.remove(fileInTempFolder)

    f = open(fileInTempFolder, 'a')

    if currentCommitNumber == 0:
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

    if currentCommitNumber < endCommitNumber:
        reconstructCommit(currentCommitNumber + 1, endCommitNumber, fileName)


def reconstructCheckout(endCommitNumber):
    cwd = os.getcwd()
    cacheDir = cwd + os.path.sep + "repo" + os.path.sep + "cache"
    if not os.path.exists(cacheDir):
        os.makedirs(cacheDir)

    commitFolderDir = cwd + os.path.sep + "repo" + os.path.sep + "commit"

    foldersInCacheFolder = os.listdir(cacheDir)
    foldersInCacheFolder = [x for x in foldersInCacheFolder if not x.startswith('.')]

    if len(foldersInCacheFolder) != 0:

        cachedCommitNumber = int(foldersInCacheFolder[0])

        if cachedCommitNumber == endCommitNumber:
            return 1

        elif cachedCommitNumber > endCommitNumber:
            rmtree(cacheDir + os.path.sep + str(cachedCommitNumber))
            reconstructCheckout(endCommitNumber)

        elif cachedCommitNumber < endCommitNumber:
            nextCommitNumber = cachedCommitNumber + 1

            commitFolder = commitFolderDir + os.path.sep + str(nextCommitNumber)

            listOfFilesInCommitFolder = os.listdir(commitFolder)
            listOfFilesInCommitFolder = [x for x in listOfFilesInCommitFolder if not x.startswith('.')]

            for file in listOfFilesInCommitFolder:
                filePathInCommitFolder = commitFolder + os.path.sep + file
                filePathInCache = cacheDir + os.path.sep + str(cachedCommitNumber) + os.path.sep + file
                linesInCommitFile = [line.rstrip('\n') for line in open(filePathInCommitFolder)]

                if os.path.exists(filePathInCache):
                    linesInCacheFile = [line.rstrip('\n') for line in open(filePathInCache)]
                    os.remove(filePathInCache)

                    for line in linesInCommitFile:
                        lineSplit = line.split("|", 2)
                        lineNum = int(lineSplit[1])
                        if lineSplit[0] == '-':
                            linesInCacheFile[lineNum] = None
                        else:
                            if len(linesInCacheFile) > lineNum:
                                linesInCacheFile[lineNum] = lineSplit[2]
                            else:
                                linesInCacheFile.append(lineSplit[2])

                    f = open(filePathInCache, 'a')
                    for line in linesInCacheFile:
                        if line is not None:
                            f.write(line + '\n')
                    f.close()

                else:
                    f = open(filePathInCache, 'a')
                    for line in linesInCommitFile:
                        lineSplit = line.split("|", 2)
                        f.write(lineSplit[2] + '\n')
                    f.close()
            oldFolderPath = cacheDir + os.path.sep + str(cachedCommitNumber)
            newFolderPath = cacheDir + os.path.sep + str(cachedCommitNumber + 1)
            os.rename(oldFolderPath, newFolderPath)
            reconstructCheckout(endCommitNumber)

    else:
        commitFolder = commitFolderDir + os.path.sep + "0"
        listOfFiles = os.listdir(commitFolder)
        listOfFiles = [x for x in listOfFiles if not x.startswith('.')]

        for fileName in listOfFiles:
            reconstructCommit(0, 0, fileName)

        cacheCommitFolder = cacheDir + os.path.sep + "0"
        os.makedirs(cacheCommitFolder)

        tempDir = cwd + os.path.sep + "repo" + os.path.sep + "temp"

        listOfFilesInTemp = os.listdir(tempDir)
        listOfFilesInTemp = [x for x in listOfFilesInTemp if not x.startswith('.')]

        for file in listOfFilesInTemp:
            filePathInTemp = tempDir + os.path.sep + file
            filePathInCache = cacheCommitFolder + os.path.sep + file
            f = open(filePathInCache, 'a')
            copyfile(filePathInTemp, filePathInCache)
            f.close()

        if endCommitNumber != 0:
            reconstructCheckout(endCommitNumber)

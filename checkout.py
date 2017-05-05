from reconstruct import *
import os
from shutil import *


def checkout(commitNumber, username):
    reconstructCheckout(commitNumber)
    cwd = os.getcwd()
    cacheDir = cwd + os.path.sep + "repo" + os.path.sep + "cache"
    foldersInCacheFolder = os.listdir(cacheDir)
    foldersInCacheFolder = [x for x in foldersInCacheFolder if not x.startswith('.')]
    listOfFilesInCacheFolder = os.listdir(cacheDir + os.path.sep + foldersInCacheFolder[0])
    listOfFilesInCacheFolder = [x for x in listOfFilesInCacheFolder if not x.startswith('.')]

    userDir = os.path.dirname(cwd) + os.path.sep + username

    itemsInParentDir = os.listdir(userDir)
    itemsInParentDir = [x for x in itemsInParentDir if not x.startswith('.')]

    for item in itemsInParentDir:
        path = userDir + os.path.sep + item
        if not os.path.isdir(path):
            os.remove(path)

    for file in listOfFilesInCacheFolder:
        filePathInCache = cacheDir + os.path.sep + foldersInCacheFolder[0] + os.path.sep + file
        filePathInUserDir = userDir + os.path.sep + file
        if username != "server":
            print(filePathInUserDir)
        if os.path.exists(filePathInUserDir):
            os.remove(filePathInUserDir)
        f = open(filePathInUserDir, 'a')
        copyfile(filePathInCache, filePathInUserDir)
        f.close()

    tempDir = cwd + os.path.sep + "repo" + os.path.sep + "temp"
    if os.path.exists(tempDir):
        rmtree(tempDir)

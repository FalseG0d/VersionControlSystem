from reconstruct import *
import os
from shutil import *


def checkout(commitNumber):
    reconstructCheckout(commitNumber)
    cwd = os.getcwd()
    cacheDir = cwd + os.path.sep + "repo" + os.path.sep + "cache"
    foldersInCacheFolder = os.listdir(cacheDir)
    foldersInCacheFolder = [x for x in foldersInCacheFolder if not x.startswith('.')]
    listOfFilesInCacheFolder = os.listdir(cacheDir + os.path.sep + foldersInCacheFolder[0])
    listOfFilesInCacheFolder = [x for x in listOfFilesInCacheFolder if not x.startswith('.')]

    parentDir = os.path.dirname(cwd)

    for file in listOfFilesInCacheFolder:
        filePathInCache = cacheDir + os.path.sep + foldersInCacheFolder[0] + os.path.sep + file
        filePathInParentDir = parentDir + os.path.sep + file
        if os.path.exists(filePathInParentDir):
            os.remove(filePathInParentDir)
        f = open(filePathInParentDir, 'a')
        copyfile(filePathInCache, filePathInParentDir)

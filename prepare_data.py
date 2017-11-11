import os
import errno
from os import walk
from PIL import Image
import numpy as np

TRAIN_COUNT = 10000
TEST_COUNT = 5000
VAL_COUNT = 1000

def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
    return

dataRoot = "data/"

def handleNpyFile(npyFile):
    print "extracting " + npyFile + "..."
    targetDir = npyFile.split('.')[0]
    trainDir = targetDir + "/train"
    mkdir_p(trainDir)
    testDir = targetDir + "/test"
    mkdir_p(testDir)
    valDir = targetDir + "/val"
    mkdir_p(valDir)

    loadedFile = np.load(npyFile);
    print "has images: " + str(len(loadedFile))
    counter = 0
    for index, imageData in enumerate(loadedFile):
        fn = str(index) + ".jpg"
        if index < TRAIN_COUNT:
            Image.fromarray(imageData.reshape(28, 28)).save(trainDir + "/" + fn)
        elif index < TRAIN_COUNT + TEST_COUNT:
            Image.fromarray(imageData.reshape(28, 28)).save(testDir + "/" + fn)
        elif index < TRAIN_COUNT + TEST_COUNT + VAL_COUNT:
            Image.fromarray(imageData.reshape(28, 28)).save(valDir + "/" + fn)
        else:
            break
        counter += 1

    print "done, total " + str(counter)
    return

for (dirpath, dirnames, filenames) in walk(dataRoot):
    for file in filenames:
        if not file.endswith(".npy"):
            continue
        handleNpyFile(dataRoot + file)

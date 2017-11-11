import os
import errno
from os import walk
import shutil
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

TRAIN_IMAGE_ROOT = dataRoot + "quickdraw_train/"
VAL_IMAGE_ROOT = dataRoot + "quickdraw_val/"
TEST_IMAGE_ROOT = dataRoot + "quickdraw_test/"

shutil.rmtree(TRAIN_IMAGE_ROOT)
mkdir_p(TRAIN_IMAGE_ROOT)

shutil.rmtree(TEST_IMAGE_ROOT)
mkdir_p(TEST_IMAGE_ROOT)

shutil.rmtree(VAL_IMAGE_ROOT)
mkdir_p(VAL_IMAGE_ROOT)

trainTxt = dataRoot + "/quickdraw_train.txt"
testTxt = dataRoot + "/quickdraw_test.txt"
valTxt = dataRoot + "/quickdraw_val.txt"

os.remove(trainTxt)
os.remove(testTxt)
os.remove(valTxt)
# open file with append mode
trainTxtFile = open(trainTxt, "a")
testTxtFile = open(testTxt, "a")
valTxtFile = open(valTxt, "a")

print TRAIN_IMAGE_ROOT
print TEST_IMAGE_ROOT
print VAL_IMAGE_ROOT

def handleNpyFile(npyFile, type):
    print "extracting " + npyFile + "..."

    fname = npyFile.split('/')[-1].split('.')[0]
    print fname

    loadedFile = np.load(npyFile);
    print "has images: " + str(len(loadedFile))
    counter = 0
    for index, imageData in enumerate(loadedFile):
        imageName = fname + "_" +  str(index) + ".jpg"
        if index < TRAIN_COUNT:
            Image.fromarray(imageData.reshape(28, 28)).save(TRAIN_IMAGE_ROOT + "/" + imageName)
            trainTxtFile.write(imageName + " " + str(type) + "\n")
        elif index < TRAIN_COUNT + TEST_COUNT:
            Image.fromarray(imageData.reshape(28, 28)).save(TEST_IMAGE_ROOT + "/" + imageName)
            testTxtFile.write(imageName + " " + str(type) + "\n")
        elif index < TRAIN_COUNT + TEST_COUNT + VAL_COUNT:
            Image.fromarray(imageData.reshape(28, 28)).save(VAL_IMAGE_ROOT + "/" + imageName)
            valTxtFile.write(imageName + " " + str(type) + "\n")
        else:
            break
        counter += 1
        # if counter >= 10:
        #     break
    print "done, total " + str(counter)

    return

for (dirpath, dirnames, filenames) in walk(dataRoot + "source_npy"):
    for index, file in enumerate(filenames):
        if not file.endswith(".npy"):
            continue
        handleNpyFile(dataRoot + "source_npy/" + file, index)

trainTxtFile.close()
testTxtFile.close()
valTxtFile.close()

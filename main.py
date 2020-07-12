import os
import glob
from PIL import Image
import time

dirName = "E:\TESTING FOLDER"

def main():
    totalMatches = 0

    os.chdir(dirName)
    listOfJpegImages = glob.glob("*.jpg")
    listOfPngImages = glob.glob("*.png")

    start = time.time()
    totalMatches += buildList(listOfJpegImages, totalMatches)
    totalMatches = buildList(listOfPngImages, totalMatches)
    end = time.time()
    print("The total number of matches were: " + str(totalMatches))
    print("The total time to find the matches was: " + str(end - start) + " seconds")

def buildList(listOfImages, totalMatches):
    imageList = []
    for currentImage in listOfImages:
        #For each image you get the name and size to populate a dictionary with
        name = currentImage
        size = os.path.getsize(currentImage)
        imageList.append([name,size])

    currentIndex = 0
    for imagePair in imageList:
        for otherImagePair in imageList[currentIndex:]:
            if(imagePair[1] == otherImagePair[1] and imagePair[0] != otherImagePair[0]):
                #Need to do additional testing of the images to make sure they are actually the same and not just the same size
                if(compareImage(imagePair[0], otherImagePair[0])):
                    print(imagePair[0] + " is the same image as " + otherImagePair[0])
                    totalMatches += 1

        currentIndex += 1
    return totalMatches


def compareImage(filenameImage1, filenameImage2):
    image1 = Image.open(dirName + "\\" + filenameImage1)
    image1Px = image1.load()
    image1Height = image1.height
    image1Width = image1.width

    image2 = Image.open(dirName + "\\" + filenameImage2)
    image2Px = image2.load()
    image2Height = image2.height
    image2Width = image2.width

    heightIterator = 0
    widthIterator = 0

    if(image1Height != image2Height or image1Width != image2Width):
        return False

    while(heightIterator < image1Height and widthIterator < image1Width):
        if(image1Px[widthIterator, heightIterator] != image2Px[widthIterator, heightIterator]):
            return False
        heightIterator += 1
        if(heightIterator >= image1Height):
            widthIterator += 1
            heightIterator = 0
    return True


main()

import os
import glob
import random
import shutil
import time

def main():
	print("Enter the selected folder, make sure to capitalize properly")
	print("Options are: ")

	directoryList = next(os.walk("."))[1]
	print(directoryList)

	userInput = input("Enter your value: ")

	os.chdir(userInput)
	listOfImages = glob.glob("*.jpg") + glob.glob("*.png") + glob.glob("*.gif")

	lengthOfList = len(listOfImages)
	if(lengthOfList > 50):
		randomList = random.sample(listOfImages, 50)
	else:
		lengthOfList = int(lengthOfList)
		randomList = random.sample(listOfImages, lengthOfList)
	print(randomList)

	if not os.path.isdir("temp"):
		os.mkdir("temp")
	else:
		for file in os.listdir("temp"):
			os.unlink(os.path.join("temp",file))

	#Move the files to the folder 
	for image in randomList:
		shutil.copy(image, "temp")

	#Rename the files to a random number
	listOfNewNames = random.sample(range(lengthOfList), lengthOfList)
	i = 0
	for imageRename in os.listdir("temp"):
		os.rename(os.path.join("temp", imageRename), os.path.join("temp", str(listOfNewNames[i]) + "_" + imageRename))
		i += 1

	print("Enter any input and the folder will be deleted")
	input("Press enter to delete the temp directory")
	for imageToRemove in os.listdir("temp"):
		os.unlink(os.path.join("temp",imageToRemove))

	os.rmdir("temp")

main()
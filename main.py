import os
import re


def main():
    # Walking all the directories and finding all the
    # .py extended files
    subDirs = [x[0] for x in os.walk('Demo')]

    finalLibrary = []
    pythonFileNames = []
    pythonFileDirs = []

    # Listing all the directories, searching for python files,
    # reading the python files, and getting the import/from library
    # names and saving into the requirements.txt file.

    for i in subDirs:
        for j in os.listdir(i):
            if j.lower().endswith(".py"):
                pythonFileNames.append(j.split(".")[0])
                pythonFileDirs.append(i + "\\" + j)

    currentLibraryList = []
    for library in pythonFileDirs:

        f = open(library, "r")

        currentLibrary = f.readlines()


        for z in currentLibrary:
            z = z.strip()
            z = z.strip("\\n")



            if "import" in z or "from" in z:
                theStrWord= z.strip()
                currentLibraryList.append(theStrWord)

        f.close()


    for i in range(len(currentLibraryList)):
        if currentLibraryList[i].split()[0] == "import" or currentLibraryList[i].split()[0] == "from":
            if currentLibraryList[i].split()[1] not in finalLibrary and currentLibraryList[i].split()[1] not in pythonFileNames:
                finalLibrary.append(currentLibraryList[i].split()[1])


    print(finalLibrary)
    return finalLibrary

# Creating a new requirements.txt file and writing down all the libraries
def writingRequirement(finalLibrary):
    for i in finalLibrary:
        f = open("requirements.txt", "a")
        f.write(i + "\n")
        f.close()


if __name__ == '__main__':
    finalLibrary = main()
    writingRequirement(finalLibrary)
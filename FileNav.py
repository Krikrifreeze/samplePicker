#file navigation
import os

def getFile(directory, n): #returns file in a directory based on n
    #directory must be a raw string.
    os.chdir(directory)
    #print("    directory: " + os.getcwd())
    dirList = os.listdir(directory) #stores all of the files in the directory into a list
    i = 0
    for file in dirList:
        if i == n:
            return file
        else:
            i+=1

def test():
    directory = r"C:\\Users\\lil kri\\Documents\\FL Studio\\Samples\\TS-RareBreaksVol1"
    index = 0
    print("fileIndex:" + str(index))
    print("filename: " + getFile(directory, index))
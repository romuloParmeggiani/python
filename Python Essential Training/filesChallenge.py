import os

def main():
    totalBytes = 0
    #Listing all the content of current working directory into variable
    dirEntries = os.listdir()
    #Creating a results folder
    if (os.path.exists("results") != True):
        os.mkdir("results")

    resultFile = open("results/resultFile.txt", "w+")
    if resultFile.mode == "w+":
        resultFile.write("Files list:\n")
        resultFile.write("------------------\n")
        for entry in dirEntries:
            if os.path.isfile(entry):
                totalBytes += os.path.getsize(entry)
                resultFile.write(entry + "\n")
        resultFile.write("------------------\n")
        resultFile.write("Total file bytecount:" + str(totalBytes))
    resultFile.close()
        

if __name__ == "__main__":
    main()
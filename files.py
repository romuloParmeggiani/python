import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
    #Creating a file with built in open(<fileName.Extention>, <Mode>)
    myFile = open("testTextFile.txt", "w+")
    #Writing some content into the file
    for i in range(10):
        myFile.write("This is some code written text\n")
    #Closing the file when we're done writing into it
    myFile.close()
    #Opening the file again to Add some additional content to it with "a+" mode
    myFile = open("testTextFile.txt", "a+")
    for i in range(5):
        myFile.write("This is some additional code written text\n")
    myFile.close()
    #Reading the content of the File, using the read() or readlines() (!) not required to close it afterwards (!)
    myFile = open("testTextFile.txt", "r")
    if myFile.mode == "r":
        contents = myFile.read()
        print(contents)

    #Printing os name
    print("OS name is:",os.name)
    #Checking if certain file exists
    print("Item exists:",str(path.exists("testTextFile.txt")))
    print("Item is a file:",str(path.isfile("testTextFile.txt")))
    print("Item is a directory:",str(path.isdir("testTextFile.txt")))
if __name__ == "__main__":
    main()
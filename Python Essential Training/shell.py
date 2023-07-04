import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
    if path.exists("testTextFile.txt"):
        #Getting the path to the desired file within the current directory
        source = path.realpath("testTextFile.txt")
        #Creating a backup copy of the file by appending the ".bak" sufix to it's name
        destination = source + ".bak"
        shutil.copy(source, destination)
        #Renaming the original file
        #os.rename("testTextFile.txt", "renamedFile.txt")
        #os.rename("testTextFile.txt.bak", "testTextFile.txt")
        #Putting all files into a zip archive
        #root_dir, tail = path.split(source)
        #make_archive("archive", "zip", root_dir)
        with ZipFile("testzip.zip", "w") as newZip:
            newZip.write("testTextFile.txt")

if __name__ == "__main__":
    main()
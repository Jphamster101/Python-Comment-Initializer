"""
Name: Johnny Pham
Filename: createPythonFile.py
Date: March 30, 2020
Description: File to assist in creating python files with comments
"""

from datetime import date
import subprocess

today = date.today()

def main():
    d2 = getDate()
    name, fileName, description = getInput()
    programFile, nameOfFile = createPythonFile(fileName, name, description, createSavePath())
    writeInitComment(name, programFile, nameOfFile, d2, description)

def getDate():
    # Textual month, day and year	
    return today.strftime("%B %d, %Y")

def getInput():
    name = input("Enter your name: ")
    fileName = input("Enter a name for the file: ")
    description = input("Enter a description for this file: ")
    return name, fileName, description

def createSavePath():
    # Opens up the File Explorer
    file_explorer = input("Open file explorer? (y or n): ")
    if file_explorer == "y":
        subprocess.Popen(r'explorer /select,"C:\Users\Johnny\Desktop\cs_portfolio\python_programming\OOP"')

    savePath = input("Enter the path where the file will be saved: ")
    if "Users" not in savePath:
        savePath  = r"C:\Users\X" + "\\" + savePath
    else:
        savePath = savePath + '\\'
    print("savePath in createSavePath function:",savePath)
    return savePath

def createPythonFile(fileName, name, description, savePath):
    print("This is savePath:", savePath)
    if ".py" not in fileName:
        nameOfFile = fileName + ".py"
    else:
        nameOfFile = fileName
    programFile = open(savePath + nameOfFile, "w")
    print("savePath + nameOfFile:", savePath + nameOfFile)
    return programFile, nameOfFile

def writeInitComment(name, file, nameOfFile, date, description):
    file.write('"""' + '\n')
    file.write("Name:" + name + '\n')
    file.write("Filename: " + nameOfFile + '\n')
    file.write("Date: " + str(date) + '\n')
    file.write("Description: " + description + '\n')
    file.write('"""' + '\n')
    file.close()

main()



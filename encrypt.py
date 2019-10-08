#!/usr/bin/python3
import os
import sys
import subprocess
from prettytable import PrettyTable

def getFiles():
    filelist = os.listdir(".")
    return filelist
def getDirs(filelist):
    dirList = []
    for files in filelist:
        if os.path.isdir(files):
            dirList.append(files)
    return dirList
def getEnc(fileList):
    encList = []
    for files in fileList:
        if "cpt" in files:
            encList.append(files)
    return encList
def getPossible(fileList,dirList,encList):
    possList = []
    for files in fileList:
        if files not in dirList and files not in encList:
            possList.append(files)
    return possList
def getFunc(operation):
    curr = getFiles()
    dir = getDirs(curr.copy())
    enc = getEnc(curr.copy())
    poss = getPossible(curr.copy(),dir.copy(),enc.copy())
    retval = []
    if operation == 0:
        retval = poss.copy()
    else:
        retval = enc.copy()
    return retval
def encryptFile(fileName):
    key = os.environ['KEYS']
    retval = subprocess.run(["ccrypt", "-e" ,fileName, "-K", key])
    if retval.returncode == 0:
        print ("Encrypted " + fileName)
def decryptFile(fileName):
    retval = subprocess.run(["ccrypt", "-d" ,fileName, "-E", "KEYS"])
    if retval.returncode == 0:
        print ("Decrypted " + fileName)
def getUser(fileList,operation):
    x = input("Enter Your Choice: ")
    retval = 0
    try:
        x = int(x)
    except:
        x = 0
        sys.stderr.write('Invalid Input, Exiting')
    if x == 0:
        retval = 1
    else:
        if x == len(fileList)+1:
            if operation ==0:
                for files in fileList:
                    encryptFile(files)
            else:
                for files in fileList:
                    decryptFile(files)
            retval = 1
        else:
            if operation == 0:
                encryptFile(fileList[x-1])
            else:
                decryptFile(fileList[x-1])
            retval = 0
    return retval
def showMenu():
    retval = 1
    try:
        print ("Enter 0 to Encrypt or 1 to Decrypt, Blank to exit")
        operation = int(input("Input: "))
    except:
        print ("Invalid Input")
        return retval
    if operation == 0:
        print ("Let's Encrypt !")
    elif operation == 1:
        print ("Let's Decrypt")
    else:
        print ("Invalid Input")
        return retval
    possList = getFunc(operation)
    if possList:
        x = PrettyTable()
        x.field_names = ["Option","File Name"]
        x.add_row([0,"Exit"])
        count = 1
        for files in possList:
            x.add_row([count,files])
            count = count +1
        x.add_row([count,"All"])
        print (x)
        y= getUser(possList.copy(),operation)
        if y == 1:
            print ("Exiting")
            return
        else:
            showMenu()
    else:
        if operation == 0:
            print ("No Encryption Possible")
        else:
            print ("No Decryption Possible")

def main():
    print ("Welcome To The File Encryption Tool")
    showMenu()
    print ("Thank you")
if __name__ == "__main__":
    main()

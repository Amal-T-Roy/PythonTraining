import os
from datetime import datetime 


#print(dir(os)) #shows all attributes&methods associated with the module

print(os.getcwd()) #Prints current working directory

#os.chdir('/Users/itsme/OneDrive/Desktop/') #Changes PWD to passed address-->WINDOWS
os.chdir('/home/amalr/Desktop/') #Changes PWD to passed address-->linux
print(os.getcwd()) #Prints current working directory

print(os.listdir()) #Prints contents of the current working directory

os.mkdir('TestFile') #creates a folder with name that is passed
"""
Note:If the file with same name exists,then new wont be created
"""

os.makedirs('TestFile/ChildFolder') #creates nested folders

os.rmdir('TestFile/ChildFolder') #Deleted the child directory

os.rename('TestFile','NameChange') #Replaces the name of the 1st arg with 2nd arg

print(os.stat('NameChange')) 
print(os.stat('opnproject')) #prints info of the file
print(os.stat('opnproject').st_size) #prints size in bytes

print(os.stat('opnproject').st_mtime) #prints last modified time
#x = os.stat('opnproject').st_mtime
print(datetime.fromtimestamp(os.stat('opnproject').st_mtime)) #Makes time humanreadable

"""Os.walk() returns 3 tuples-path,folders,files in them"""
for dirpath,dirnames,filenames in   os.walk('/home/amalr/Desktop/') :
    print('Current Path = ',dirpath)
    print('Folders = ',dirnames)
    print('Files = ',filenames)
    print()

#Get environment variables
print(os.environ) #Prints all environ variables
print(os.environ.get('HOME')) #Just that of home

print(os.path.isfile('opnproject')) #retun true if arg is a file
print(os.path.isdir('opnproject')) #retun true if arg is a directory

print(os.path.splitext('Test.txt'))
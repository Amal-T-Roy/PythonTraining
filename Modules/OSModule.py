import os

#print(dir(os)) #shows all attributes&methods associated with the module

print(os.getcwd()) #Prints current working directory

os.chdir('/Users/itsme/OneDrive/Desktop/') #Changes PWD to passed address-->WINDOWS
#os.chdir('/Users/itsme/OneDrive/Desktop/') #Changes PWD to passed address-->linux
print(os.getcwd()) #Prints current working directory

print(os.listdir()) #Prints contents of the current working directory

os.mkdir('TestFile') #creates a folder with name that is passed
"""Note:If the file with same name exists,then new wont be created"""
os.makedirs('TestFile/ChildFolder') #creates nested folders
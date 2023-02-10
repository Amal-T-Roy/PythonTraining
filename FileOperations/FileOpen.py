#opening a file using absolute path ,using read only permission
#f = open('C:/Users/itsme/OneDrive/Desktop/Python/FileOperations/HelloWorld.txt', 'r')

f = open('HelloWorld.txt', 'r')
print(f)

#method to read contents
#print(f.read())

#To print line by line,call below method->has internal pointer->increment line no. automatically
print(f.readline(3)) #prints only 3 characters of the line
print(f.tell())
print(f.readline(),end = "#") #removes the LF at the end
print(f.tell())


print(f.fileno()) #prints no of lines in file


Buff = []
Buff = f.read(5)
print('Buff = ')
print(Buff)

f.seek(2) #Move cursor to after second character 
print(f.read())

f.close() #close file after operations
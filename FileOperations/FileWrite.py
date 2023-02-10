# f = open('C:/Users/itsme/OneDrive/Desktop/Python/FileOperations/HelloWorld.txt', 'w')
f = open('HelloWorld.txt', 'a')
print(f)

f.write('HIHI') #Overwrites the contents of the file

f.write('Bruh')

f.close()
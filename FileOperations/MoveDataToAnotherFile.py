# "C:\Users\itsme\OneDrive\Desktop\Python\FileOperations\Target.txt"

#open source file
#f = open('C:/Users/itsme/OneDrive/Desktop/Python/FileOperations/HelloWorld.txt', 'r')
f = open('HelloWorld.txt', 'a')

# Buff = []
# Buff.append(f.read(15))
# print(Buff)

string = f.read(15)
print(type(string))

#Open target file
target = open('C:/Users/itsme/OneDrive/Desktop/Python/FileOperations/Target.txt', 'a')
# target.write(str(Buff)) Write a list to file
target.write(string) #write a string to file

f.close()
target.close()
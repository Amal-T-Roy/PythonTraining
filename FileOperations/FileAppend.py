#f = open('C:/Users/itsme/OneDrive/Desktop/Python/FileOperations/HelloWorld.txt', 'a')
f = open('HelloWorld.txt', 'a')

f.write('Woah that was awesome\nNeverMind')
print(f.tell())

string = input('Enter input string:\n')
f.seek(1)
f.write(string)
# print(f.read())

f.close() #closing file
f = open('C:/Users/itsme/OneDrive/Desktop/Python/FileOperations/HelloWorld.txt', 'r')
f = open('HelloWorld.txt', 'r')

Buff = []
Buff = f.read(15) #pass no.of characters to read
print('Buff = {} '.format(Buff))

f.close() #Closing file

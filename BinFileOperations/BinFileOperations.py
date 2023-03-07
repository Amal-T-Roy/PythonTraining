import pickle

def MainMenu():
    print('1.Write data')
    print('2.Read Data')
    print('3.Append Data')

def write():
    f = open('Test.dat',mode='wb')
    x = input('Enter string to write:\n')
    pickle.dump(x,f)
    pickle.dump([],f)
    f.close()
    

def read():
    f = open('Test.dat',mode='rb')
    x = pickle.load(f)
    print(x)
    print(f.tell())
    f.close()


def append():
    f = open('Test.dat',mode='ab')
    string = input('Enter data:\n')
    f.seek(0)
    pickle.dump(string,f)
    f.close()

Repeat = True
while Repeat == True:
    MainMenu()
    choise = int(input('Enter the operation to be performed:'))
    if choise == 1:
        write()
    elif choise == 2:
        read()
    elif choise == 3:
        append()
    else:
        print('Invalid Choise')

    option = input('Continue(Y/N)\n')
    if(option == 'Y'):
        Repeat = True
    else:
        Repeat = False

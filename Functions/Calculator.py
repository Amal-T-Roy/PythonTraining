def add() :
    return x + y

def sub() :
    return x - y

def mult() :
    return x*y

def div() :
    return x/y

def get_rem() :
    return x % y

x = int(input('Enter value1 :'))
y = int(input('Enter value2 :'))

print(
'''
----MENU---
1.Add
2.Subtract
3.Multiply
4.Divide
5.Remainder
'''
)

#List containing function names
Operations = [add,sub,mult,div,get_rem]

choice = int(input('Enter the operation : '))
if(choice < 1 or choice >= 6) :
    print('💀☠☠Invalid Operation☠☠💀')
else :
    #Attach the parantheses to the function name,thus making the fun call
    output = Operations[choice - 1]()
    print(output)

print(Operations[choice - 1]())
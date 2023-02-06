Stack = [1,2,3]

Stack.append(4)
print(Stack)
Stack.append(4)
print(Stack.pop())
print(Stack)
if Stack == [] :
    print('Stack is empty')
else :
    print('Not empty')

for i in range (0,5) :
    print(Stack.pop())
    if Stack == [] :
        print('Stack is empty')
        break

print(Stack)



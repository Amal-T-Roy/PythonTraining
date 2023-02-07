a = [] #initialise empty list

for i in range(0,10) :
    a.append(i) 

print(a)

#Code to print even numbers upto a given input
even = []
limit = int(input('Enter the number\n'))

if limit > 0 :
    for i in range (0,limit,2) :
        even.append(i)
else :
    print('Invalid input')

print(even)
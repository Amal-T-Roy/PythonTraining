a , b = 0 , 1

x = int(input('Enter number of values to print \n'))

for i in range(0,x) :
        a , b = b , a + b
        print(b , end = '\n')
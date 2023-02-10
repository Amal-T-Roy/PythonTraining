a,b = 0,1

for i in range(1,10) :
    a,b = b,a + b
    print(b ,end = '!\n')


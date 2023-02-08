def Add(x = 0,y = 0) :
    return x + y

print(Add(5,6))
print(Add(6))
print(Add())
print(Add(10,9))

#Using place holder and .format() method
print('Sum = {} , {}'.format(Add(5,8),Add(9,1)))

#using Map to iterate through a list
Inputs = [1,2,3,4]
print(list(map(Add,Inputs )))

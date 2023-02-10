TestArray = [1,2,3,4,5,6,7,8]

#normally we use i as the iterator
for i in TestArray :
    print(i,end = '') 

#initialise iterator
iterator = iter(TestArray)
print(iterator.__next__())
print(iterator.__next__())
print(next(iterator)) #same as above

#to print the rest of the test array
# for i in range(0,6) :
#     print(iterator.__next__())


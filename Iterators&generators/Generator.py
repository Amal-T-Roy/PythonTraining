"""
The commented part is a program that returns the squares of list elememts passed into the function.
It is modified using generator
"""


# def square_numbers(nums) :
#     result = []
#     for i in nums :
#         result.append(i*i)
#     return result

# TestArray = [1,2,3,4,5]

# OutPut = square_numbers(TestArray)
# print(OutPut)

def square_numbers(nums) :
    for i in nums :
        yield (i*i)

TestArray = [1,2,3,4,5]

OutPut = square_numbers(TestArray)
print(OutPut)

print(next(OutPut)) #Print nxt value
print(next(OutPut))
print(next(OutPut))
print(next(OutPut))
print(next(OutPut))

#If we go beyond the range,it will raise an exception called 'StopIteration'
print(next(OutPut))
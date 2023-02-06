combine = []

for x in [1,2,3] :
    for y in [4,5,6] :
        if x != y :
            combine.append((x,y))

print(combine)

vec = [1,2,3,4,5]
temp = [x**2 for x in vec]
print (temp)

squares = []

squares = [abs(x*2/3) for x in range(5)]
print(squares)
del(squares[1])
print(squares)

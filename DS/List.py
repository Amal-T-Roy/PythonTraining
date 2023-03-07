List = [1,2,3,4,5,6]

print( List)
List.insert(3,7)
print( List)
List.append(8)
print( List)
List.remove(3)
print( List)
x = List.index(5, 0, len(List)) # Value,start,stop
print(x)
List.append(4)
print(List.count(4))
List.sort()
print(List)
List.reverse()
print(List)
List.insert(3,9) # index,value
print(List)
print(List.pop(4)) # Pops val at 4th index
print(List)
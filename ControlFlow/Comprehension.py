squares = []

x = int(input('Enter the value'))

squares = [i**2 for i in range(1,x)]
print(squares)
del(squares[1])
print(squares)

print(hex(id(squares)))
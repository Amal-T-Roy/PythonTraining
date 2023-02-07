a = 10
b = 5

print (a+b)
print("Hello World")

c = 7
d = 9
f = c/d
g = round(f,2)
print(g)
print (c / d)
print (c // d)
print(c % d) #remainder
print (c ** 2) #power
print(3*('Hello' + ' ' + 'There'))

#String ops

string = 'America'
print(string[3:6])
x = print(len(string))
print(x)

for i in range(0,6) :
    print(string[::-1])

data = [10,9,8,7,6,5,4,3,2,1]
DATA = [1,2,3,4,5,6,7,8,9,10]
JOIN = [data,DATA]

for i in range(0,10) :
    data[i] = data[i]/2
    print(data)

data.append(100)
print(data)

print(JOIN)

print(pow(5,2))

value = input('Enter value\n')
print('The value enterd = ',value)
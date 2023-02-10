student = {'name' : 'John' , 'age' : 25 , 'class' : 12}
print(student)
print(student['name'])

#use .get() so that we dont get an error if we access nonexistent key
print(student.get('name'))
print(student.get('number'))#we get none as output instead of keyerrror
print(student.get('number','ERROR 404'))#pass default message if not found

student.update({'name' : 'Mathew' , 'age' : 18})
print(student)
print(len(student))

del(student['name'])
print(student)

print(student.keys()) #method to print keys only
print(student.values()) #print values only
print(student.items()) #print key-value pairs

student.update({'name' : 'Mathew' , 'age' : 18})

for key in student :#loop through dict and print only keys
    print(key)

for key,value in student.items() :#loop through dict and print key,value pairs
    print(key,value)
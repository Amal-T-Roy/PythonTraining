def student_info(*args,**kwargs) :
    print(args)
    print(kwargs)

courses = ['Maths','Science'] #list
info = {'name' : 'Dude' , 'age' : 22} #dictionary

student_info(*courses,**info) 
student_info(courses,info) 
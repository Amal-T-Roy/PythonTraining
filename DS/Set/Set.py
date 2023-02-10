Set1  = {9,8,7,6,5,4,3,2}
print(Set1)

science_courses = {'Bio','Maths','chemistry','English','Maths'}
commerce_courses = {'Accountancy','Maths','Logistics','English'}
#science_courses.remove('Bio') #remove from set
#science_courses.add('Physics') #add to set


#Duplicates are ignored->Takes only 1st occurence
print(science_courses)

#Membership check for an element
print('Maths' in science_courses)

#to print common courses
print(science_courses.intersection(commerce_courses))
#to print courses exclusive for science stream
print(science_courses.difference(commerce_courses))
#to print total courses
print(science_courses.union(commerce_courses))
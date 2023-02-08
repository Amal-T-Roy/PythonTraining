#Super class i.e this is going to be inherited by other classes
class pet :
    def __init__(self,name,age) :
        self.name = name
        self.age =  age

    def show(self) :
        print(f"I am {self.name} and I am {self.age} years old")

class cat(pet) :
    def speak() :
        print('Meow')

class dog(pet) :
    def speak() :
        print('Bark!')

#instance of pet class
p = pet('Tom',10)
print(type(p))
p.show()

#instance of cat class
c = cat('Jerry',5)
print(type(c))
c.show() #inherited from pet class
print(c.age)

#instance of dog class
d = dog('Butch',18)
d.show()
dog.speak()
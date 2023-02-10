#upper level class i.e this is going to be inherited by other classes
class pet :
    def __init__(self,name,age) :
        self.name = name
        self.age =  age

    def show(self) :
        print(f"I am {self.name} and I am {self.age} years old")

class cat(pet) :
    def speak(self) :
        print('Meow')

class dog(pet) :
    def speak(self) :
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
c.speak() #method inside cat class

#instance of dog class
d = dog('Butch',18)
d.show()
d.speak()
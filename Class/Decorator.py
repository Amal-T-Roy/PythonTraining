class person :
    number_of_people = 0 #class attribute
    GRAVITY = 9.8

    def __init__(self,name) :
        self.name = name
        person.add_people() #increment no.of people every time class is initialised
    
    @classmethod #decorator
    def Number_of_people(cls) :
        return cls.number_of_people
    
    @classmethod #decorator
    def add_people(cls) :
        cls.number_of_people += 1

p1 = person('Dude') #will increment no.of people
p2 = person('Bruh') #will increment no.of people

print(person.Number_of_people())  

#increment the value
#person.add_people()
#print(person.Number_of_people())  

p3 = person('Bro')
print(p1.number_of_people)
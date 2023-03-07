# To make an object private,use double underscore.Single underscore makes it a partial private

class car:
    def __init__(self,speed,color) :
        self.__speed = speed
        self.__color = color
    def set_speed(self,value) : # Setter of sttribute
        self.__speed = value
    def get_speed(self) : # Getter of attribute
        return self.__speed
    def get_color(self) :
        return self.__color

Ford  = car(200,'Red')
Benz  = car(250,'Blue')

# print(Ford.color)
    
print(Ford.get_speed())
Ford.set_speed(300)
print(Ford.get_speed())
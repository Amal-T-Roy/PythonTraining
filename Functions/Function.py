def Hello_World() :
    return 'Hello World'

#Hello_World()
print(Hello_World())
print(Hello_World().upper())

def Greet(greeting,name = 'man') :
    return '{},{}'.format(greeting,name)

print(Greet('hey!','dude'))
print(Greet('hey!','John'))
print(Greet('hey!')) #No second parameter
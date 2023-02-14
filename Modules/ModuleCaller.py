from Calculations import * #Imports entire contents of the module
import Calculations as cal
from Anagram import AnagramChecker #Imports specified function from module
from Anagram import PalindromeChecker

print(y) #Variable in module called

print(add(5,6))
print(add(5,7))
print(add(8,9))

S1 = input('Enter String 1:\n')
S2 = input('Enter String 2:\n')

AnagramChecker(S1,S2) #Function defined in second imported file
print(PalindromeChecker(S1))

x = add #saved function object to a variable
print(x(100,200))

g = cal.modulusof(4,5) #aliased function
print('{} is the modulus'.format(g))

#Used to find correlation between points
from matplotlib import pyplot as plt

x = [1,2,3,4,5,6,7,8] #abscissa
y = [4,5,1,4,2,6,8,3] #ordinates

plt.scatter(x,y,label = 'test',color = 'r',s = 25,marker="o") 
"""
s->size of point
mark->Shape of the point(o,x,...etc)

"""


plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')

plt.legend()
plt.show()


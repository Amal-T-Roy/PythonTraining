#Used to track changes over time for one or more groups

from matplotlib import pyplot as plt

days = [1,2,3,4,5]

sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]

"""
With polygons we cant have labels for our data
So we draw some empty lines with same label with same color
Thus we can get the legend
"""
plt.plot([],[],color='m',label = 'sleeping',linewidth = 5)
plt.plot([],[],color = 'c',label = 'eating',linewidth = 5)
plt.plot([],[],color = 'r',label = 'working',linewidth = 5)


plt.stackplot(days,sleeping,eating,working,colors=['m','c','r'])
#First arg is the one in the x axis.we plot rest on y

plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('Scatter/Area Plot')

plt.legend()
plt.show()

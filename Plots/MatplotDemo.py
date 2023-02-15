from matplotlib import pyplot as plt

"""
plot canvas
Here,first list contain x-cordinates and second contain y-coordinates
values at same index create an ordered pair->eg:  (list1[0],list2[1])
This point is then plotted
"""

x = [1,2,3] #abscissa
y = [4,5,1] #ordinates

plt.plot(x,y)

#Name the axises and add title
plt.title('Info')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

#show output
plt.show()
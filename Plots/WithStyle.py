from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

#set input data for plot1
x = [5,8,10]
y = [12,16,6]

#set input data for plot1
x2 = [6,9,11]
y2 = [6,15,7]

#Plot the graphs
plt.plot(x,y,'g',label='L1',linewidth =3) #'g' sets colour = green
plt.plot(x2,y2,'r',label='L2',linewidth =3) #'r' sets colour = red

#Add titles and labels
plt.title('Compare Graphs')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

#Add legend
plt.legend()

#Add grid
plt.grid(True,color = 'k')

#Show the output
plt.show()

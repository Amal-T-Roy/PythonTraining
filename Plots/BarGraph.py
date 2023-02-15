import matplotlib.pyplot as plt

"""
    Bargraphs are used to visualise categorical data
"""

#Set input
bar1_x = [1,3,5,7]
bar1_y = [5,2,7,8]

bar2_x = [2,4,6,8]
bar2_y = [8,6,2,5]

#Plot bar graph
plt.bar(bar1_x,bar1_y,label = 'B1',color = 'r')
plt.bar(bar2_x,bar2_y,label = 'B2',color = 'g')

#Set labels and title
plt.title('Demo')
plt.xlabel = 'barnumber'
plt.ylabel = 'barheight'

#Add legend
plt.legend()

#To Add grid
# plt.grid(True,color = 'k')

#Show output
plt.show()
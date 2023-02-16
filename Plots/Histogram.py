import matplotlib.pyplot as plt

"""
    Histograms are used to visualize quantitative data.
    Here ages of a group of people is taken,which is to be represented as diff age groups
"""

#Set input
ages = [42,42,42,42,43,43,45,47,49,50,50,49,39.41,39,41,42,33,27,28,29,10,22,66,78,99,88,53,56,42,18,19,25,12]

sections = [0,10,20,30,40,50,60,70,80,90,100]

#Plot
# plt.hist(ages,sections,histtype='bar',rwidth=0.5) #Looks like bar graph
# plt.hist(ages,sections,histtype='barstacked',rwidth=0.5) #looks like bar graph when using only 1 dataset
plt.hist(ages,sections,histtype='step',rwidth=0.5) #step graph,with insides clear
#plt.hist(ages,sections,histtype='stepfilled',rwidth=0.5) #step graph,with insides filled

#Add labels
plt.xlabel('Age Range')
plt.ylabel('count')
plt.title('Age Representation')

#Add grid
plt.grid(True)

#Show plot
plt.show()
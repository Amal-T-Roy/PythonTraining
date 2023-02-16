from matplotlib import pyplot as plt

slices = [7, 2, 2, 14]
activities = ["sleeping", "eating", "working", "playing"]
cols = ["c", "r", "m", "b"]

plt.pie(
    slices,  # Input data
    labels=activities,  # Names of the slices
    colors=cols,  # Color of each slices
    startangle=90,  # Angle from which plotting starts->0 starts at 3'O clock,90 at 12 O clock
    shadow=(True, "b"),  # Set shadow
    explode=(0, 0.1, 0, 0),  # To make some slices pull outside
    autopct="%1.1f%%",  # Overlay the percentages on the slices
)
plt.title("Pie Plot")
plt.show()

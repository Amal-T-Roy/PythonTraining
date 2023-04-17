from tkinter import *

root = Tk()
root.title("DashBoard")

# Label1 = Label(root,text="Heading")
# Label2 = Label(root,text="Subtext")

def Click():
    Label1 = Label(root,text="Butten pressed!!")
    Label1.pack()
    # Label1.grid(row=2,column=0)

IgnitionButton = Button(root,text="Start/Stop",border=10,command=Click,bg="red",fg="white")
IgnitionButton.pack()

# Label1.grid(row=0,column=0)
# Label2.grid(row=1,column=5)

root.mainloop()

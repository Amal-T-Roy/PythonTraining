from tkinter import *

root = Tk()
root.title("Slider")
root.geometry("400x400")
Display = Entry(root,width=35,borderwidth=5)
# Display.grid(row=0,column=0,columnspan=3,padx=10,pady=10)





def DisplaySpeed(Speed):
    print(str(Speed))

Vertical = Scale(root,from_=0,to=200,showvalue=True,orient=HORIZONTAL,length=500,borderwidth=5)
Vertical.pack()

def slide():
    MyLabel = Label(text=Vertical.get()).pack()



MyButton  = Button(root,text="Click to update",command=slide).pack()

root.mainloop()
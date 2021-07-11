from tkinter import *
root = Tk()
#

e = Entry(root, bg="lightblue", width=200, borderwidth=5)
e.pack()
e.get()
e.insert(0, "Enter your name.")


def myClick():
    name = "Hello " + e.get() + "."
    myLabel = Label(root, text=name)
    myLabel.pack()

myButton = Button(root, text="Enter your name.", padx=50, pady=20, command=myClick, bg="#531235")
myButton.pack()




#MAIN RUNNING LOOP
root.mainloop()
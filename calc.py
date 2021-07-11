from tkinter import *
root = Tk()
root.title("Simple Calulator")

e = Entry(root, width=25, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def buttonAdd(number):
    #e.delete(0, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))

def buttonClear():
    e.delete(0, END)

def buttonPlus():
    firstNumber = e.get()
    global fNum
    fNum = int(firstNumber)
    e.delete(0, END)

def buttonEqual():
    secondNumber = e.get()
    e.delete(0, END)
    e.insert(0, fNum + int(secondNumber))


#Define buttons

button0 = Button(root, text="0", padx=40, pady=20, command=lambda: buttonAdd(0))
button1 = Button(root, text="1", padx=40, pady=20, command=lambda: buttonAdd(1))
button2 = Button(root, text="2", padx=40, pady=20, command=lambda: buttonAdd(2))
button3 = Button(root, text="3", padx=40, pady=20, command=lambda: buttonAdd(3))
button4 = Button(root, text="4", padx=40, pady=20, command=lambda: buttonAdd(4))
button5 = Button(root, text="5", padx=40, pady=20, command=lambda: buttonAdd(5))
button6 = Button(root, text="6", padx=40, pady=20, command=lambda: buttonAdd(6))
button7 = Button(root, text="7", padx=40, pady=20, command=lambda: buttonAdd(7))
button8 = Button(root, text="8", padx=40, pady=20, command=lambda: buttonAdd(8))
button9 = Button(root, text="9", padx=40, pady=20, command=lambda: buttonAdd(9))
buttonPlus = Button(root, text="+", padx=40, pady=20, command=buttonPlus)
buttonClear = Button(root, text="Clear", padx=30, pady=20, command= buttonClear)
buttonEqual = Button(root, text="=", padx=40, pady=20, command=buttonEqual)

#putting buttons on screen

buttonEqual.grid(row=5, column=1)
buttonClear.grid(row=4, column=2)
buttonPlus.grid(row=4, column=1)
button0.grid(row=4, column=0)
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)



######
root.mainloop()
from tkinter import *
root = Tk()
root.geometry("475x200")
f1 = Frame(root)
f1.pack()
Label(f1,text = "This is the form to enter the name of dance participants...").pack()
f2 = Frame(root).pack()
Label(f2,text = "Enter the name").pack()

root.mainloop()
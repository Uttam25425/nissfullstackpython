from tkinter import *
def add():
	n1=int(e1.get())
	n2=int(e2.get())
	result=n1+n2
	lbl.config(text="result="+str(result))

root=Tk()
root.title("Addition App")
root.geometry("300x200")

Label(root,text="Enter first number").pack()
e1=Entry(root)
e1.pack()

Label(root,text="Enter your second number").pack()

lbl=Label(root,text="")
lbl.pack()

root.mainloop()
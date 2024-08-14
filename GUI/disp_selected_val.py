# from tkinter import *
# from tkinter import messagebox
# def show():
#     s1=val.get()
#     messagebox.showinfo("class",s1)

# window=Tk()
# window.geometry("400x300")
# val=StringVar()
# r1=Radiobutton(window,text="fy",value="fybca",variable=val)
# r2=Radiobutton(window,text="sy",value="sybca",variable=val)
# r3=Radiobutton(window,text="ty",value="tybca",variable=val)
# b1=Button(window,text="ok",command=show)
# r1.grid(row=0,column=0)
# r2.grid(row=0,column=1)
# r3.grid(row=0,column=2)
# b1.grid(row=1,column=2)
# window.mainloop()

from tkinter import *
from tkinter import messagebox
def show():
    s1=val.get()
    messagebox.showinfo("class",s1)


window=Tk()
window.geometry("300x400")
val=StringVar()
r1=Radiobutton(window,text="orange",value="orange",variable=val)
r2=Radiobutton(window,text="papaya",value="papaya",variable=val)
r3=Radiobutton(window,text="banana",value="banana",variable=val)
b1=Button(window,text="select",command=show)
r1.grid(row=0,column=0)   
r2.grid(row=1,column=0) 
r3.grid(row=2,column=0) 
b1.grid(row=3,column=0) 
window.mainloop()














from tkinter import *
def disp_squre():
    n=t1.get()
    n=int(n)
    s=n*n
    t2.insert(0,s)

window=Tk()
window.geometry("500x400")
l1=Label(window,text="ener no :")
l2=Label(window,text="result:")
t1=Entry(window,width="10")
t2=Entry(window,width="10")
b1=Button(window,text="squre",command=disp_squre)
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
b1.grid(row=2,column=1)
window.mainloop()

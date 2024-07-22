# from tkinter import *
# window=Tk()
# def disp_name():
#     s=t1.get()
#     t2.insert(0,s)

# window.geometry("500x300")
# l1=Label(window,text="enter name :")
# l2=Label(window,text="ur name :")
# t1=Entry(window,width="10")
# t2=Entry(window,width="10")
# b1=Button(window,text="display",command=disp_name)

# l1.grid(row=0,column=0)
# l2.grid(row=1,column=0)
# t1.grid(row=0,column=1)
# t2.grid(row=1,column=1)
# b1.grid(row=2,column=1)
# window.mainloop()

from tkinter import *
def coloris():
    s=t1.get()
    t2.insert(0,s)

window=Tk()
window.geometry("500x300")
l1=Label(window,text="enter color :")
l2=Label(window,text="your selected color :")
t1=Entry(window,width="10")
t2=Entry(window,width="10")
b1=Button(window,text="your name :",command=coloris)

l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
t1.grid(row=0,column=1)
t2.grid(row=1,column=1)
b1.grid(row=2,column=1)
window.mainloop()










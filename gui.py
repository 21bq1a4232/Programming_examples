from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("hello AlluArjun")
window.geometry('500x300')
def clicked():
    messagebox.showinfo("HELLO",'click "ok" to exit')
btn=Button(window,text='click here',command=clicked)
b=Button(window,text="exit",command=exit)
b.grid(column=1,row=1)
btn.grid(column=0,row=0)
window.mainloop()
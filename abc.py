from tkinter import *

win = Tk()

def num(event) :
    lb1["text"] = int(lb1["text"]) + int(entry.get())
def click() :
    lb1["text"] = 0

entry = Entry(win)
entry.bind("<Return>", num)
entry.pack()
lb1 = Label(win, text = "0")
btn = Button(win, text = "clear", fg = "black", bg = "white", command  = click)
lb1.pack()
btn.pack()
win.mainloop()






















    

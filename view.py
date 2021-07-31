# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter
from tkinter import *






if __name__=='__main__':
    root = Tk()

    menubar = tkinter.Menu(root)
    root['menu'] = menubar

    filebar = tkinter.Menu(menubar, tearoff=False)
    editbar = tkinter.Menu(menubar, tearoff=False)
    otherbar = tkinter.Menu(menubar, tearoff=False)

    menubar.add_cascade(label='File', menu=filebar)
    menubar.add_cascade(label='Edit', menu=editbar)
    menubar.add_cascade(label='Other', menu=otherbar)

    filebar.add_command(label='Open')
    filebar.add_command(label='Choice Device')

    editbar.add_command(label='Copy')
    otherbar.add_command(label='Exit', command=root.quit)
    root.title("APP性能测试 v1.0")
    root.geometry("800x500+300+200")
    root.mainloop()
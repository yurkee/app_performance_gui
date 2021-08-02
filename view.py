# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import tkinter
from tkinter import *
from app_performance import AppPerformance

ap = AppPerformance()








root = Tk()

menubar = Menu(root)
root['menu'] = menubar

filebar = Menu(menubar, tearoff=False)
editbar = Menu(menubar, tearoff=False)
otherbar = Menu(menubar, tearoff=False)

menubar.add_cascade(label='Select', menu=filebar)
menubar.add_cascade(label='Edit', menu=editbar)
menubar.add_cascade(label='Other', menu=otherbar)

filebar.add_command(label='DeviceName', command=ap.get_device_name)
filebar.add_command(label='ChoiceDevice')

editbar.add_command(label='Copy')

otherbar.add_command(label='Exit', command=root.quit)

frame = Frame(root)
deviceLabel = Label(frame, text='设置执行次数：')
deviceLabel.pack(side=LEFT, padx=5, pady=5)
frame.pack()

countVar = StringVar()
countLabel = Entry(frame, text='countlabel',width=10)
countLabel.pack(side=LEFT, padx=5, pady=5)




root.title("APP性能测试 v1.0")
root.geometry("800x500+300+200")
root.mainloop()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
James Maher & Drew Gross
EC552 Spring 22 Final Project
"""
from tkinter import *
from PIL import ImageTk, Image
# from tkinter.ttk import *

window = Tk()
window.title("DNA Assembly Optimization Tool")
window.geometry('1400x800')

"""
frame = Frame(window)
frame.grid(column=3,row=4)
frame.place(anchor = 'ne', relx=0.5, rely=0.5)

img = Image.open("Lachesis.png")
img_resize = img.resize((200,300), Image.ANTIALIAS)
newim = ImageTk.PhotoImage(img_resize)
imlabel = Label(frame, image = newim)
imlabel.grid(column=3,row=4)
"""

info = Label(window, text="Enter parameters and create assemblies!", font=("Times New Roman",18))
info.grid(column=1,row=0)

tit = Label(window, text="Lachesis", font=("Comic Sans MS",48))
tit.grid(column=0,row=0)

partenter = Entry(window, width = 10)
partenter.grid(column=0,row=3)
partenter.focus()

partlabel = Label(window, text="Enter part to assemble below:")
partlabel.grid(column=0,row=2)

optienter = Listbox(window, exportselection=False)
optienter.insert(1, "Cost")
optienter.insert(2, "Computation Time")
optienter.insert(3, "Both")
optienter.insert(4, "Neither")
optienter.grid(column=2,row=2)

optilabel = Label(window, text = "Select paramters to optimize for:")
optilabel.grid(column=2,row=1)

aoenter = Listbox(window, exportselection=False)
aoenter.insert(1, "Cost")
aoenter.insert(2, "Computation Time")
aoenter.insert(3, "Both")
aoenter.insert(4, "Neither")
aoenter.grid(column=2,row=4)

aolabel = Label(window, text = "Select paramters to optimize against:")
aolabel.grid(column=2,row=3)

graphbestlabel = Label(window, text="Assembly Tree for Optimized Assembly Process",font= ('Aerial', 18))
graphbestlabel.grid(column=1,row=1)

graphBest= Label(window, text= "Assembly tree will\n print here.")
graphBest.grid(column=1,row=2)

graphworstlabel = Label(window, text="Assembly Tree for Optimized Assembly Process",font= ('Aerial', 18))
graphworstlabel.grid(column=1,row=3)

graphWorst= Label(window, text= "Assembly tree will\n print here.")
graphWorst.grid(column=1,row=4)

def clicked():
    part = partenter.get()
    optimization = optienter.get(optienter.curselection())
    deoptimization = aoenter.get(aoenter.curselection())
    info.configure(text="Re-enter parameters and create new assemblies!")
    
RunButton = Button(window, text="Generate Assembly Protocol(s)", command=clicked, fg="green",bg="white")
RunButton.grid(column=2,row=5)

window.mainloop()

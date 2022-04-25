#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
James Maher & Drew Gross
EC552 Spring 22 Final Project
"""
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.title("DNA Assembly Optimization Tool")
window.geometry('1400x800')

info = Label(window, text="Enter parameters and create assemblies!", font=("Times New Roman",18))
info.grid(column=0,row=0)

partenter = Entry(window, width = 10)
partenter.grid(column=1,row=1)
partenter.focus()

partlabel = Label(window, text="Enter part to assemble below:")
partlabel.grid(column=1,row=0)

optienter = Combobox(window)
optienter['values']=("Cost", "Computation Time", "Both", "Neither")
optienter.grid(column=2,row=1)

optilabel = Label(window, text = "Select paramters to optimize for")
optilabel.grid(column=2,row=0)

aoenter = Combobox(window)
aoenter['values']=("Cost", "Computation Time", "Both", "Neither")
aoenter.grid(column=2,row=3)

aolabel = Label(window, text = "Select paramters to optimize against")
aolabel.grid(column=2,row=2)

def clicked():
    part = partenter.get()
    optimization = optienter.get()
    deoptimation = aoenter.get()
    info.configure(text="Re-enter parameters and create new assemblies!")
    
RunButton = Button(window, text="Generate Assembly Protocol(s)", command=clicked)
RunButton.grid(column=0,row=1)

window.mainloop()

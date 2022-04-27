#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
James Maher & Drew Gross
EC552 Spring 22 Final Project
"""
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import ctypes
import os
# from tkinter.ttk import *

cwd = os.getcwd()

window = Tk()
window.title("DNA Assembly Optimization Tool")
window.geometry('1400x800')

###Option to upload .csv file
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File",filetypes = (("CSV files","*.csv*"),("all files","*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)

filename = "dataset.csv"
label_file_explorer = Label(window,text = " ",fg = "indigo") 
button_explore = Button(window, text = "Browse Files",command = browseFiles)
label_file_explorer.grid(column = 0, row = 5)
button_explore.grid(column = 0, row = 4)



img = Image.open("LachesisWorst.png")
img_resize = img.resize((250,250), Image.Resampling.LANCZOS)
newim_W = ImageTk.PhotoImage(img_resize)

img = Image.open("LachesisBest.png")
img_resize = img.resize((250,250), Image.Resampling.LANCZOS)
newim_B = ImageTk.PhotoImage(img_resize)

img = Image.open("AnimeLachesis.png")
img_resize = img.resize((150,150), Image.Resampling.LANCZOS)
UI_flair = ImageTk.PhotoImage(img_resize)

info = Label(window, image=UI_flair)
info.grid(column=0,row=1)

info = Label(window, text="Enter parameters and create assemblies!", font=("Times New Roman",18))
info.grid(column=1,row=0)

tit = Label(window, text="Lachesis",fg="indigo", font=("Times New Roman",48))
tit.grid(column=0,row=0)

partenter = Entry(window, width = 10)
partenter.grid(column=0,row=3)
partenter.focus()

partlabel = Label(window, text="Enter part (a.b.c.d) to assemble below:")
partlabel.grid(column=0,row=2)

optienter = Listbox(window, exportselection=False,height=4)
optienter.insert(1, "Cost")
optienter.insert(2, "Computation Time")
optienter.insert(3, "Both")
optienter.insert(4, "Neither")
optienter.grid(column=2,row=2)

optilabel = Label(window, text = "Select paramters to optimize for:")
optilabel.grid(column=2,row=1)

aoenter = Listbox(window, exportselection=False,height=4)
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

graphworstlabel = Label(window, text="Assembly Tree for De-Optimized Assembly Process",font= ('Aerial', 18))
graphworstlabel.grid(column=1,row=3)

graphWorst= Label(window, text= "Assembly tree will\n print here.")
graphWorst.grid(column=1,row=4)

def clicked():
    part = partenter.get()
    optimization = optienter.get(optienter.curselection())
    deoptimization = aoenter.get(aoenter.curselection())
    info.configure(text="Re-enter parameters and create new assemblies!")
    graphWorst.configure(image = newim_W)
    graphBest.configure(image = newim_B) ### need different variable
    interface = ctypes.CDLL(cwd+'/project.cpp')
    interface.main_interface(filename, part, optimization, deoptimization)
    
RunButton = Button(window, text="Generate Assembly Protocol(s)", command=clicked, fg="green",bg="white")
RunButton.grid(column=2,row=5)

window.mainloop()

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
import sys
# from tkinter.ttk import *

cwd = os.getcwd()

window = Tk()
window.title("DNA Assembly Optimization Tool")
window.geometry('1200x700')

###Option to upload .csv file
def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/", title = "Select a File", filetypes = (("CSV files","*.csv*"),("all files","*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)

filename = "dataset.csv"
label_file_explorer = Label(window,text = " ",fg = "indigo") 
button_explore = Button(window, text = "Browse .csv Files",command = browseFiles)
label_file_explorer.grid(column = 0, row = 6)
button_explore.grid(column = 0, row = 5)


img = Image.open("AnimeLachesis.png")
img_resize = img.resize((165,165), Image.Resampling.LANCZOS)
UI_flair = ImageTk.PhotoImage(img_resize)

info = Label(window, image=UI_flair)
info.grid(column=0,row=2)

info = Label(window, text="Enter parameters \nand create assemblies!", fg="indigo", font=("Times New Roman",18))
info.grid(column=1,row=0)

tit = Label(window, text="Lachesis",fg="indigo", font=("Times New Roman",48))
tit.grid(column=0,row=0)

partenter = Entry(window, width = 10)
partenter.grid(column=0,row=4)
partenter.focus()

stage_txt = Label(window, text="Cost ($) per Stage", font=("Times New Roman",12))
stage_txt.grid(column=3,row=2)

step_txt = Label(window, text="Cost($) per Step", font=("Times New Roman",12))
step_txt.grid(column=3,row=3)

cost_stage = Entry(window, width = 10)
cost_stage.grid(column=4,row=2)
cost_stage.focus()

cost_step = Entry(window, width = 10)
cost_step.grid(column=4,row=3)
cost_step.focus()

partlabel = Label(window, text="Enter part (a.b.c.d) to assemble below:")
partlabel.grid(column=0,row=3)

# optienter = Listbox(window, exportselection=False,height=4)
# optienter.insert(1, "Cost")
# optienter.insert(2, "Computation Time")
# optienter.insert(3, "Both")
# optienter.insert(4, "Neither")
# optienter.grid(column=2,row=2)

# optilabel = Label(window, text = "Select paramters to optimize for:")
# optilabel.grid(column=2,row=1)

# aoenter = Listbox(window, exportselection=False,height=4)
# aoenter.insert(1, "Cost")
# aoenter.insert(2, "Computation Time")
# aoenter.insert(3, "Both")
# aoenter.insert(4, "Neither")
# aoenter.grid(column=2,row=4)

# aolabel = Label(window, text = "Select paramters to optimize against:")
# aolabel.grid(column=2,row=3)

graphbestlabel = Label(window, text="Assembly Tree for \nOptimized Assembly Process",font= ('Aerial', 18))
graphbestlabel.grid(column=1,row=1)

graphBest= Label(window, text= "Assembly tree will\n print here.")
graphBest.grid(column=1,row=2)

graphworstlabel = Label(window, text="Assembly Tree for \nDe-Optimized Assembly Process",font= ('Aerial', 18))
graphworstlabel.grid(column=1,row=3)

graphWorst= Label(window, text= "Assembly tree will\n print here.")
graphWorst.grid(column=1,row=4)

errormsg = Label(window,text=" ")
errormsg.grid(column=3,row=6)

def clicked():
    
    while len(partenter.get()) == 0 or len(cost_stage.get()) == 0 or len(cost_step.get()) == 0:
        errormsg.configure(text="Fill all fields!", fg="red", font=("Times New Roman",18))
        return
    # optimization = optienter.get(optienter.curselection())
    # deoptimization = aoenter.get(aoenter.curselection())
    errormsg.configure(text=" ")
    part = partenter.get()
    stage_cost = cost_stage.get()
    step_cost = cost_step.get()
    
    info.configure(text="Re-enter parameters and create new assemblies!")
    interface = ctypes.CDLL(cwd+'/project.cpp')
    if ".csv" in filename and len(filename) != 0:  ## checks if .csv file chosen
        if len(part) !=0:                           ## appends text input to csv file if it exists
            with open(filename,'a') as fd:
                fd.write(myCsvRow)
                [imfile_Best, imfile_Worst] = interface.main_interface(fd, cost_stage, cost_step)  ## argument is appended csv file
        else:
            [imfile_Best, imfile_Worst] = interface.main_interface(filename, cost_stage, cost_step) ## argument is unedited csv
    else:
        [imfile_Best, imfile_Worst] = interface.main_interface(part, cost_stage, cost_step) ## argument is text input only if no filename chosen
    img = Image.open(imfile_Worst)
    img_resize = img.resize((250,250), Image.Resampling.LANCZOS)
    newim_W = ImageTk.PhotoImage(img_resize)

    img = Image.open(imfile_Best)
    img_resize = img.resize((250,250), Image.Resampling.LANCZOS)
    newim_B = ImageTk.PhotoImage(img_resize)
    graphWorst.configure(image = newim_W)
    graphBest.configure(image = newim_B)
    graphBest.configure(text="a     b     c     d\n\\     /     \\     /\nab        cd\n  \\      /\n    abcd")
    graphWorst.configure(text="a     b     c     d\n\\    /      |     |\nab        c    d\n \\        /     |\n   \\    /       |\n     abc       d\n   \\        /\n     \\    /\n     abcd")

RunButton = Button(window, text="Generate Assembly Protocol(s)", command=clicked, fg="green",bg="white")
RunButton.grid(column=3,row=5)

window.mainloop()

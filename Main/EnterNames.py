from tkinter import *  
from PIL import ImageTk,Image
import random


root = Tk()
canvas = Canvas(root, width = 2000, height = 2000)
canvas.config(bg="white")
canvas.pack()

names = []
def getName(name1):
    name1 = (entry1.get())
    names.append(name1)
    namesLabel1 = Label(root, height=2, font=("Arial", 20), fg="white", bg="green", text=name1)
    namesLabel1.pack()
    canvas.create_window(600, 200, anchor=NW, window=namesLabel1)
    
def getName2(name2):
    name2 = (entry2.get())
    names.append(name2)
    namesLabel2 = Label(root, height=2, font=("Arial", 20), fg="white", bg="green", text=name2)
    namesLabel2.pack()
    canvas.create_window(600, 300, anchor=NW, window=namesLabel2)
    
def getName3(name3):
    name3 = (entry3.get())
    names.append(name3)
    namesLabel3 = Label(root, height=2, font=("Arial", 20), fg="white", bg="green", text=name3)
    namesLabel3.pack()
    canvas.create_window(600, 400, anchor=NW, window=namesLabel3)
    
def getName4(name4):
    name4 = (entry4.get())
    names.append(name4)
    namesLabel4 = Label(root, height=2, font=("Arial", 20), fg="white", bg="green", text=name4)
    namesLabel4.pack()
    canvas.create_window(600, 500, anchor=NW, window=namesLabel4)

def createNames():
    namesList = (" ".join(names))
    namesLabel = Label(root, text=str(namesList))
    namesLabel.pack()
    canvas.create_window(200, 600, anchor=NW, window=namesLabel)
    

name1 = Label(root, text="name of player 1:")
name1.pack()
name2 = Label(root, text="name of player 2:")
name2.pack()
name3 = Label(root, text="name of player 3:")
name3.pack()
name4 = Label(root, text="name of player 4:")
name4.pack()
entry1 = Entry(root)
entry1.bind('<Return>',getName)
entry1.pack()
entry2 = Entry(root)
entry2.bind('<Return>',getName2)
entry2.pack()
entry3 = Entry(root)
entry3.bind('<Return>',getName3)
entry3.pack()
entry4 = Entry(root)
entry4.bind('<Return>',getName4)
entry4.pack()

canvas.create_window(200, 200, anchor=NW, window=name1)
canvas.create_window(400, 200, anchor=NW, window=entry1)
canvas.create_window(200, 300, anchor=NW, window=name2)
canvas.create_window(400, 300, anchor=NW, window=entry2)
canvas.create_window(200, 400, anchor=NW, window=name3)
canvas.create_window(400, 400, anchor=NW, window=entry3)
canvas.create_window(200, 500, anchor=NW, window=name4)
canvas.create_window(400, 500, anchor=NW, window=entry4)


createNames()
        

root.mainloop()

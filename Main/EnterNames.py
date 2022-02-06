from tkinter import *  
from PIL import ImageTk,Image
import random


root = Tk()
canvas = Canvas(root, width = 2000, height = 2000)
canvas.config(bg="white")
canvas.pack()

def nextPage():
    root.destroy()
    import HTBQuestionGenerate

namesFile = open("namesFile.txt", "w")
names = []
def getName(name1):
    name1 = (entry1.get())
    names.append(name1)
    namesLabel1 = Label(root, height=2, font=("Arial", 20), fg="white", bg="green", text=name1)
    namesLabel1.pack()
    canvas.create_window(600, 220, anchor=NW, window=namesLabel1)
    namesFile.write(name1+ "\n")
    
def getName2(name2):
    name2 = (entry2.get())
    names.append(name2)
    namesLabel2 = Label(root, height=2, font=("Arial", 20), fg="white", bg="green", text=name2)
    namesLabel2.pack()
    canvas.create_window(600, 320, anchor=NW, window=namesLabel2)
    namesFile.write(name2+ "\n")
    
def getName3(name3):
    name3 = (entry3.get())
    names.append(name3)
    namesLabel3 = Label(root, height=2, font=("Arial", 20), fg="white", bg="green", text=name3)
    namesLabel3.pack()
    canvas.create_window(600, 420, anchor=NW, window=namesLabel3)
    namesFile.write(name3+ "\n")
    
def getName4(name4):
    name4 = (entry4.get())
    names.append(name4)
    namesLabel4 = Label(root, height=2, font=("Arial", 20), fg="white", bg="green", text=name4)
    namesLabel4.pack()
    canvas.create_window(600, 520, anchor=NW, window=namesLabel4)
    namesFile.write(name4+ "\n")

titleImg = Image.open("images/IMG_0403.jpg")
titleImg = titleImg.resize((750, 150), Image.ANTIALIAS)
titleImg = ImageTk.PhotoImage(titleImg)
canvas.create_image(180, 50, anchor=NW, image=titleImg)



name1 = Label(root, text="Name of player 1:")
name1.pack()
name2 = Label(root, text="Name of player 2:")
name2.pack()
name3 = Label(root, text="Name of player 3:")
name3.pack()
name4 = Label(root, text="Name of player 4:")
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

canvas.create_window(200, 220, anchor=NW, window=name1)
canvas.create_window(400, 220, anchor=NW, window=entry1)
canvas.create_window(200, 320, anchor=NW, window=name2)
canvas.create_window(400, 320, anchor=NW, window=entry2)
canvas.create_window(200, 420, anchor=NW, window=name3)
canvas.create_window(400, 420, anchor=NW, window=entry3)
canvas.create_window(200, 520, anchor=NW, window=name4)
canvas.create_window(400, 520, anchor=NW, window=entry4)


submitButtonImg = Image.open("images/IMG_0402.jpg")
submitButtonImg = submitButtonImg.resize((250, 120), Image.ANTIALIAS)
submitButtonImg = ImageTk.PhotoImage(submitButtonImg)
submitButton = Button(root, image=submitButtonImg, command=nextPage)
submitButton.pack()
canvas.create_window(200, 600, anchor=NW, window=submitButton)

root.mainloop()

namesFile.close()

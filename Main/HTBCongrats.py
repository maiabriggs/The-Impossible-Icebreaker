from tkinter import *
from PIL import ImageTk,Image
import random

def startGame():
    print("Start game")
    
root = Tk()
canvas = Canvas(root, width = 2000, height = 2000)
canvas.config(bg="white")
canvas.pack()

buttonImg = Image.open("/Users/paulinagerchuk/Documents/IMG_0407.jpg")
buttonImg = buttonImg.resize((500, 300), Image.ANTIALIAS)
buttonImg = ImageTk.PhotoImage(buttonImg)
button = Button(root, image=buttonImg, command=startGame, font=("Arial",20), compound=CENTER)
button.pack()
canvas.create_window(500, 300, anchor=NW, window=button)

root.mainloop()

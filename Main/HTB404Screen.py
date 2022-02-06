from tkinter import *
from PIL import ImageTk,Image
import random

def startGame():
    print("Start game")
    
root = Tk()
canvas = Canvas(root, width = 2000, height = 2000)
canvas.config(bg="#bdfaa3")
canvas.pack()

buttonImg = Image.open("images/IMG_0408.jpg")
buttonImg = buttonImg.resize((700, 450), Image.ANTIALIAS)
buttonImg = ImageTk.PhotoImage(buttonImg)
canvas.create_image(400, 150, anchor=NW, image=buttonImg)

root.mainloop()

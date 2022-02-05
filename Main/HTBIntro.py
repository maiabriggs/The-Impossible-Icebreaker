from tkinter import *  
from PIL import ImageTk,Image

def startGame():
    print("Game start")

root = Tk()
canvas = Canvas(root, width = 2000, height = 2000)
canvas.config(bg="white")
canvas.pack()  
title = Image.open("/Users/paulinagerchuk/Documents/IMG_0398.jpg")
title = title.resize((650, 350), Image.ANTIALIAS)
title = ImageTk.PhotoImage(title)
beginButtonImg = Image.open("/Users/paulinagerchuk/Documents/IMG_0399.jpg")
beginButtonImg = beginButtonImg.resize((300, 150), Image.ANTIALIAS)
beginButtonImg = ImageTk.PhotoImage(beginButtonImg)
beginButton = Button(root, image=beginButtonImg, command=startGame)
beginButton.pack()
canvas.create_image(400, 50, anchor=NW, image=title)
canvas.create_window(550, 450, anchor=NW, window=beginButton)
root.mainloop()


#figure out placement
#add button
#change image when hovered over

from tkinter import *  
from PIL import ImageTk,Image

def nextPage():
    root.destroy()
    import question1

#setting up canvas with white background
root = Tk()
canvas = Canvas(root, width = 2000, height = 2000)
canvas.config(bg="white")
canvas.pack()  

#open title image as Image, resize, then save as PhotoImage so its displayed in TKinter
title = Image.open("/home/maia/Documents/The-Impossible-Icebreaker/images/imposIcebreaker.JPG")
title = title.resize((650, 350), Image.ANTIALIAS)
title = ImageTk.PhotoImage(title)

#open, resize, and save buttonImage as a PhotoImage
beginButtonImg = Image.open("/home/maia/Documents/The-Impossible-Icebreaker/images/IMG_0399.jpg")
beginButtonImg = beginButtonImg.resize((300, 150), Image.ANTIALIAS)
beginButtonImg = ImageTk.PhotoImage(beginButtonImg)
#make a button with the beginButtonImg image inside it
beginButton = Button(root, image=beginButtonImg, command=nextPage)
beginButton.pack()

#create objects of both images on canvas and choose their location
canvas.create_image(400, 50, anchor=NW, image=title)
canvas.create_window(550, 450, anchor=NW, window=beginButton)
root.mainloop()


from tkinter import *  
from PIL import ImageTk,Image

root = Tk()
canvas = Canvas(root, width = 2000, height = 2000)
canvas.config(bg="white")
canvas.pack()

def nextPage():
    root.destroy()
    import question1

tag_yourself = Image.open("images/TagYourself.jpg")
tag_yourself = tag_yourself.resize((800, 496), Image.ANTIALIAS)
tag_yourself = ImageTk.PhotoImage(tag_yourself)

canvas.create_image(750, 300, anchor='center', image=tag_yourself)

root.mainloop()
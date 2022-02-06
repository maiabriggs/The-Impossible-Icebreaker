from tkinter import *  
from PIL import ImageTk,Image

def nextPage():
    root.destroy()
    import HTBIntro

root = Tk()
canvas = Canvas(root, width = 2000, height = 2000)
canvas.config(bg="white")
canvas.pack()  
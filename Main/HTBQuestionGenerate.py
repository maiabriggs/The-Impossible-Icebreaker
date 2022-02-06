from tkinter import *
from PIL import ImageTk,Image
import random
from importlib import reload
import QuestionCount as qc

def nextPage():
    if qc.count == 0:
        root.destroy()
        import question1
    else:
        print(qc.count)
        qc.decrease()
        root.destroy()
        import HTBQuestionGenerate2
        reload(HTBQuestionGenerate2) 

path_to_qSet1 = "TestQuestions.txt"
f = open("namesFile.txt", "r")

root = Tk()
canvas = Canvas(root, width = 2000, height = 2000)
canvas.config(bg="white")
canvas.pack()

root.title("Learning how to use tkinter")

#filename of question set 1 path variable at top
with open(path_to_qSet1) as file:
    questionsList = file.read().splitlines()
    
question = random.choice(questionsList)

print(question)

#making name buttons
#uploading names from file into variables
namesFile = f
player1 = namesFile.readline()
player2 = namesFile.readline()
player3 = namesFile.readline()
player4 = namesFile.readline()

message = Label(root, height=2, font=("Arial", 20), text = question)
message.pack()
canvas.create_window(200, 100, anchor=NW, window=message)


buttonImg = Image.open("images/IMG_0401.jpg")
buttonImg = buttonImg.resize((250, 120), Image.ANTIALIAS)
buttonImg = ImageTk.PhotoImage(buttonImg)
button = Button(root, image=buttonImg, command=nextPage, text=player1, font=("Arial",20), compound=CENTER)
button.pack()
canvas.create_window(200, 300, anchor=NW, window=button)


button = Button(root, image=buttonImg, command=nextPage, text=player2, font=("Arial",20), compound=CENTER)
button.pack()
canvas.create_window(600, 300, anchor=NW, window=button)

button = Button(root, image=buttonImg, command=nextPage, text=player3, font=("Arial",20), compound=CENTER)
button.pack()
canvas.create_window(200, 500, anchor=NW, window=button)

button = Button(root, image=buttonImg, command=nextPage, text=player4, font=("Arial",20), compound=CENTER)
button.pack()
canvas.create_window(600, 500, anchor=NW, window=button)

root.mainloop()

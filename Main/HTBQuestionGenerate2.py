from tkinter import *
from PIL import ImageTk,Image
import random
from importlib import reload
import QuestionCount as qc

def nextPage():
    qc.decrease()
    root.destroy()
    import HTBQuestionGenerate
    reload(HTBQuestionGenerate)
    
def Create4Answers(canvas, answersArr):
    button = Button(root, image=buttonImg, command=nextPage, text=answersArr[0], font=("Arial",20), compound=CENTER)
    button.pack()
    canvas.create_window(200, 300, anchor=NW, window=button)

    button = Button(root, image=buttonImg, command=nextPage, text=answersArr[1], font=("Arial",20), compound=CENTER)
    button.pack()
    canvas.create_window(600, 300, anchor=NW, window=button)

    button = Button(root, image=buttonImg, command=nextPage, text=answersArr[2], font=("Arial",20), compound=CENTER)
    button.pack()
    canvas.create_window(200, 500, anchor=NW, window=button)

    button = Button(root, image=buttonImg, command=nextPage, text=answersArr[3], font=("Arial",20), compound=CENTER)
    button.pack()
    canvas.create_window(600, 500, anchor=NW, window=button)

def Create2Answers(canvas, answersArr):
    button = Button(root, image=buttonImg, command=nextPage, text=answersArr[0], font=("Arial",20), compound=CENTER)
    button.pack()
    canvas.create_window(200, 300, anchor=NW, window=button)

    button = Button(root, image=buttonImg, command=nextPage, text=answersArr[1], font=("Arial",20), compound=CENTER)
    button.pack()
    canvas.create_window(600, 300, anchor=NW, window=button)

path_to_qSet1 = "TestQuestions.txt"
namesFile = open("namesFile.txt", "r")
players = []
for i in range(4):
    players.append(namesFile.readline())


root = Tk()
canvas = Canvas(root, width = 2000, height = 2000)
canvas.config(bg="white")
canvas.pack()

root.title("Learning how to use tkinter")

#filename of question set 1 path variable at top
with open(path_to_qSet1) as file:
    questionsList = file.read().splitlines()
    
question = random.choice(questionsList).replace("[name]",random.choice(players))

print(question)

#making name buttons
#uploading names from file into variables

message = Label(root, height=2, font=("Arial", 20), text = question)
message.pack()
canvas.create_window(200, 100, anchor=NW, window=message)


buttonImg = Image.open("images/IMG_0401.jpg")
buttonImg = buttonImg.resize((250, 120), Image.ANTIALIAS)
buttonImg = ImageTk.PhotoImage(buttonImg)
#Create4Answers(canvas,players)
Create2Answers(canvas, ["Yes","No"])
root.mainloop()
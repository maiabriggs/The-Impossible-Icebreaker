from tkinter import *
from PIL import ImageTk,Image
import random
from importlib import reload
import QuestionCount as qc

def nextPage():
    if qc.count <= 0:
        root.destroy()
        import HTBCongrats
    else:
        print(qc.count)
        qc.decrease()
        root.destroy()
        import HTBQuestionGenerate2
        reload(HTBQuestionGenerate2) 
        
lives = 3
ans = random.randint(1,4)
def checkAnswer(num):
    global lives
    global ans
    if num==ans:
        print("correct lol")
    else:
        lives = lives - 1
        livesCount = Label(root, image=livesImg, text=str(lives), font=("Arial",20), compound=CENTER)
        livesCount.pack()
        canvas.create_window(800, 600, anchor=NW, window=livesCount)
        print("nope")
    nextPage()

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
players = []
for i in range(4):
    players.append(namesFile.readline())

message = Label(root, height=2, font=("Arial", 20), text = question)
message.pack()
canvas.create_window(200, 100, anchor=NW, window=message)


buttonImg = Image.open("images/IMG_0401.jpg")
buttonImg = buttonImg.resize((250, 120), Image.ANTIALIAS)
buttonImg = ImageTk.PhotoImage(buttonImg)
button = Button(root, image=buttonImg, command=lambda:checkAnswer(1), text=players[0], font=("Arial",20), compound=CENTER)
button.pack()
canvas.create_window(200, 300, anchor=NW, window=button)


button = Button(root, image=buttonImg, command=lambda:checkAnswer(2), text=players[1], font=("Arial",20), compound=CENTER)
button.pack()
canvas.create_window(600, 300, anchor=NW, window=button)

button = Button(root, image=buttonImg, command=lambda:checkAnswer(3), text=players[2], font=("Arial",20), compound=CENTER)
button.pack()
canvas.create_window(200, 500, anchor=NW, window=button)

button = Button(root, image=buttonImg, command=lambda:checkAnswer(4), text=players[3], font=("Arial",20), compound=CENTER)
button.pack()
canvas.create_window(600, 500, anchor=NW, window=button)

livesImg = Image.open("images/IMG_0404.jpg")
livesImg = livesImg.resize((200, 200), Image.ANTIALIAS)
livesImg = ImageTk.PhotoImage(livesImg)
livesCount = Label(root, image=livesImg, text=str(lives), font=("Arial",20), compound=CENTER)
livesCount.pack()
canvas.create_window(800, 600, anchor=NW, window=livesCount)

root.mainloop()

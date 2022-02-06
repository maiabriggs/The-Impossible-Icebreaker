from tkinter import *
from PIL import ImageTk,Image
import random
from importlib import reload
import QuestionCount as qc
import QuestionGen

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

def Create4Answers(canvas, answersArr):
    button = Button(root, image=buttonImg, command=lambda:checkAnswer4(1), text=answersArr[0], font=("Arial",20), compound=CENTER)
    button.pack()
    canvas.create_window(200, 300, anchor=NW, window=button)

    button = Button(root, image=buttonImg, command=lambda:checkAnswer4(2), text=answersArr[1], font=("Arial",20), compound=CENTER)
    button.pack()
    canvas.create_window(600, 300, anchor=NW, window=button)

    button = Button(root, image=buttonImg, command=lambda:checkAnswer4(3), text=answersArr[2], font=("Arial",20), compound=CENTER)
    button.pack()
    canvas.create_window(200, 500, anchor=NW, window=button)

    button = Button(root, image=buttonImg, command=lambda:checkAnswer4(4), text=answersArr[3], font=("Arial",20), compound=CENTER)
    button.pack()
    canvas.create_window(600, 500, anchor=NW, window=button)

def Create2Answers(canvas, answersArr):
    button = Button(root, image=buttonImg, command=lambda:checkAnswer2(1), text=answersArr[0], font=("Arial",20), compound=CENTER)
    button.pack()
    canvas.create_window(200, 300, anchor=NW, window=button)

    button = Button(root, image=buttonImg, command=lambda:checkAnswer2(2), text=answersArr[1], font=("Arial",20), compound=CENTER)
    button.pack()
    canvas.create_window(600, 300, anchor=NW, window=button)
        
lives = 3
def checkAnswer4(num):
    ans = random.randint(1,4)
    global lives
    global ans
    if num==ans:
        print("correct")
    else:
        lives = lives - 1
        livesCount = Label(root, image=livesImg, text=str(lives), font=("Arial",20), compound=CENTER)
        livesCount.pack()
        canvas.create_window(800, 600, anchor=NW, window=livesCount)
        print("nope")
    nextPage()
    
def checkAnswer2(num):
    ans = random.randint(1,2)
    global lives
    global ans
    if num==ans:
        print("correct")
    else:
        lives = lives - 1
        livesCount = Label(root, image=livesImg, text=str(lives), font=("Arial",20), compound=CENTER)
        livesCount.pack()
        canvas.create_window(800, 600, anchor=NW, window=livesCount)
        print("nope")
    nextPage()

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
    
question = QuestionGen.getQuestion().replace("[name]",random.choice(players))

print(question)

#making name buttons
#uploading names from file into variables

message = Label(root, height=2, font=("Arial", 20), text = question)
message.pack()
canvas.create_window(200, 100, anchor=NW, window=message)

buttonImg = Image.open("images/IMG_0401.jpg")
buttonImg = buttonImg.resize((250, 120), Image.ANTIALIAS)
buttonImg = ImageTk.PhotoImage(buttonImg)

livesImg = Image.open("images/IMG_0404.jpg")
livesImg = livesImg.resize((200, 200), Image.ANTIALIAS)
livesImg = ImageTk.PhotoImage(livesImg)
livesCount = Label(root, image=livesImg, text=str(lives), font=("Arial",20), compound=CENTER)
livesCount.pack()
canvas.create_window(800, 600, anchor=NW, window=livesCount)

root.mainloop()


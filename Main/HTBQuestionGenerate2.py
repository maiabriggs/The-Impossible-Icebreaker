from tkinter import *
from PIL import ImageTk,Image
import random
from importlib import reload
import QuestionCount as qc
import QuestionGen

def nextPage():
    qc.decrease()
    root.destroy()
    import HTBQuestionGenerate
    reload(HTBQuestionGenerate)
    
lives = 3
ans = random.randint(1,4)
def checkAnswer(num):
    if num==ans:
        print("correct lol")
    else:
        global lives
        lives = lives - 1
        livesCount = Label(root, image=livesImg, text=str(lives), font=("Arial",20), compound=CENTER)
        livesCount.pack()
        canvas.create_window(800, 600, anchor=NW, window=livesCount)
        print("nope")
    nextPage()

path_to_qSet1 = "TestQuestions.txt"

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
namesFile = open("namesFile.txt","r")
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
button1 = Button(root, image=buttonImg, command=lambda:checkAnswer(1), text=player1, font=("Arial",20), compound=CENTER)
button1.pack()
canvas.create_window(200, 250, anchor=NW, window=button1)

button2 = Button(root, image=buttonImg, command=lambda:checkAnswer(2), text=player2, font=("Arial",20), compound=CENTER)
button2.pack()
canvas.create_window(600, 250, anchor=NW, window=button2)

button3 = Button(root, image=buttonImg, command=lambda:checkAnswer(3), text=player3, font=("Arial",20), compound=CENTER)
button3.pack()
canvas.create_window(200, 450, anchor=NW, window=button3)

button4 = Button(root, image=buttonImg, command=lambda:checkAnswer(4), text=player4, font=("Arial",20), compound=CENTER)
button4.pack()
canvas.create_window(600, 450, anchor=NW, window=button4)

livesImg = Image.open("images/IMG_0404.jpg")
livesImg = livesImg.resize((200, 200), Image.ANTIALIAS)
livesImg = ImageTk.PhotoImage(livesImg)
livesCount = Label(root, image=livesImg, text=str(lives), font=("Arial",20), compound=CENTER)
livesCount.pack()
canvas.create_window(800, 600, anchor=NW, window=livesCount)

root.mainloop()

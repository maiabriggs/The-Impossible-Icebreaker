import tkinter as tk
import random

path_to_qSet1 = "../Archie/TestQuestions.txt"

window = tk.Tk()
window.title("Learning how to use tkinter")

with open(path_to_qSet1) as file:           #filename of question set 1 path variable at top
    questionsList = file.readlines()

questionChosen = random.choice(questionsList)
print(questionChosen)

message = tk.Label(window, text = questionChosen)
message.pack()

window.mainloop()

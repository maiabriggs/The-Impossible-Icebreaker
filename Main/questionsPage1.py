import tkinter as tk
import random

path_to_qSet1 = "../Archie/TestQuestions.txt"

window = tk.Tk()
window.title("Learning how to use tkinter")

message = tk.Label(window, text = "Testing tkinter")
message.pack()

with open(path_to_qSet1) as file:           #filename of question set 1 path variable at top
    questionsList = file.readlines()

questionChosen = random.choice(questionsList)
print(questionChosen)

window.mainloop()

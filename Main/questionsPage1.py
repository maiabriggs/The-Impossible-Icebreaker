import tkinter as tk

window = tk.Tk()
window.title("Learning how to use tkinter")

message = tk.Label(window, text = "Testing tkinter")
message.pack()

with open(questionsList.txt) as file:
    questionsList = file.readlines()

window.mainloop()

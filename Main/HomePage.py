import tkinter as tk
from PIL import Image
window=tk.Tk()
window.title("The Impossible Icebreaker")

message = tk.Label(window, text = "The Impossible Icebreaker")
message.pack()

def start():
    print("Start")

begin = tk.Button(
    window, 
    text = "Begin!",
    command = start())

begin.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

window.mainloop()
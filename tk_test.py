from tkinter import *
from tkinter import ttk


def button_click():
    text = entry.get()
    label["text"] = text


window = Tk()
window.title("Window & Widgets")
# window.geometry("800x500")

label = ttk.Label(window, text="Hello, World!")
label.pack()

entry = ttk.Entry(window)
entry.pack()

button = ttk.Button(window, text="Click Me!", command=button_click)
button.pack()


# run the main loop
window.mainloop()

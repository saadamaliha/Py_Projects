"""
This program is a GUI application built using the Tkinter library in Python.
The application allows users to look up word meanings in an online dictionary.
It makes use of the PyDictionary library to access the online dictionary and retrieve the meanings of words.

"""

# Import Required Libraries
from tkinter import *
from PyDictionary import PyDictionary

# Create instances and objects
dictionary = PyDictionary()
win = Tk()

# Define the size of the window
win.geometry("700x400")

win.title("Python Dictionary")


# Define Helper Function to use the other attributes of PyDictionary Class
def dict():
    meaning.config(text=dictionary.meaning(word.get())['Noun'][0])


# Define Labels and Buttons
Label(win, text="Dictionary", font=("Times New Roman", 20)).pack(pady=20)

# Frame 1
frame = Frame(win)
Label(frame, text="Type any Word ", font=("Poppins bold", 15)).pack(side=LEFT)
word = Entry(frame, font=("Times New Roman", 15))
word.pack()
frame.pack(pady=10)
# Frame 2
frame1 = Frame(win)
Label(frame1, text="Meaning:", font=("Aerial", 18)).pack(side=LEFT)
meaning = Label(frame1, text="", font=("Poppins", 15), width=30)
meaning.pack()
frame1.pack(pady=10)

Button(win, text="Find", font=("Poppins bold", 15), command=dict).pack()

# Execute Tkinter
win.mainloop()

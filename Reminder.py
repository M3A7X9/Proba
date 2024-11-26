from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import pygame
import time


window = Tk()
window.title("Напоминание")

label = Label(text="Напоминание")
label.pack(paddy=10)
set_button = Button(text="Установить напоминание", command=set)
set_button.pack()

window.mainloop()
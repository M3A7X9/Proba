from tkinter import *
from tkinter import simpledialog as sd
from tkinter import messagebox as mb
import datetime
import pygame
import time


t = None

def set():
    global t
    rem = sd.askstring("Время напоминания", "Введите время в формате ЧЧ:ММ (24-часовой формат)")
    if rem:
        try:
            hour = int(rem.split(":")[0])
            minute = int(rem.split(":")[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=minute)
            print(dt)
            t = dt.timestamp()
            print(t)
            label.config(text=f"Напоминание установлено на: {hour:02}:{minute:02}")
        except ValueError:
            mb.showerror("Ошибка", "Неверный формат времени")


window = Tk()
window.title("Напоминание")

label = Label(text="Напоминание")
label.pack(pady=10)
set_button = Button(text="Установить напоминание", command=set)
set_button.pack()

window.mainloop()
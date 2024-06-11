import WINDOW_7
from tkinter import messagebox

def email_authentication():
    email_ = str(WINDOW_7.email.get())
    validos = 0
    for i in email_:
        if i == "@":
            validos += 1
        if validos == 1 and i == ".":
            validos += 1

    if validos < 2:
        messagebox.showerror("ERROR", "CORREO INVALIDO")


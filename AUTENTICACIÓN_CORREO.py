import WINDOW_5

from tkinter import messagebox

def email_authentication():
    email_ = str(WINDOW_5.email.get())
    if " " in email_:
        messagebox.showerror("ERROR", "CORREO INVALIDO")
    if email_.count("@") != 1:
        messagebox.showerror("ERROR", "CORREO INVALIDO")
    if email_.count(".") > 1:
        messagebox.showerror("ERROR", "CORREO INVALIDO")
    else:
        WINDOW_5.switch_to_root8()


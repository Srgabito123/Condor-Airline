from tkinter import *
import customtkinter as ctk

root = ctk.CTk()
root.title("CONDOR")
root._set_appearance_mode("light")
root.geometry("1000x600")
root.resizable(0, 0)
root.config(bg = "light pink")
root.iconbitmap("logo.ico")

#---------------------------FONTS---------------------------

font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")

#---------------------------FRAMES---------------------------

frame_principal = ctk.CTkFrame(master = root,
                        width = 1000,
                        height = 600,
                        corner_radius = 10,
                        fg_color = "light pink",
                        border_color = "white",
                        border_width = 2,
                        bg_color = "transparent"
                        )

frame_1 = ctk.CTkFrame(master = frame_principal,
                        width = 900,
                        height = 400,
                        corner_radius = 0,
                        fg_color = "white",
                        border_color = "white",
                        border_width = 2,
                        bg_color = "transparent"
                        )

frame_pase = ctk.CTkFrame(master = frame_1,
                        width = 1000,
                        height = 70,
                        corner_radius = 0,
                        fg_color = "light blue",
                        border_color = "white",
                        border_width = 1.5,
                        )

frame_cheap = ctk.CTkFrame(master = frame_1,
                        width = 250,
                        height = 400,
                        corner_radius = 0,
                        fg_color = "beige",
                        border_color = "white",
                        border_width = 1.5,
                        )


#------------------------L A B E L S------------------------



#------------------------positioning------------------------
frame_principal.place(relx=0.5, rely=0.5, anchor="center")
frame_1.place(relx=0.5, rely=0.5, anchor="center")
frame_pase.place(relx=0.5, rely=0.09, anchor="center")
frame_cheap.place(relx=0.09, rely=0.5, anchor="center")

root.mainloop()
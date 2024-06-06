from tkinter import *
import customtkinter as ctk
from PIL import Image
root = ctk.CTk()
# screen_width = root.winfo_screenwidth()
# screen_height = root.winfo_screenheight()
# window_width = 1000
# window_height = 600
# center_x = int(screen_width / 2 - window_width / 2)
# center_y = int(screen_height / 2 - window_height / 2)
# root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root.title("CONDOR")
root.geometry("1000x600")
root._set_appearance_mode("light")
root.resizable(0, 0)
root.config(bg = "#d7bb9f")
#-------------------------fonts-------------------------
font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")
font_2 = ctk.CTkFont(family="Cooper Black", size=12)
#-------------------------Frames-------------------------
principal_frame = ctk.CTkFrame(master = root,
                        width = 1000,
                        height = 600,
                        corner_radius = 10,
                        fg_color = "#d7bb9f",
                        border_color = "white",
                        border_width = 2
                        ).place(relx = 0.5, rely = 0.5, anchor = CENTER)

#-------------------------Labels-------------------------
welcome_text = ctk.CTkLabel(master = principal_frame,
                        text = "Bienvenido a Condor Airlines",
                        text_color= "black",
                        corner_radius=20,
                        font = (font_1, 30),
                        fg_color = "beige",
                        bg_color= "#d7bb9f"
                        ).place(relx = 0.5, rely = 0.1, anchor = CENTER)
decision_text = ctk.CTkLabel(master = principal_frame,
                        text = "¿Qué quieres hacer hoy?",
                        text_color= "black",
                        corner_radius=20,
                        font = (font_1, 20),
                        fg_color = "beige",
                        bg_color= "#d7bb9f"
                        ).place(relx = 0.5, rely = 0.65, anchor = CENTER)
#-------------------------Images-------------------------
image_1 = ctk.CTkImage(light_image=Image.open("logo.png"),
                       dark_image=Image.open("logo.png"),
                       size = (300, 300)
                       )
image1_label = ctk.CTkLabel(principal_frame, 
                            image=image_1, 
                            text = "", 
                            bg_color="#d7bb9f"
                            ).place(relx = 0.5, rely = 0.38, anchor = CENTER)                        
#-------------------------Buttons-------------------------
make_flights_button = ctk.CTkButton(master = principal_frame,
                        width = 240,
                        height = 70,
                        corner_radius = 32,
                        text = "Realizar un vuelo",
                        text_color= "white",
                        fg_color = "#a06553",
                        border_color = "black",
                        border_width = 2,
                        font = font_1,
                        bg_color= "#d7bb9f",
                        hover_color= "light blue"
                        ).place(relx = 0.25, rely = 0.8, anchor = CENTER)
make_flights_button = ctk.CTkButton(master = principal_frame,
                        width = 240,
                        height = 70,
                        corner_radius = 32,
                        text = "Realizar check-in",
                        text_color= "white",
                        fg_color = "#a06553",
                        border_color = "black",
                        border_width = 2,
                        font = font_1,
                        bg_color= "#d7bb9f",
                        hover_color= "light blue"
                        ).place(relx = 0.75, rely = 0.8, anchor = CENTER)
root.mainloop()
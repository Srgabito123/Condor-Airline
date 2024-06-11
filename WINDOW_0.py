import customtkinter as ctk
from PIL import Image

#--------------------------FUNCIONES-------------------------------------

def switch_to_root1():
    root0.destroy()
    import WINDOW_1
    WINDOW_1.initialize_root1()

def switch_to_root2():
    root0.destroy()
    import WINDOW_2
    WINDOW_2.initialize_root2()

#--------------------------VENTANA 0-------------------------------------
root0 = ctk.CTk()

root0.resizable(0, 0)

screen_width = root0.winfo_screenwidth()
screen_height = root0.winfo_screenheight()
window_width = 1000
window_height = 600

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root0.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root0.config(background="#d7bb9f")
root0.title("CONDOR-AIRLINES")
root0.iconbitmap("images/ICONO.ico")
#-------------------------fonts-------------------------

font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")
font_2 = ctk.CTkFont(family="Cooper Black", size=12)

#-------------------------Frames-------------------------

principal_frame = ctk.CTkFrame(master = root0,
                        width = 1000,
                        height = 600,
                        corner_radius = 10,
                        fg_color = "#d7bb9f",
                        border_color = "white",
                        border_width = 2
                        ).place(relx = 0.5, rely = 0.5, anchor = "center")

#-------------------------Labels-------------------------

welcome_text = ctk.CTkLabel(master = principal_frame,
                        text = "Bienvenido a Condor Airlines",
                        text_color= "black",
                        corner_radius=20,
                        font = (font_1, 30),
                        fg_color = "beige",
                        bg_color= "#d7bb9f"
                        ).place(relx = 0.5, rely = 0.1, anchor = "center")

decision_text = ctk.CTkLabel(master = principal_frame,
                        text = "¿Qué quieres hacer hoy?",
                        text_color= "black",
                        corner_radius=20,
                        font = (font_1, 20),
                        fg_color = "beige",
                        bg_color= "#d7bb9f"
                        ).place(relx = 0.5, rely = 0.65, anchor = "center")

#-------------------------Images-------------------------

image_1 = ctk.CTkImage(light_image=Image.open("images/LOGO AEROLINEA.png"),
                       dark_image=Image.open("images/LOGO AEROLINEA.png"),
                       size = (300, 300)
                       )
image1_label = ctk.CTkLabel(principal_frame, 
                            image=image_1, 
                            text = "", 
                            bg_color="#d7bb9f"
                            ).place(relx = 0.5, rely = 0.38, anchor = "center")  
                      
#-------------------------Buttons-------------------------

make_flights_button = ctk.CTkButton(master = principal_frame,
                        width = 240,
                        height = 70,
                        corner_radius = 32,
                        text = "Realizar un vuelo",
                        text_color= "white",
                        fg_color = "#a06553",
                        border_color = "#a06553",
                        border_width = 2,
                        font = font_1,
                        bg_color= "#d7bb9f",
                        hover_color= "light blue",
                        command = switch_to_root2
                        ).place(relx = 0.25, rely = 0.8, anchor = "center")

make_checkin_button = ctk.CTkButton(master = principal_frame,
                        width = 240,
                        height = 70,
                        corner_radius = 32,
                        text = "Realizar check-in",
                        text_color= "white",
                        fg_color = "#a06553",
                        border_color = "#a06553",
                        border_width = 2,
                        font = font_1,
                        bg_color= "#d7bb9f",
                        hover_color= "light blue",
                        command = switch_to_root1
                        ).place(relx = 0.75, rely = 0.8, anchor = "center")

root0.mainloop()
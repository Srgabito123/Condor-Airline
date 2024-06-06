import customtkinter as ctk
from PIL import Image
#------------------------------FUNCTIONS------------------------------------------

def check_in():
    text_box_1.delete(0, ctk.END)
    text_box_2.delete(0, ctk.END)
    
#-------------------------------VENTANA 1------------------------------------------

root1 = ctk.CTk()
root1.resizable(0, 0)

screen_width = root1.winfo_screenwidth()
screen_height = root1.winfo_screenheight()
window_width = 1000
window_height = 600

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root1.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
root1.config(background="#d7bb9f")
root1.title("Mapaula airline")
root1.iconbitmap("images/ICONO.ico")

#----------------------------------------FONTS-------------------------------------

font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")
font_2 = ctk.CTkFont(family="Cooper Black", size=12)

#-------------------------------------IMÁGEN--------------------------------------

image_1 = ctk.CTkImage(light_image=Image.open("images/LOGO AEROLINEA.png"),
                       dark_image=Image.open("images/LOGO AEROLINEA.png"),
                       size = (340, 340)
                       )

image1_label = ctk.CTkLabel(root1, 
                            image=image_1, 
                            text = "", 
                            bg_color="#d7bb9f"
                            )

#------------------------------------TÍTULOS----------------------------------------

title_1 = ctk.CTkLabel(root1, 
                       text="Código", 
                       width=150, 
                       height=40, 
                       font=("Helvetica", 18, "bold"),
                       text_color="brown",
                       bg_color="#d7bb9f",
                       fg_color="beige",
                       corner_radius=10
                       )

title_2 = ctk.CTkLabel(root1, 
                       text="Apellido", 
                       width=150, 
                       height=40, 
                       font=("Helvetica", 18, "bold"),
                       text_color="brown",
                       bg_color="#d7bb9f",
                       fg_color="beige",
                       corner_radius=10
                       )

#------------------------------------CAJAS DE TEXTO----------------------------------------

text_box_1 = ctk.CTkEntry(root1, 
                        width=250, 
                        height=50, 
                        bg_color="#d7bb9f", 
                        fg_color="beige",
                        font = font_1,
                        border_width=3,
                        border_color="#a06553"
                        )

text_box_2 = ctk.CTkEntry(root1, 
                        width=250, 
                        height=50,
                        font = font_1, 
                        bg_color="#d7bb9f",
                        fg_color="beige",
                        border_width=3,
                        border_color="#a06553"
                        )

#------------------------------------BOTON----------------------------------------

button_1 = ctk.CTkButton(root1, 
                        text="Realizar Check-In",
                        text_color="white", 
                        width=200, 
                        height=50,
                        font=("Helvetica", 18, "bold"),
                        bg_color="#d7bb9f",
                        fg_color="#a06553",
                        cursor="hand2",
                        hover_color="lightblue",
                        border_width=3,
                        border_color="#a06553",
                        corner_radius=10,
                        command = check_in
                        )

#------------------------------------POSICIONAMIENTO----------------------------------------

image1_label.place(x=330, y=1)
title_1.place(x=250, y=300)
title_2.place(x=600, y=300)
text_box_1.place(x=200, y=350)
text_box_2.place(x=550, y=350)
button_1.place(x=400, y=440)

root1.mainloop()
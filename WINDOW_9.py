import customtkinter as ctk
from PIL import Image
import WINDOW_5
from tkinter import messagebox as mb

def initialize_root9():

    #------------------------------FUNCTIONS------------------------------------------

    def check_in():

        code = WINDOW_5.code
        last_name = WINDOW_5.last_name_

        entry_code = text_box_1.get()
        entry_last_name = text_box_2.get()
        entry_last_name = entry_last_name.upper()

        if entry_code != code and entry_last_name != last_name:
            mb.showerror("Error", "Código y apellido incorrectos")
            return
        if entry_code == code and entry_last_name == last_name:
            mb.showinfo("Check-In", "Check-In realizado con éxito")
            root9.destroy()
        if entry_code != code:
            mb.showerror("Error", "Código incorrecto")
            return
        if entry_last_name != last_name:
            mb.showerror("Error", "Apellido incorrecto")
            return
        
    #-------------------------------VARIABLES-----------------------------------------

    

    #-------------------------------WINDOW 1------------------------------------------

    root9 = ctk.CTk()
    root9.resizable(0, 0)

    screen_width = root9.winfo_screenwidth()
    screen_height = root9.winfo_screenheight()
    window_width = 1000
    window_height = 600

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root9.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root9.config(background="#d7bb9f")
    root9.title("CONDOR-AIRLINES")
    root9.iconbitmap("images/ICONO.ico")

    #----------------------------------------FONTS-------------------------------------

    font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")
    font_2 = ctk.CTkFont(family="Cooper Black", size=12)

    #-------------------------------------IMAGE--------------------------------------
    
    image_1 = ctk.CTkImage(light_image=Image.open("images/LOGO AEROLINEA.png"),
                        dark_image=Image.open("images/LOGO AEROLINEA.png"),
                        size = (340, 340)
                        )

    image1_label = ctk.CTkLabel(root9, 
                                image=image_1, 
                                text = "", 
                                bg_color="#d7bb9f"
                                )

    #------------------------------------LABELS----------------------------------------

    title_1 = ctk.CTkLabel(root9, 
                        text="Código", 
                        width=150, 
                        height=40, 
                        font=("Helvetica", 18, "bold"),
                        text_color="brown",
                        bg_color="#d7bb9f",
                        fg_color="beige",
                        corner_radius=10
                        )

    title_2 = ctk.CTkLabel(root9, 
                        text="Apellido", 
                        width=150, 
                        height=40, 
                        font=("Helvetica", 18, "bold"),
                        text_color="brown",
                        bg_color="#d7bb9f",
                        fg_color="beige",
                        corner_radius=10
                        )

    #------------------------------------TEXT BOXES----------------------------------------

    text_box_1 = ctk.CTkEntry(root9, 
                            width=250, 
                            height=50, 
                            bg_color="#d7bb9f", 
                            fg_color="beige",
                            font = font_1,
                            border_width=3,
                            border_color="#a06553"
                            )

    text_box_2 = ctk.CTkEntry(root9, 
                            width=250, 
                            height=50,
                            font = font_1, 
                            bg_color="#d7bb9f",
                            fg_color="beige",
                            border_width=3,
                            border_color="#a06553"
                            )

    #------------------------------------BOTON----------------------------------------

    button_1 = ctk.CTkButton(root9, 
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

    root9.mainloop()
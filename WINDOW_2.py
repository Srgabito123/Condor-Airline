import customtkinter as ctk
from PIL import Image, ImageTk
from tkinter import messagebox as mb
import CONSTANTES

def initialize_root2():

    #--------------------------------VENTANA 2---------------------------------------

    root2 = ctk.CTk()
    root2.resizable(0, 0)

    screen_width = root2.winfo_screenwidth()
    screen_height = root2.winfo_screenheight()
    window_width = 1000
    window_height = 600

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root2.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root2.config(background="#d7bb9f")
    root2.title("CONDOR-AIRLINES")
    root2.iconbitmap("images/ICONO.ico")
    
    #-------------------------VARIBLES OPTION MENUS----------------------------------

    roundtrip_options = ["Solo ida"] #Valores
    roundtrip_value = ctk.StringVar() #Tipo de variable
    roundtrip_value.set(roundtrip_options[0]) #Valor por defecto

    origin_value = ctk.StringVar() 
    destiny_value = ctk.StringVar() 
    dates_value = ctk.StringVar() 
    amountpeople_value = ctk.IntVar()

    #--------------------------------FUNCIONES---------------------------------------

    def switch_to_root4_5():

        if origin_value.get() == "" or destiny_value.get() == "" or dates_value.get() == "" or amountpeople_value.get() == "":
            mb.showwarning("Error", "Por favor, llene todos los campos")
            return
        if origin_value.get() == destiny_value.get():
            mb.showwarning("Error", "El origen y el destino no pueden ser iguales")
            return
        else:
            root2.destroy()
            import WINDOW_4_5
            WINDOW_4_5.initialize_root4_5(origin_value.get(),
                                            destiny_value.get(),
                                            dates_value.get())


    #----------------------------------FRAMES----------------------------------------

    frame_1 = ctk.CTkFrame(root2,
                        bg_color="#d7bb9f", 
                        fg_color = "#d7bb9f", 
                        width = 860, 
                        height = 400, 
                        border_color = "beige", 
                        border_width = 4,
                        corner_radius = 15
                        )

    roundtrip_frame = ctk.CTkFrame(root2, 
                        fg_color = "#d7bb9f",
                        bg_color = "#d7bb9f", 
                        width = 257, 
                        height = 57, 
                        border_color = "#a06553", 
                        border_width = 3,
                        corner_radius = 3
                        )

    amountpeople_frame = ctk.CTkFrame(root2, 
                        fg_color = "#d7bb9f",
                        bg_color = "#d7bb9f", 
                        width = 103, 
                        height = 56, 
                        border_color = "#a06553", 
                        border_width = 3,
                        corner_radius = 3
                        )

    origin_frame = ctk.CTkFrame(root2, 
                        fg_color = "#d7bb9f",
                        bg_color = "#d7bb9f", 
                        width = 226, 
                        height = 73, 
                        border_color = "#a06553", 
                        border_width = 3,
                        corner_radius = 3
                        )

    destination_frame = ctk.CTkFrame(root2, 
                        fg_color = "#d7bb9f",
                        bg_color = "#d7bb9f", 
                        width = 226, 
                        height = 73, 
                        border_color = "#a06553", 
                        border_width = 3,
                        corner_radius = 0
                        )

    dateflight_frame = ctk.CTkFrame(root2, 
                        fg_color = "#d7bb9f",
                        bg_color = "#d7bb9f", 
                        width = 226, 
                        height = 73, 
                        border_color = "#a06553", 
                        border_width = 3,
                        corner_radius = 0
                        )

    image_frame = ctk.CTkFrame(root2, 
                            fg_color="beige",
                            bg_color="#d7bb9f", 
                            corner_radius = 2,
                            border_width = 3, 
                            border_color = "beige"
                            )

    divisor_line = ctk.CTkFrame(root2, 
                        fg_color = "#d7bb9f", 
                        width = 860, 
                        height = 12,
                        corner_radius = 0,
                        border_color = "beige", 
                        border_width = 4
                        )

    #--------------------------------------IMÁGEN----------------------------------------

    icon_image = Image.open("D:/GABO/2024/UNIVERSIDAD/SEMESTRE 1/FUNDAMENTOS DE PROGRAMACIÓN IMPERATIVA/PROYECTO FINAL/Repositorio/PERSONAS.png")
    icon_image = icon_image.resize((20, 20), Image.Resampling.LANCZOS)
    icon_photo = ImageTk.PhotoImage(icon_image)

    #----------------------------------OPTION MENUS----------------------------------------

    roundtrip_optionmenu = ctk.CTkOptionMenu(root2, 
                                            variable = roundtrip_value, 
                                            values = roundtrip_options,
                                            width = 250,
                                            height=50,
                                            font=("Poppins", 16),
                                            text_color = "brown",
                                            bg_color = "#a06553",
                                            fg_color = "beige",
                                            cursor = "hand2",
                                            button_color = "beige",
                                            button_hover_color = "#a06553",
                                            dropdown_font = ("Poppins", 16),
                                            dropdown_text_color = "brown",
                                            dropdown_hover_color = "#a06553",
                                            dropdown_fg_color = "beige",
                                            corner_radius = 2
                                            )

    origin_optionmenu = ctk.CTkOptionMenu(root2, 
                                            variable = origin_value, 
                                            values = CONSTANTES.origin_city,
                                            width = 220,
                                            height=50,
                                            font=("Poppins", 16),
                                            text_color = "brown",
                                            bg_color = "beige",
                                            fg_color = "beige",
                                            cursor = "hand2",
                                            button_color = "beige",
                                            button_hover_color = "#a06553",
                                            dropdown_font = ("Poppins", 16),
                                            dropdown_text_color = "brown",
                                            dropdown_hover_color = "#a06553",
                                            dropdown_fg_color = "beige",
                                            corner_radius = 2
                                            )

    destination_optionmenu = ctk.CTkOptionMenu(root2, 
                                            variable = destiny_value, 
                                            values = CONSTANTES.destiny_city,
                                            width = 220,
                                            height=50,
                                            font=("Poppins", 16),
                                            text_color = "brown",
                                            bg_color = "beige",
                                            fg_color = "beige",
                                            cursor = "hand2",
                                            button_color = "beige",
                                            button_hover_color = "#a06553",
                                            dropdown_font = ("Poppins", 16),
                                            dropdown_text_color = "brown",
                                            dropdown_hover_color = "#a06553",
                                            dropdown_fg_color = "beige",
                                            corner_radius = 2
                                            )

    dateflight_optionmenu = ctk.CTkOptionMenu(root2, 
                                            variable = dates_value, 
                                            values = CONSTANTES.departure_date,
                                            width = 220,
                                            height=50,
                                            font=("Poppins", 16),
                                            text_color = "brown",
                                            bg_color = "beige",
                                            fg_color = "beige",
                                            cursor = "hand2",
                                            button_color = "beige",
                                            button_hover_color = "#a06553",
                                            dropdown_font = ("Poppins", 16),
                                            dropdown_text_color = "brown",
                                            dropdown_hover_color = "#a06553",
                                            dropdown_fg_color = "beige",
                                            corner_radius = 2
                                            )

    amountpeople_optionmenu = ctk.CTkOptionMenu(image_frame, 
                                            variable = amountpeople_value, 
                                            values = ["1"],
                                            width = 10,
                                            height=50,
                                            font=("Poppins", 16),
                                            text_color = "brown",
                                            bg_color = "beige",
                                            fg_color = "beige",
                                            cursor = "hand2",
                                            button_color = "beige",
                                            button_hover_color = "#a06553",
                                            dropdown_font = ("Poppins", 16),
                                            dropdown_text_color = "brown",
                                            dropdown_hover_color = "#a06553",
                                            dropdown_fg_color = "beige",
                                            corner_radius = 2
                                            )

    #-----------------------------------LABELS----------------------------------------

    icon_people_label = ctk.CTkLabel(image_frame, 
                                    image=icon_photo, 
                                    text="", 
                                    fg_color="beige",
                                    height = 30
                                    )

    origin_label = ctk.CTkLabel(root2, 
                                text = "Origen",
                                width = 220,
                                height = 16,
                                font=("Poppins", 12), 
                                text_color = "brown",
                                fg_color = "beige", 
                                bg_color = "#d7bb9f",
                                anchor = "w"
                                )

    destination_label = ctk.CTkLabel(root2, 
                                text = "Destino",
                                width = 220,
                                height = 16,
                                font=("Poppins", 12), 
                                text_color = "brown",
                                fg_color = "beige", 
                                bg_color = "#d7bb9f",
                                anchor = "w"
                                )

    dateflight_label = ctk.CTkLabel(root2, 
                                text = "Fecha ida",
                                width = 220,
                                height = 16,
                                font=("Poppins", 12), 
                                text_color = "brown",
                                fg_color = "beige", 
                                bg_color = "#d7bb9f",
                                anchor = "w"
                                )

    #------------------------------------BOTON----------------------------------------

    button_search = ctk.CTkButton(root2, 
                        text="Buscar",
                        text_color="white", 
                        width=150, 
                        height=40,
                        font=("Poppins", 16, "bold"),
                        bg_color="#d7bb9f",
                        fg_color="#a06553",
                        cursor="hand2",
                        hover_color="lightblue",
                        command = switch_to_root4_5)

    #----------------------------------POSICIONAMIENTO----------------------------------------

    frame_1.place(x = 70, y = 70)
    roundtrip_frame.place(x = 97, y = 105)
    amountpeople_frame.place(x = 777, y = 104.8)
    origin_frame.place(x = 97, y = 241)
    destination_frame.place(x = 320, y = 241)
    dateflight_frame.place(x = 647, y = 241)
    divisor_line.place(x = 70, y = 190)
    roundtrip_optionmenu.place(x = 100, y = 108)
    image_frame.place(x = 780, y = 108)
    amountpeople_optionmenu.grid(row=0, column=1, sticky="nsew", padx=(0, 5))
    icon_people_label.grid(row=0, column=0, sticky="nsew", padx=(5, 0))
    origin_label.place(x = 100, y = 244)
    destination_label.place(x = 323, y = 244)
    origin_optionmenu.place(x = 100, y = 260)
    destination_optionmenu.place(x = 323, y = 260)
    dateflight_optionmenu.place(x = 650, y = 260)
    dateflight_label.place(x = 650, y = 244)
    button_search.place(x=425, y=370)

    root2.mainloop()

if __name__ == "__main__":
    initialize_root2()
from tkinter import *
import customtkinter as ctk
import AUTENTICACIÓN_CORREO


def initialize_root7():
    root7 = ctk.CTk()
    root7.title("CONDOR-AIRLINE")
    root7._set_appearance_mode("light")
    root7.geometry("1000x600")
    root7.resizable(0, 0)
    root7.config(bg = "#d7bb9f")
    root7.iconbitmap("images/ICONO.ico")
    root = ctk.CTk()
    root.title("CONDOR")
    root._set_appearance_mode("light")
    root.geometry("1000x600")
    root.resizable(0, 0)
    root.config(bg = "light pink")
    # root.iconbitmap("logo.ico")

    #----------------------------VARIABLES OPTIPON MENUS-------------------------------

    gender_options = ["Masculino", "Femenino", "Otro"]
    value_genders = ctk.StringVar()
    value_genders.set(gender_options[0])

    id_types = ["C. de Ciudadanía (CC)", "C. de Extranjería (CE)",
                "Número de Identificación Tributario (NIT)", "Pasaporte"]
    value_id = ctk.StringVar()
    value_id.set(id_types[0])

    #-------------------------------------FONTS----------------------------------------

    font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")
    font_2 = ctk.CTkFont(family="Cooper Black", size=12)

    #-------------------------------------FRAMES----------------------------------------

    principal_frame = ctk.CTkFrame(root7,
                            width = 1000,
                            height = 600,
                            corner_radius = 10,
                            fg_color = "#d7bb9f",
                            border_color = "white",
                            border_width = 2
                            )

    make_flights_frame = ctk.CTkFrame(principal_frame,
                            width = 900,
                            height = 400,
                            corner_radius = 36,
                            fg_color = "beige",
                            border_color = "white",
                            border_width = 2
                            )

    frame_genders = ctk.CTkFrame(make_flights_frame,
                                width = 255,
                                height = 55,
                                corner_radius = 10,
                                fg_color = "beige",
                                border_color = "#a06553",
                                border_width = 2
                                )

    frame_type_id = ctk.CTkFrame(make_flights_frame,
                                width = 258,
                                height = 55,
                                corner_radius = 10,
                                fg_color = "beige",
                                border_color = "#a06553",
                                border_width = 2
                                )

    #-------------------------Labels-------------------------

    title_label = ctk.CTkLabel(make_flights_frame,
                            text = "Realizar un vuelo",
                            text_color= "black",
                            font = ("helvetica", 20, "bold"),
                            fg_color = "beige",
                            )

    #-------------------------entry--------------------------

    entry_first_name = ctk.CTkEntry(master = make_flights_frame,
                            width = 250,
                            height = 50,
                            corner_radius = 10,
                            text_color= "black",
                            fg_color = "white",
                            border_color = "#a06553",
                            border_width = 2,
                            font = font_1,
                            placeholder_text= "Primer Nombre",
                            )

    entry_last_name = ctk.CTkEntry(master = make_flights_frame,
                            width = 250,
                            height = 50,
                            corner_radius = 10,
                            text_color= "black",
                            fg_color = "white",
                            border_color = "#a06553",
                            border_width = 2,
                            font = font_1,
                            placeholder_text= "Primer Apellido"
                            )

    genero = ctk.CTkOptionMenu(make_flights_frame, 
                            variable= value_genders,
                            values = gender_options,
                            width = 250, 
                            height = 50, 
                            corner_radius = 10, 
                            text_color= "black", 
                            fg_color = "white",
                            bg_color= "#a06553", 
                            font = font_1, 
                            button_color= "#a06553",
                            button_hover_color= "light blue",
                            dropdown_fg_color= "white",
                            dropdown_hover_color= "light pink",
                            dropdown_text_color= "black",
                            )

    type_identification = ctk.CTkOptionMenu(make_flights_frame, 
                            values = id_types,
                            variable= value_id,
                            width = 250, 
                            height = 50, 
                            corner_radius = 10, 
                            text_color= "black", 
                            fg_color = "white", 
                            bg_color= "#a06553",
                            font = font_1, 
                            button_color= "#a06553",
                            button_hover_color= "light blue",
                            dropdown_fg_color= "white",
                            dropdown_hover_color= "light pink",
                            dropdown_text_color= "black",
                            )

    identification = ctk.CTkEntry(master = make_flights_frame,
                            width = 250,
                            height = 50,
                            corner_radius = 10,
                            text_color= "black",
                            fg_color = "white",
                            border_color = "#a06553",
                            border_width = 2,
                            font = font_1,
                            placeholder_text= "Identificación",
                            )

    nationality = ctk.CTkEntry(master = make_flights_frame,
                            width = 250,
                            height = 50,
                            corner_radius = 10,
                            text_color= "black",
                            fg_color = "white",
                            border_color = "#a06553",
                            border_width = 2,
                            font = font_1,
                            placeholder_text= "Nacionalidad",
                            )

    phone = ctk.CTkEntry(master = make_flights_frame,
                            width = 250,
                            height = 50,
                            corner_radius = 10,
                            text_color= "black",
                            fg_color = "white",
                            border_color = "#a06553",
                            border_width = 2,
                            font = font_1,
                            placeholder_text= "Teléfono",
                            )

    email = ctk.CTkEntry(master = make_flights_frame,
                            width = 250,
                            height = 50,
                            corner_radius = 10,
                            text_color= "black",
                            fg_color = "white",
                            border_color = "#a06553",
                            border_width = 2,
                            font = font_1,
                            placeholder_text= "Correo Electrónico",
                            )

    #-------------------------BUTTONS-------------------------

    button_make_flight = ctk.CTkButton(master = make_flights_frame,
                            text = "Seleccionar Vuelo",
                            width = 250,
                            height = 50,
                            corner_radius = 10,
                            fg_color = "#a06553",
                            font = font_1,
                            border_color = "#a06553",
                            border_width = 2,
                            hover_color= "light blue",
                            text_color= "white"
                            )

    continue_flight = ctk.CTkButton(master = make_flights_frame,
                            text = "Continuar",
                            width = 250,
                            height = 50,
                            corner_radius = 10,
                            fg_color = "#a06553",
                            font = font_1,
                            border_color = "light pink",
                            border_width = 2,
                            hover_color= "light blue",
                            text_color= "white",
                            command = AUTENTICACIÓN_CORREO.email_authentication
                            )

    #-------------------------POSICIONAMIENTO-------------------------

    principal_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
    make_flights_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
    title_label.place(relx = 0.15, rely = 0.14, anchor = "center")
    entry_first_name.place(relx = 0.5, rely = 0.3, anchor = "center")
    entry_last_name.place(relx = 0.8, rely = 0.3, anchor = "center")
    genero.place(relx = 0.2, rely = 0.3, anchor = "center")
    frame_genders.place(relx = 0.2, rely = 0.3, anchor = "center")
    identification.place(relx = 0.5, rely = 0.5, anchor = "center")
    nationality.place(relx = 0.8, rely = 0.5, anchor = "center")
    type_identification.place(relx = 0.2, rely = 0.5, anchor = "center")
    frame_type_id.place(relx = 0.2, rely = 0.5, anchor = "center")
    phone.place(relx = 0.5, rely = 0.7, anchor = "center")
    email.place(relx = 0.8, rely = 0.7, anchor = "center")
    button_make_flight.place(relx = 0.2, rely = 0.7, anchor = "center")
    continue_flight.place(relx = 0.5, rely = 0.9, anchor = "center")

    root7.mainloop()


from tkinter import *
import customtkinter as ctk
import WINDOW_7 
import WINDOW_6

def initialize_root9(): 
    
    root9 = ctk.CTk()
    root9.title("CONDOR-AIRLINES")
    root9._set_appearance_mode("light")
    root9.geometry("1000x600")
    root9.resizable(0, 0)
    root9.config(bg = "light pink")
    

    #---------------------------FONTS---------------------------

    font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")
    font_2 = ctk.CTkFont(family="Cooper Black", size=12)
    name_ = WINDOW_7.first_name
    last_ = WINDOW_7.last_name
    

    #---------------------------FRAMES---------------------------

    frame_principal = ctk.CTkFrame(master = root9,
                            width = 1000,
                            height = 600,
                            corner_radius = 10,
                            fg_color = "#d7bb9f",
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
                            fg_color = "#a06553",
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

    label_aerolinea = ctk.CTkLabel(master = frame_cheap,
                            text = """CONDOR 

    AIRLINES""",
                            font = (font_1, 25),
                            text_color = "black",
                            )

    pase_abordaje = ctk.CTkLabel(master = frame_pase,
                            text = "PASE DE ABORDAJE",
                            font = (font_1, 20),
                            text_color = "black",
                            )

    nombre_pasajero = ctk.CTkLabel(master = frame_1,
                            text = "Nombre del pasajero:",
                            font = (font_1, 18),
                            text_color = "black",
                            )

    nombre = ctk.CTkLabel(master = frame_1,
                            text = f"{name_} {last_}",
                            font = (font_1, 18),
                            text_color = "black",
                            )

    origen_pasajero = ctk.CTkLabel(master = frame_1,
                            text = "Origen:",
                            font = (font_1, 18),
                            text_color = "black",
                            )

    origen = ctk.CTkLabel(master = frame_1,
                            text = WINDOW_6.exit_city_f,
                            font = (font_1, 18),
                            text_color = "black",
                            )

    destino_pasajero = ctk.CTkLabel(master = frame_1,
                            text = "Destino:",
                            font = (font_1, 18),
                            text_color = "black",
                            )

    destino = ctk.CTkLabel(master = frame_1,
                            text = WINDOW_6.coming_city_f,
                            font = (font_1, 18),
                            text_color = "black",
                            )

    fecha_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Fecha:",
                            font = (font_1, 18),
                            text_color = "black",
                            )

    fecha = ctk.CTkLabel(master = frame_1,
                            text = WINDOW_6.flight_date_f,
                            font = (font_1, 18),
                            text_color = "black",
                            )

    hora_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Hora:",
                            font = (font_1, 18),
                            text_color = "black",
                            )

    hora = ctk.CTkLabel(master = frame_1,
                            text = WINDOW_6.takeoff_hour_f,
                            font = (font_1, 18),
                            text_color = "black",
                            )

    numero_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Vuelo:",
                            font = (font_1, 22),
                            text_color = "black",
                            )

    vuelo = ctk.CTkLabel(master = frame_1,
                            text = WINDOW_6.flight_code_f,
                            font = (font_1, 22),
                            text_color = "black",
                            )

    codigo_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Código Check-in:",
                            font = (font_1, 22),
                            text_color = "black",
                            )
    
    checkin = ctk.CTkLabel(master = frame_1,
                            text = "123456",
                            font = (font_1, 22),
                            text_color = "black",
                            )

    #------------------------positioning------------------------


    frame_principal.place(relx=0.5, rely=0.5, anchor="center")
    frame_1.place(relx=0.5, rely=0.5, anchor="center")
    frame_pase.place(relx=0.5, rely=0.09, anchor="center")
    frame_cheap.place(relx=0.09, rely=0.5, anchor="center")
    label_aerolinea.place(relx=0.55, rely=0.5, anchor="center")
    pase_abordaje.place(relx=0.5, rely=0.5, anchor="center")
    nombre_pasajero.place(relx=0.37, rely=0.27, anchor="center")
    nombre.place(relx=0.37, rely=0.38, anchor="center")
    origen_pasajero.place(relx=0.37, rely=0.58, anchor="center")
    origen.place(relx=0.37, rely=0.68, anchor="center")
    destino_pasajero.place(relx=0.76, rely=0.58, anchor="center")
    destino.place(relx=0.76, rely=0.68, anchor="center")
    fecha_vuelo.place(relx=0.76, rely=0.27, anchor="center")
    fecha.place(relx=0.85, rely=0.27, anchor="center")
    hora_vuelo.place(relx=0.76, rely=0.36, anchor="center")
    hora.place(relx=0.85, rely=0.36, anchor="center")
    numero_vuelo.place(relx=0.3, rely=0.9, anchor="center")
    vuelo.place(relx=0.43, rely=0.9, anchor="center")
    codigo_vuelo.place(relx=0.7, rely=0.9, anchor="center")
    checkin.place(relx=0.89, rely=0.9, anchor="center")



    root9.mainloop()
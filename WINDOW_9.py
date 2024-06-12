from tkinter import *
import customtkinter as ctk
from WINDOW_7 import entry_first_name, entry_last_name

def initialize_root9(): 
    global entry_first_name, entry_first_name
    root9 = ctk.CTk()
    root9.title("CONDOR-AIRLINES")
    root9._set_appearance_mode("light")
    root9.geometry("1000x600")
    root9.resizable(0, 0)
    root9.config(bg = "light pink")
    

    #---------------------------FONTS---------------------------

    font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")
    font_2 = ctk.CTkFont(family="Cooper Black", size=12)


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
                            font = (font_2, 18),
                            text_color = "black",
                            )

    nombre = ctk.CTkLabel(master = frame_1,
                            text = f"""{entry_firts_name.get()} {entry_last_name.get()}""",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    origen_pasajero = ctk.CTkLabel(master = frame_1,
                            text = "Origen:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    origen = ctk.CTkLabel(master = frame_1,
                            text = origen,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    destino_pasajero = ctk.CTkLabel(master = frame_1,
                            text = "Destino:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    destino = ctk.CTkLabel(master = frame_1,
                            text = destino,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    fecha_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Fecha:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    fecha = ctk.CTkLabel(master = frame_1,
                            text = fecha,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    hora_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Hora:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    hora = ctk.CTkLabel(master = frame_1,
                            text = hora,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    numero_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Vuelo:",
                            font = (font_2, 27),
                            text_color = "black",
                            )

    vuelo = ctk.CTkLabel(master = frame_1,
                            text = vuelo,
                            font = (font_2, 25),
                            text_color = "black",
                            )
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
                            font = (font_2, 18),
                            text_color = "black",
                            )

    nombre = ctk.CTkLabel(master = frame_1,
                            text = nombre,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    origen_pasajero = ctk.CTkLabel(master = frame_1,
                            text = "Origen:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    origen = ctk.CTkLabel(master = frame_1,
                            text = origen,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    destino_pasajero = ctk.CTkLabel(master = frame_1,
                            text = "Destino:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    destino = ctk.CTkLabel(master = frame_1,
                            text = destino,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    fecha_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Fecha:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    fecha = ctk.CTkLabel(master = frame_1,
                            text = fecha,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    hora_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Hora:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    hora = ctk.CTkLabel(master = frame_1,
                            text = hora,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    numero_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Vuelo:",
                            font = (font_2, 27),
                            text_color = "black",
                            )

    vuelo = ctk.CTkLabel(master = frame_1,
                            text = vuelo,
                            font = (font_2, 25),
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
    numero_vuelo.place(relx=0.37, rely=0.9, anchor="center")
    vuelo.place(relx=0.48, rely=0.9, anchor="center")


    root9.mainloop()
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
    numero_vuelo.place(relx=0.37, rely=0.9, anchor="center")
    vuelo.place(relx=0.48, rely=0.9, anchor="center")


    root9.mainloop().CTkLabel(master = frame_pase,
                            text = "PASE DE ABORDAJE",
                            font = (font_1, 20),
                            text_color = "black",
                            )

    nombre_pasajero = ctk.CTkLabel(master = frame_1,
                            text = "Nombre del pasajero:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    nombre = ctk.CTkLabel(master = frame_1,
                            text = CONSTANTES.firts_name + " " + CONSTANTES.last_name,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    origen_pasajero = ctk.CTkLabel(master = frame_1,
                            text = "Origen:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    origen = ctk.CTkLabel(master = frame_1,
                            text = origen,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    destino_pasajero = ctk.CTkLabel(master = frame_1,
                            text = "Destino:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    destino = ctk.CTkLabel(master = frame_1,
                            text = destino,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    fecha_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Fecha:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    fecha = ctk.CTkLabel(master = frame_1,
                            text = fecha,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    hora_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Hora:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    hora = ctk.CTkLabel(master = frame_1,
                            text = hora,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    numero_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Vuelo:",
                            font = (font_2, 27),
                            text_color = "black",
                            )

    vuelo = ctk.CTkLabel(master = frame_1,
                            text = vuelo,
                            font = (font_2, 25),
                            text_color = "black",
                            )
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
                            font = (font_2, 18),
                            text_color = "black",
                            )

    nombre = ctk.CTkLabel(master = frame_1,
                            text = nombre,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    origen_pasajero = ctk.CTkLabel(master = frame_1,
                            text = "Origen:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    origen = ctk.CTkLabel(master = frame_1,
                            text = origen,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    destino_pasajero = ctk.CTkLabel(master = frame_1,
                            text = "Destino:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    destino = ctk.CTkLabel(master = frame_1,
                            text = destino,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    fecha_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Fecha:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    fecha = ctk.CTkLabel(master = frame_1,
                            text = fecha,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    hora_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Hora:",
                            font = (font_2, 18),
                            text_color = "black",
                            )

    hora = ctk.CTkLabel(master = frame_1,
                            text = hora,
                            font = (font_2, 18),
                            text_color = "black",
                            )

    numero_vuelo = ctk.CTkLabel(master = frame_1,
                            text = "Vuelo:",
                            font = (font_2, 27),
                            text_color = "black",
                            )

    vuelo = ctk.CTkLabel(master = frame_1,
                            text = vuelo,
                            font = (font_2, 25),
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
    numero_vuelo.place(relx=0.37, rely=0.9, anchor="center")
    vuelo.place(relx=0.48, rely=0.9, anchor="center")


    root9.mainloop()
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
    numero_vuelo.place(relx=0.37, rely=0.9, anchor="center")
    vuelo.place(relx=0.48, rely=0.9, anchor="center")


    root9.mainloop()
from tkinter import *
import customtkinter as ctk

root = ctk.CTk()
root.title("CONDOR")
root._set_appearance_mode("light")
root.geometry("1000x600")
root.resizable(0, 0)
root.config(bg = "#d7bb9f")
#root.iconbitmap("logo.ico")

#---------------------------FUNCTIONS---------------------------

def eleccion_vuelo():
    if frame_eleccion_vuelo.winfo_viewable():
        frame_eleccion_vuelo.place_forget()
    else:
        frame_eleccion_vuelo.place(relx = 0.49, rely = 0.6, anchor = "center")

def cerrar_ventana():
    frame_eleccion_vuelo.place_forget()

#---------------------------VARIABLES---------------------------
hora_llegada = "13:00"
hora_salida = "10:00"
lugar_salida = "Bogotá"
lugar_llegada = "Cartagena"
ida = f"Ida: {lugar_salida} - {lugar_llegada}"
precio = "2.000.000"
fecha = "2024-06-13"
flechita = "-------------------------------------->"
plata = """
1 artículo personal (bolso) 
(Debe caber debajo del asiento)

1 equipaje de mano (10 kg) 
(Desde $195.100 COP)

Equipaje de bodega (23 kg) 
(Desde $175.600 COP)

Asiento Economy 
(Aleatoria-clasificado Aluminio)

Cambios de vuelo (No es permitido)

Reembolso (No es permitido)"""

diamante = """
1 artículo personal (bolso) 
(Debe caber debajo del asiento)

1 equipaje de bodega (23 kg) 
Debe caber en el 
compartimiento superior

1 equipaje de mano (10 kg) 
(Entrega el equipaje en el counter)

Asiento Economy 
(Filas específicas disponibles
 de manera aleatoria)

Cambios de vuelo (No es permitido)

Reembolso (No es permitido)"""

premium = """
1 artículo personal (bolso) 
(Debe caber debajo del asiento)

1 equipaje de mano (10 kg) 
Debe caber en el 
compartimiento superior

1 equipaje de bodega (23 kg) 
(Entrega el equipaje en el counter)
Asiento Plus 
(Sujeto a disponibilidad
clasificado Premium)

Cambios de vuelo 
(Sin cargo por cambio, antes del vuelo)

Reembolso (No es permitido)"""

#---------------------------FONTS---------------------------

font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")

#---------------------------FRAMES---------------------------

frame_principal = ctk.CTkFrame(master = root,
                        width = 1000,
                        height = 600,
                        corner_radius = 10,
                        fg_color = "#d7bb9f",
                        border_color = "white",
                        border_width = 2,
                        bg_color = "transparent"
                        )

frame_vuelos = ctk.CTkScrollableFrame(master = frame_principal,
                        width = 930,
                        height = 400,
                        fg_color = "transparent",
                        corner_radius = 30,
                        scrollbar_button_color = "beige",
                        orientation = "vertical"
                        )

frame_eleccion_vuelo = ctk.CTkFrame(master = frame_principal,
                        width=940,
                        height=470, 
                        fg_color="white",
                        border_width=2,
                        border_color="beige",
                        corner_radius=32
                        )

#---------------------------BOTONES---------------------------

opcion1 = ctk.CTkButton(master = frame_vuelos,    
                        width = 890, 
                        height = 160, 
                        corner_radius = 50,
                        fg_color = "beige",
                        hover_color = "beige",
                        text = " ",
                        border_color= "black",
                        border_width= 1.5,
                        command=eleccion_vuelo
                        )

opcion2 = ctk.CTkButton(master = frame_vuelos, 
                        fg_color = "beige",  
                        width = 890, 
                        height = 160, 
                        corner_radius = 50,
                        bg_color = "#d7bb9f",
                        hover_color = "beige",
                        text = " ",
                        border_color= "black",
                        border_width= 1.5,
                        command=eleccion_vuelo
                        )

opcion3 = ctk.CTkButton(master = frame_vuelos,
                        fg_color = "beige",  
                        width = 890, 
                        height = 160, 
                        corner_radius = 50,
                        bg_color = "#d7bb9f",
                        hover_color = "beige",
                        text = " ",
                        border_color= "black",
                        border_width= 1.5,
                        command=eleccion_vuelo
                        )

opcion4 = ctk.CTkButton(master = frame_vuelos,
                        fg_color = "beige",  
                        width = 890, 
                        height = 160, 
                        corner_radius = 50,
                        bg_color = "#d7bb9f",
                        hover_color = "beige",
                        text = " ",
                        border_color= "black",
                        border_width= 1.5,
                        command=eleccion_vuelo
                        )

boton_dias1 = ctk.CTkButton(master = frame_principal,
                        text = f"Fecha: {fecha}",
                        font = (font_1, 13), 
                        text_color = "black",
                        width = 100, 
                        height = 50, 
                        corner_radius = 32,
                        border_color= "black",
                        border_width= 1.5, 
                        fg_color = "beige",  
                        hover_color = "light blue"
                        )

boton_dias2 = ctk.CTkButton(master = frame_principal,
                        text = f"Fecha: {fecha}",
                        font = (font_1, 13), 
                        text_color = "black",
                        width = 100, 
                        height = 50, 
                        corner_radius = 32,
                        border_color= "black",
                        border_width= 1.5,
                        fg_color = "beige",  
                        hover_color = "light blue"
                        )

boton_dias3 = ctk.CTkButton(master = frame_principal,
                        text = f"Fecha: {fecha}",
                        font = (font_1, 13), 
                        text_color = "black",
                        width = 100, 
                        height = 50, 
                        corner_radius = 32, 
                        border_color= "black",
                        border_width= 1.5,
                        fg_color = "beige",  
                        hover_color = "light blue"
                        )

boton_dias4 = ctk.CTkButton(master = frame_principal,
                        text = f"Fecha: {fecha}",
                        font = (font_1, 13), 
                        text_color = "black",
                        width = 100, 
                        height = 50, 
                        corner_radius = 32,
                        border_color= "black",
                        border_width= 1.5, 
                        fg_color = "beige",  
                        hover_color = "light blue"
                        )

boton_dias5 = ctk.CTkButton(master = frame_principal,
                        text = f"Fecha: {fecha}",
                        font = (font_1, 13), 
                        text_color = "black",
                        width = 100, 
                        height = 50, 
                        corner_radius = 32,
                        border_color= "black",
                        border_width= 1.5, 
                        fg_color = "beige",  
                        hover_color = "light blue"
                        )

mejor_precio = ctk.CTkButton(master = frame_principal,
                        text = "Mejor precio",
                        font = (font_1, 13),
                        text_color = "black",
                        width = 100,
                        height = 50,
                        corner_radius = 32,
                        border_color= "black",
                        border_width= 1.5,
                        fg_color = "beige",
                        hover_color = "light blue"
                        )

vuelo_directo = ctk.CTkButton(master = frame_principal, 
                        text = "Vuelos directos",
                        font = (font_1, 13),
                        text_color = "black", 
                        width = 100, 
                        height = 50, 
                        corner_radius = 32, 
                        border_color= "black",
                        border_width= 1.5,
                        fg_color = "beige", 
                        hover_color = "light blue"
                        )

plata_clase = ctk.CTkButton(master = frame_eleccion_vuelo,
                        width=285,
                        height=400, 
                        fg_color="beige",
                        border_width=2,
                        corner_radius=32,
                        hover_color= "beige",
                        text= ""
                        )

diamante_clase = ctk.CTkButton(master = frame_eleccion_vuelo,
                        width=285,
                        height=400, 
                        fg_color="beige",
                        hover_color= "beige",
                        border_width=2,
                        corner_radius=32
                        )

premium_clase = ctk.CTkButton(master = frame_eleccion_vuelo,
                        width=285,
                        height=400, 
                        fg_color="beige",
                        hover_color= "beige",
                        border_width=2,
                        corner_radius=32
                        )

seleccionar_plata = ctk.CTkButton(master = plata_clase,
                        width=230,
                        height=30, 
                        font = (font_1, 15),
                        fg_color="light pink",
                        hover_color= "light blue",
                        border_width=2,
                        corner_radius=36,
                        text_color="black",
                        text="Seleccionar"
                        )

seleccionar_diamante = ctk.CTkButton(master = diamante_clase,
                        width=230,
                        height=30, 
                        font = (font_1, 15),
                        fg_color="light pink",
                        hover_color= "light blue",
                        border_width=2,
                        corner_radius=36,
                        text_color="black",
                        text="Seleccionar"
                        )

seleccionar_premium = ctk.CTkButton(master = premium_clase,
                        width=230,
                        height=30, 
                        font = (font_1, 15),
                        fg_color="light pink",
                        hover_color= "light blue",
                        border_width=2,                    
                        corner_radius=36,
                        text_color="black",
                        text="Seleccionar"
                        )

cerrar_ventana = ctk.CTkButton(master = frame_eleccion_vuelo,
                        width=230,
                        height=30, 
                        font = (font_1, 15),
                        fg_color="light blue",
                        hover_color= "light pink",
                        border_width=2,
                        corner_radius=36,
                        text_color="black",
                        text="Cerrar",
                        command=cerrar_ventana
                        )

#---------------------------TEXTOS---------------------------

text_viaje = ctk.CTkLabel(master = frame_principal, 
                        text = ida, 
                        fg_color = "beige", 
                        width = 0.2, 
                        height = 0.065, 
                        text_color = "black", 
                        font = font_1, 
                        corner_radius = 10, 
                        bg_color = "#d7bb9f",
                        )

text_hora_salida = ctk.CTkLabel(master = opcion1, 
                        text = hora_salida,
                        fg_color = "transparent",
                        bg_color= "beige",
                        text_color = "black",
                        font = font_1,
                        width = 0.1,
                        height = 0.3
                        )

text_hora_llegada = ctk.CTkLabel(master = opcion1, 
                        text = hora_llegada,
                        fg_color = "beige",
                        text_color = "black",
                        font = font_1,
                        width = 0.1,
                        height = 0.3,
                        corner_radius = 10,
                        )

text_lugar_salida = ctk.CTkLabel(master = opcion1, 
                        text = lugar_salida,
                        fg_color = "Beige",
                        text_color = "black",
                        font = font_1,
                        width = 0.1,
                        height = 0.3,
                        corner_radius = 10,
                        )

text_lugar_llegada = ctk.CTkLabel(master = opcion1, 
                        text = lugar_llegada,
                        fg_color = "Beige",
                        text_color = "black",
                        font = font_1,
                        width = 0.1,
                        height = 0.3,
                        corner_radius = 10,
                        )

text_desde = ctk.CTkLabel(master = opcion1,
                        text = """DESDE:

                            COP $""",
                        fg_color = "transparent",
                        text_color = "black",
                        font = font_1,
                        width = 0.1,
                        height = 0.3,
                        corner_radius = 10,
                        )

text_precio = ctk.CTkLabel(master = opcion1,
                        text = precio,
                        fg_color = "beige",
                        text_color = "black",
                        font = font_1,
                        width = 0.1,
                        height = 0.3,
                        corner_radius = 10,
                        )

text_flechita = ctk.CTkLabel(master = opcion1,
                        text = flechita,
                        fg_color = "beige",
                        text_color = "black",
                        font = ("roboto", 20),
                        width = 0.3,
                        height = 0.3,
                        )

text_filtrar = ctk.CTkLabel(master = frame_principal,
                        text = "Filtrar por:",
                        fg_color = "transparent",
                        text_color = "black",
                        font = (font_1, 16),
                        width = 0.3,
                        height = 0.3,
                        bg_color = "transparent"
                        )

nombre_plata = ctk.CTkLabel(master = plata_clase,
                        text = "Plata",
                        fg_color = "transparent",
                        text_color = "black",
                        font = font_1,
                        width = 0.3,
                        height = 0.3
                        )

texto_plata = ctk.CTkLabel(master = plata_clase,
                        text = plata,
                        fg_color = "transparent",
                        bg_color= "transparent",
                        text_color = "black",
                        font = (font_1, 14),
                        width = 100,
                        height = 100
                        )

nombre_diamante = ctk.CTkLabel(master = diamante_clase,
                        text = "Diamante",
                        fg_color = "transparent",
                        text_color = "black",
                        font = font_1,
                        width = 0.3,
                        height = 0.3
                        )

texto_diamante = ctk.CTkLabel(master = diamante_clase,
                        text = diamante,
                        fg_color = "transparent",
                        text_color = "black",
                        bg_color= "transparent",
                        font = (font_1, 14),
                        width = 100,
                        height = 100,
                        )

nombre_premium = ctk.CTkLabel(master = premium_clase,
                        text = "Premium",
                        fg_color = "transparent",
                        text_color = "black",
                        font = font_1,
                        width = 0.3,
                        height = 0.3
                        )

texto_premium = ctk.CTkLabel(master = premium_clase,
                        text = premium,
                        fg_color = "transparent",
                        bg_color= "transparent",
                        text_color = "black",
                        font = (font_1, 14),
                        width = 100,
                        height = 100
                        )
                    
#---------------------------POSICIONAMIENTO-----------------------

frame_principal.place(relx = 0.5, rely = 0.5, anchor = "center")
frame_vuelos.place(relx = 0.5, rely = 0.59, anchor = "center")
frame_eleccion_vuelo.place_forget()
text_viaje.place(x = 6, y = 8, relwidth = 0.3, relheight = 0.065)
text_filtrar.place(x = 593, y = 8, relwidth = 0.08, relheight = 0.05)
plata_clase.place(relx=0.17, rely=0.03, anchor="n")
diamante_clase.place(relx=0.50, rely=0.03, anchor="n")
premium_clase.place(relx=0.83, rely=0.03, anchor="n")
nombre_plata.place(relx=0.5, rely=0.05, anchor="center")
texto_plata.place(relx=0.5, rely=0.42, anchor="center")
nombre_diamante.place(relx=0.5, rely=0.05, anchor="center")
texto_diamante.place(relx=0.5, rely=0.45, anchor="center")
nombre_premium.place(relx=0.5, rely=0.05, anchor="center")
texto_premium.place(relx=0.5, rely=0.45, anchor="center")
cerrar_ventana.place(relx=0.5, rely=0.93, anchor="center")  
mejor_precio.place(x = 686, y = 8, relwidth = 0.12, relheight = 0.05)
vuelo_directo.place(x = 825, y = 8, relwidth = 0.14, relheight = 0.05)
boton_dias1.place(x = 20, y = 76, relwidth = 0.16, relheight = 0.057)
boton_dias2.place(x = 220, y = 76, relwidth = 0.16, relheight = 0.057)
boton_dias3.place(x = 420, y = 76, relwidth = 0.16, relheight = 0.057)
boton_dias4.place(x = 620, y = 76, relwidth = 0.16, relheight = 0.057)
boton_dias5.place(x = 820, y = 76, relwidth = 0.16, relheight = 0.057)
opcion1.pack(padx=5, pady=10, expand= True, anchor = "center")
opcion2.pack(padx=5, pady=10, expand= True, anchor = "center")
opcion3.pack(padx=5, pady=10, expand= True, anchor = "center")
opcion4.pack(padx=5, pady=10, expand= True, anchor = "center")
text_hora_salida.place(relx = 0.1, rely = 0.4, anchor = "center")
text_lugar_salida.place(relx = 0.1, rely = 0.54, anchor = "center")
text_hora_llegada.place(relx = 0.5, rely = 0.4, anchor = "center")
text_lugar_llegada.place(relx = 0.5, rely = 0.54, anchor = "center")
text_desde.place(relx = 0.66, rely = 0.4, anchor = "center")
text_precio.place(relx = 0.83, rely = 0.53, anchor = "center")
text_flechita.place(relx = 0.3, rely = 0.45, anchor = "center")
seleccionar_plata.place(relx=0.5, rely=0.93, anchor="center")
seleccionar_diamante.place(relx=0.5, rely=0.93, anchor="center")
seleccionar_premium.place(relx=0.5, rely=0.93, anchor="center")
root.mainloop()
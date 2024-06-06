from tkinter import *
import customtkinter as ctk

root = ctk.CTk()
root.title("CONDOR")
root._set_appearance_mode("light")
root.geometry("1000x600")
root.resizable(0, 0)
root.config(bg = "light pink")
root.iconbitmap("logo.ico")

#-------------------------fonts-------------------------
font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")
font_2 = ctk.CTkFont(family="Cooper Black", size=12)
#-------------------------Frames-------------------------
principal_frame = ctk.CTkFrame(master = root,
                        width = 1000,
                        height = 600,
                        corner_radius = 10,
                        fg_color = "light pink",
                        border_color = "white",
                        border_width = 2
                        )

make_flights_frame = ctk.CTkFrame(master = principal_frame,
                        width = 900,
                        height = 400,
                        corner_radius = 36,
                        fg_color = "beige",
                        border_color = "white",
                        border_width = 2
                        )

#-------------------------Labels-------------------------
title_label = ctk.CTkLabel(master = make_flights_frame,
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
                        border_color = "light pink",
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
                        border_color = "light pink",
                        border_width = 2,
                        font = font_1,
                        placeholder_text= "Primer Apellido"
                        )

genero = ctk.CTkComboBox(master = make_flights_frame, 
                        values = ["Masculino", "Femenino", "Otro"],
                        width = 250, 
                        height = 50, 
                        corner_radius = 10, 
                        text_color= "black", 
                        fg_color = "white", 
                        border_color = "light pink", 
                        border_width = 2, 
                        font = font_1, 
                        button_color= "light pink",
                        button_hover_color= "light blue",
                        dropdown_fg_color= "white",
                        dropdown_hover_color= "light pink",
                        dropdown_text_color= "black",
                        )

type_identification = ctk.CTkComboBox(master = make_flights_frame, 
                        values = ["C. de Ciudadanía (CC)", "C. de Extranjería (CE)",
                        "Número de Identificación Tributario (NIT)", "Pasaporte"],
                        width = 250, 
                        height = 50, 
                        corner_radius = 10, 
                        text_color= "black", 
                        fg_color = "white", 
                        border_color = "light pink", 
                        border_width = 2, 
                        font = font_1, 
                        button_color= "light pink",
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
                        border_color = "light pink",
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
                        border_color = "light pink",
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
                        border_color = "light pink",
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
                        border_color = "light pink",
                        border_width = 2,
                        font = font_1,
                        placeholder_text= "Correo Electrónico",
                        )

#-------------------------Buttons-------------------------
button_make_flight = ctk.CTkButton(master = make_flights_frame,
                        text = "Seleccionar Vuelo",
                        width = 250,
                        height = 50,
                        corner_radius = 10,
                        fg_color = "light pink",
                        font = font_1,
                        border_color = "light pink",
                        border_width = 2,
                        hover_color= "light blue",
                        text_color= "black"
                        )

continue_flight = ctk.CTkButton(master = make_flights_frame,
                        text = "Continuar",
                        width = 250,
                        height = 50,
                        corner_radius = 10,
                        fg_color = "light pink",
                        font = font_1,
                        border_color = "light pink",
                        border_width = 2,
                        hover_color= "light blue",
                        text_color= "black"
                        )

principal_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
make_flights_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
title_label.place(relx = 0.15, rely = 0.14, anchor = "center")
entry_first_name.place(relx = 0.5, rely = 0.3, anchor = "center")
entry_last_name.place(relx = 0.8, rely = 0.3, anchor = "center")
genero.place(relx = 0.2, rely = 0.3, anchor = "center")
identification.place(relx = 0.5, rely = 0.5, anchor = "center")
nationality.place(relx = 0.8, rely = 0.5, anchor = "center")
type_identification.place(relx = 0.2, rely = 0.5, anchor = "center")
phone.place(relx = 0.5, rely = 0.7, anchor = "center")
email.place(relx = 0.8, rely = 0.7, anchor = "center")
button_make_flight.place(relx = 0.2, rely = 0.7, anchor = "center")
continue_flight.place(relx = 0.5, rely = 0.9, anchor = "center")

root.mainloop()
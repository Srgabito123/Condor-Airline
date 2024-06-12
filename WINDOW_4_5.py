from tkinter import *
import customtkinter as ctk
import CONSTANTES
import WINDOW_6
    
def initialize_root4_5(origin_city, destiny_city, departure_date):
    
    #--------------------------------VENTANA 4_5---------------------------------------

    root4_5 = ctk.CTk()
    root4_5.resizable(0, 0)

    screen_width = root4_5.winfo_screenwidth()
    screen_height = root4_5.winfo_screenheight()
    window_width = 1000
    window_height = 600

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root4_5.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root4_5.config(background="#d7bb9f")
    root4_5.title("CONDOR-AIRLINES")
    root4_5.iconbitmap("images/ICONO.ico")

    #---------------------------FUNCTIONS---------------------------

    def switch_to_window6(num, takeoff_hour, landing_hour, exit_city, coming_city, price):
        root4_5.destroy()
        import WINDOW_6
        WINDOW_6.initialize_root6(num, takeoff_hour, landing_hour, exit_city, coming_city, price)
        

    def eleccion_vuelo(min_price, mid_price, max_price, takeoff_hour, landing_hour, exit_city, coming_city):

        if flight_choice_frame.winfo_viewable():
            flight_choice_frame.place_forget()
        else:
            flight_choice_frame.place(relx = 0.49, rely = 0.6, anchor = "center")

            plata_clase = ctk.CTkButton(master = flight_choice_frame,
                            width=285,
                            height=400, 
                            fg_color="beige",
                            border_width=2,
                            corner_radius=32,
                            hover_color= "beige",
                            text= ""
                            )

            diamante_clase = ctk.CTkButton(master = flight_choice_frame,
                                    width=285,
                                    height=400, 
                                    fg_color="beige",
                                    hover_color= "beige",
                                    border_width=2,
                                    corner_radius=32
                                    )

            premium_clase = ctk.CTkButton(master = flight_choice_frame,
                                    width=285,
                                    height=400, 
                                    fg_color="beige",
                                    hover_color= "beige",
                                    border_width=2,
                                    corner_radius=32
                                    )

            select_plata = ctk.CTkButton(master = plata_clase,
                                    width=230,
                                    height=30, 
                                    font = (font_1, 15),
                                    fg_color="light pink",
                                    hover_color= "light blue",
                                    border_width=2,
                                    corner_radius=36,
                                    text_color="black",
                                    text="Seleccionar",
                                    command=lambda: switch_to_window6(3, takeoff_hour, landing_hour, 
                                                                      exit_city, coming_city, min_price)
                                    )

            select_diamante = ctk.CTkButton(master = diamante_clase,
                                    width=230,
                                    height=30, 
                                    font = (font_1, 15),
                                    fg_color="light pink",
                                    hover_color= "light blue",
                                    border_width=2,
                                    corner_radius=36,
                                    text_color="black",
                                    text="Seleccionar",
                                    command=lambda: switch_to_window6(2, takeoff_hour, landing_hour, 
                                                                      exit_city, coming_city, mid_price)
                                    )

            select_premium = ctk.CTkButton(master = premium_clase,
                                    width=230,
                                    height=30, 
                                    font = (font_1, 15),
                                    fg_color="light pink",
                                    hover_color= "light blue",
                                    border_width=2,                    
                                    corner_radius=36,
                                    text_color="black",
                                    text="Seleccionar",
                                    command=lambda: switch_to_window6(1, takeoff_hour, landing_hour, 
                                                                      exit_city, coming_city, max_price)
                                    )

            close_window = ctk.CTkButton(master = flight_choice_frame,
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
            nombre_plata = ctk.CTkLabel(master = plata_clase,
                                text = "Plata",
                                fg_color = "transparent",
                                text_color = "black",
                                font = font_1,
                                width = 0.3,
                                height = 0.3
                                )
            precio_plata = ctk.CTkLabel(master = plata_clase,
                                        text = f"Desde ${min_price} COP",
                                        fg_color = "transparent",
                                        text_color = "black",
                                        font = (font_1, 14),
                                        width = 0.3,
                                        height = 0.3
                                        )

            texto_plata = ctk.CTkLabel(master = plata_clase,
                                        text = plata,
                                        fg_color = "transparent",
                                        bg_color= "transparent",
                                        text_color = "black",
                                        font = (font_1, 13),
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
                
            precio_diamante = ctk.CTkLabel(master = diamante_clase,
                                        text = f"Desde ${mid_price} COP",
                                        fg_color = "transparent",
                                        text_color = "black",
                                        font = (font_1, 13),
                                        width = 0.3,
                                        height = 0.3
                                        )

            texto_diamante = ctk.CTkLabel(master = diamante_clase,
                                        text = diamante,
                                        fg_color = "transparent",
                                        text_color = "black",
                                        bg_color= "transparent",
                                        font = (font_1, 12.5),
                                        width = 100,
                                        height = 90,
                                        )

            nombre_premium = ctk.CTkLabel(master = premium_clase,
                                        text = "Premium",
                                        fg_color = "transparent",
                                        text_color = "black",
                                        font = font_1,
                                        width = 0.3,
                                        height = 0.3
                                        )
                
            precio_premium = ctk.CTkLabel(master = premium_clase,
                                        text = f"Desde ${max_price} COP",
                                        fg_color = "transparent",
                                        text_color = "black",
                                        font = (font_1, 13),
                                        width = 0.3,
                                        height = 0.3
                                        )

            texto_premium = ctk.CTkLabel(master = premium_clase,
                                        text = premium,
                                        fg_color = "transparent",
                                        bg_color= "transparent",
                                        text_color = "black",
                                        font = (font_1, 12.5),
                                        width = 100,
                                        height = 100
                                        )
            
            nombre_plata.place(relx=0.5, rely=0.05, anchor="center")
            precio_plata.place(relx=0.5, rely=0.15, anchor="center")
            texto_plata.place(relx=0.5, rely=0.5, anchor="center")
            nombre_diamante.place(relx=0.5, rely=0.05, anchor="center")
            precio_diamante.place(relx=0.5, rely=0.15, anchor="center")
            texto_diamante.place(relx=0.5, rely=0.5, anchor="center")
            nombre_premium.place(relx=0.5, rely=0.05, anchor="center")
            precio_premium.place(relx=0.5, rely=0.15, anchor="center")
            texto_premium.place(relx=0.5, rely=0.5, anchor="center")
            plata_clase.place(relx=0.17, rely=0.03, anchor="n")
            diamante_clase.place(relx=0.50, rely=0.03, anchor="n")
            premium_clase.place(relx=0.83, rely=0.03, anchor="n")
            close_window.place(relx=0.5, rely=0.93, anchor="center") 
            select_plata.place(relx=0.5, rely=0.93, anchor="center")
            select_diamante.place(relx=0.5, rely=0.93, anchor="center")
            select_premium.place(relx=0.5, rely=0.93, anchor="center")


    def cerrar_ventana():
        flight_choice_frame.place_forget()

    #---------------------------VARIABLES---------------------------

    departure_city = origin_city
    arrival_city = destiny_city
    ida = f"Ida: {departure_city} - {arrival_city}"

    fecha = departure_date
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

    principal_frame = ctk.CTkFrame(master = root4_5,
                            width = 1000,
                            height = 600,
                            corner_radius = 10,
                            fg_color = "#d7bb9f",
                            border_color = "white",
                            border_width = 2,
                            bg_color = "transparent"
                            )
    
    date_buttons_frame = ctk.CTkFrame(master = principal_frame,
                                        width = 880,
                                        height = 40,
                                        fg_color = "#d7bb9f",
                                        )   

    flights_frame = ctk.CTkScrollableFrame(master = principal_frame,
                            width = 930,
                            height = 400,
                            fg_color = "transparent",
                            corner_radius = 30,
                            scrollbar_button_color = "beige",
                            orientation = "vertical"
                            )

    flight_choice_frame = ctk.CTkFrame(master = principal_frame,
                            width=940,
                            height=470, 
                            fg_color="white",
                            border_width=2,
                            border_color="beige",
                            corner_radius=32
                            )

    #---------------------------BOTONES---------------------------

    for i in range(len(CONSTANTES.flights)):

        button_flight = ctk.CTkButton(master = flights_frame,    
                                width = 890, 
                                height = 160, 
                                corner_radius = 50,
                                fg_color = "beige",
                                hover_color = "beige",
                                text = " ",
                                border_color= "black",
                                border_width= 1.5,
                                command=lambda i=i:eleccion_vuelo(CONSTANTES.min_price[i], 
                                                                  CONSTANTES.mid_price[i], 
                                                                  CONSTANTES.max_price[i],
                                                                  CONSTANTES.takeoff_hour[i],
                                                                  CONSTANTES.landing_hour[i],
                                                                  CONSTANTES.exit_city[i],
                                                                  CONSTANTES.coming_city[i])
                                )

        departure_hour_text = ctk.CTkLabel(master = button_flight, 
                                text = CONSTANTES.departure_hour[i],
                                fg_color = "transparent",
                                bg_color= "beige",
                                text_color = "black",
                                font = font_1,
                                width = 0.1,
                                height = 0.3
                                )

        arrival_hour_text = ctk.CTkLabel(master = button_flight, 
                                text = CONSTANTES.arrival_hour[i],
                                fg_color = "beige",
                                text_color = "black",
                                font = font_1,
                                width = 0.1,
                                height = 0.3,
                                corner_radius = 10,
                                )

        departure_place_text = ctk.CTkLabel(master = button_flight, 
                                text = departure_city,
                                fg_color = "Beige",
                                text_color = "black",
                                font = font_1,
                                width = 0.1,
                                height = 0.3,
                                corner_radius = 10,
                                )

        arrival_place_text = ctk.CTkLabel(master = button_flight, 
                                text = arrival_city,
                                fg_color = "Beige",
                                text_color = "black",
                                font = font_1,
                                width = 0.1,
                                height = 0.3,
                                corner_radius = 10,
                                )

        text_desde = ctk.CTkLabel(master = button_flight,
                                text = """DESDE:

                                    COP $""",
                                fg_color = "transparent",
                                text_color = "black",
                                font = font_1,
                                width = 80,
                                height = 80,
                                corner_radius = 10,
                                )

        text_precio = ctk.CTkLabel(master = button_flight,
                                text = CONSTANTES.price[i],
                                fg_color = "beige",
                                text_color = "black",
                                font = font_1,
                                width = 60,
                                height = 30,
                                corner_radius = 10,
                                )

        text_flechita = ctk.CTkLabel(master = button_flight,
                                text = flechita,
                                fg_color = "beige",
                                text_color = "black",
                                font = ("roboto", 20),
                                width = 0.3,
                                height = 0.3,
                                )
        
        button_flight.pack(padx=5, pady=10, expand= True, anchor = "center")
        departure_hour_text.place(relx = 0.1, rely = 0.4, anchor = "center")
        departure_place_text.place(relx = 0.1, rely = 0.54, anchor = "center")
        arrival_hour_text.place(relx = 0.5, rely = 0.4, anchor = "center")
        arrival_place_text.place(relx = 0.5, rely = 0.54, anchor = "center")
        text_desde.place(relx = 0.68, rely = 0.4, anchor = "center")
        text_precio.place(relx = 0.86, rely = 0.53, anchor = "center")
        text_flechita.place(relx = 0.3, rely = 0.45, anchor = "center")

        def replace_buttons(departure_city, arrival_city, date):

            CONSTANTES.recive_data(departure_city, arrival_city, date)
            for widget in flights_frame.winfo_children():
                widget.destroy()
            

            for i in range(len(CONSTANTES.flights)):
                button_flight = ctk.CTkButton(master = flights_frame,    
                                        width = 890, 
                                        height = 160, 
                                        corner_radius = 50,
                                        fg_color = "beige",
                                        hover_color = "beige",
                                        text = " ",
                                        border_color= "black",
                                        border_width= 1.5,
                                        command=lambda i=i:eleccion_vuelo(CONSTANTES.min_price[i], 
                                                                  CONSTANTES.mid_price[i], 
                                                                  CONSTANTES.max_price[i],
                                                                  CONSTANTES.takeoff_hour[i],
                                                                  CONSTANTES.landing_hour[i],
                                                                  CONSTANTES.exit_city[i],
                                                                  CONSTANTES.coming_city[i]))

                departure_hour_text = ctk.CTkLabel(master = button_flight, 
                                        text = CONSTANTES.departure_hour[i],
                                        fg_color = "transparent",
                                        bg_color= "beige",
                                        text_color = "black",
                                        font = font_1,
                                        width = 0.1,
                                        height = 0.3
                                        )

                arrival_hour_text = ctk.CTkLabel(master = button_flight, 
                                        text = CONSTANTES.arrival_hour[i],
                                        fg_color = "beige",
                                        text_color = "black",
                                        font = font_1,
                                        width = 30,
                                        height = 0.3,
                                        corner_radius = 10,
                                        )

                departure_place_text = ctk.CTkLabel(master = button_flight, 
                                        text = departure_city,
                                        fg_color = "Beige",
                                        text_color = "black",
                                        font = font_1,
                                        width = 0.1,
                                        height = 0.3,
                                        corner_radius = 10,
                                        )

                arrival_place_text = ctk.CTkLabel(master = button_flight, 
                                        text = arrival_city,
                                        fg_color = "Beige",
                                        text_color = "black",
                                        font = font_1,
                                        width = 12,
                                        height = 0.3,
                                        corner_radius = 10,
                                        )

                text_desde = ctk.CTkLabel(master = button_flight,
                                        text = """DESDE:

                                            COP $""",
                                        fg_color = "transparent",
                                        text_color = "black",
                                        font = font_1,
                                        width = 0.08,
                                        height = 0.3,
                                        corner_radius = 10,
                                        )

                text_precio = ctk.CTkLabel(master = button_flight,
                                        text = CONSTANTES.price[i],
                                        fg_color = "beige",
                                        text_color = "black",
                                        font = font_1,
                                        width = 0.1,
                                        height = 0.3,
                                        corner_radius = 10,
                                        )

                text_flechita = ctk.CTkLabel(master = button_flight,
                                        text = flechita,
                                        fg_color = "beige",
                                        text_color = "black",
                                        font = ("roboto", 20),
                                        width = 0.3,
                                        height = 0.3,
                                        )
                
                button_flight.pack(padx=5, pady=10, expand= True, anchor = "center")
                departure_hour_text.place(relx = 0.1, rely = 0.4, anchor = "center")
                departure_place_text.place(relx = 0.1, rely = 0.54, anchor = "center")
                arrival_hour_text.place(relx = 0.5, rely = 0.4, anchor = "center")
                arrival_place_text.place(relx = 0.5, rely = 0.54, anchor = "center")
                text_desde.place(relx = 0.7, rely = 0.4, anchor = "center")
                text_precio.place(relx = 0.89, rely = 0.53, anchor = "center")
                text_flechita.place(relx = 0.3, rely = 0.45, anchor = "center")

    for i in range(len(CONSTANTES.all_dates)):
        day_button = ctk.CTkButton(master = date_buttons_frame,
                                text = f"Fecha: {CONSTANTES.all_dates[i]}",
                                font = (font_1, 13), 
                                text_color = "black",
                                width = 70, 
                                height = 50, 
                                corner_radius = 32,
                                border_color= "black",
                                border_width= 1.5, 
                                fg_color = "beige",  
                                hover_color = "light blue",
                                command=lambda i=i: replace_buttons(departure_city, arrival_city, CONSTANTES.all_dates[i])
                                
                                )
        day_button.pack(side = LEFT, padx = 10)


    

    #---------------------------TEXTOS---------------------------

    text_viaje = ctk.CTkLabel(master = principal_frame, 
                            text = ida, 
                            fg_color = "beige", 
                            width = 0.2, 
                            height = 0.065, 
                            text_color = "black", 
                            font = font_1, 
                            corner_radius = 10, 
                            bg_color = "#d7bb9f",
                            )
    
    
   
                        
    #---------------------------POSICIONAMIENTO-----------------------

    principal_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
    flights_frame.place(relx = 0.5, rely = 0.59, anchor = "center")
    flight_choice_frame.place_forget()
    text_viaje.place(x = 6, y = 8, relwidth = 0.3, relheight = 0.065)
    date_buttons_frame.place(x = 50, y = 70)
    root4_5.mainloop()
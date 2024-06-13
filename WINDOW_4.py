import customtkinter as ctk
import CONSTANTES

def initialize_root4(num, takeoff_hour, landing_hour, exit_city, coming_city, price, flight_code, flight_date_):
   global departure_time, arrival_time, departure_city, arrival_city, takeoff_hour_f, landing_hour_f, exit_city_f, coming_city_f, price_f, flight_code_f, flight_date_f
   #-------------------------------VENTANA 6-------------------------

   takeoff_hour_f = takeoff_hour
   landing_hour_f = landing_hour
   exit_city_f = exit_city
   coming_city_f = coming_city
   price_f = price
   flight_code_f = flight_code
   flight_date_f = flight_date_
   
   root4 = ctk.CTk()
   root4.title("CONDOR-AIRLINES")
   root4._set_appearance_mode("light")
   root4.geometry("1000x600")
   root4.resizable(0,0)
   root4.config(bg = "#d7bb9f")
   root4.iconbitmap("images/ICONO.ico")
   
   def switch_to_root5(category, num):
      root4.destroy()
      import WINDOW_5
      WINDOW_5.initialize_root5(category, num) 
   #---------------------------VARIABLES---------------------------

   departure_time = takeoff_hour
   arrival_time = landing_hour
   departure_city = exit_city
   arrival_city = coming_city
   price = price

   category = ""
   if num == 1:
      category = "Premium"
   elif num == 2:
      category = "Diamante"
   elif num == 3:
      category = "Plata"



   
   ida = f"Ida: {departure_city} - {arrival_city}"
   arrow = "-------------------------------------->"
   font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")
   principal_frame = ctk.CTkFrame(master = root4,
                              width = 1000,
                              height = 600,
                              corner_radius = 30,
                              fg_color = "#d7bb9f",
                              border_color = "#d7bb9f",
                              border_width = 2,
                              bg_color = "#d7bb9f"
                              )
   #---------------------------BOTONES---------------------------
   select_button = ctk.CTkButton(master = root4,
                                 text = "SELECCIONAR",
                                 bg_color="#d7bb9f", 
                                 fg_color="#a06553",
                                 text_color = "white",
                                 font = (font_1, 16, "bold"),
                                 width = 35,
                                 height = 35,
                                 corner_radius = 10,
                                 border_width = 1.5,
                                 hover_color = "beige",
                                 border_color = "#a06553",
                                 command= lambda: switch_to_root5(category, num)
                                 )
   button_flight = ctk.CTkButton(master = principal_frame,    
                                width = 890, 
                                height = 160, 
                                corner_radius = 50,
                                fg_color = "beige",
                                hover_color = "beige",
                                text = " ",
                                border_color= "black",
                                border_width= 1.5,
                                )
   
   text_reservation = ctk.CTkLabel(master = root4,
                           text = f"Total reservation: COP ${price}",
                           fg_color = "#d7bb9f",
                           text_color = "black",
                           font = (font_1, 20),
                           width = 0.3,
                           height = 0.3,
                           bg_color = "#d7bb9f",
                           corner_radius = 10
                           )

   departure_hour_text = ctk.CTkLabel(master = button_flight, 
                                text = departure_time,
                                fg_color = "transparent",
                                bg_color= "beige",
                                text_color = "black",
                                font = font_1,
                                width = 0.1,
                                height = 0.3
                                )

   arrival_hour_text = ctk.CTkLabel(master = button_flight, 
                                text = arrival_time,
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
                                width = 0.1,
                                height = 0.3,
                                corner_radius = 10,
                                )

   text_precio = ctk.CTkLabel(master = button_flight,
                                text = price,
                                fg_color = "beige",
                                text_color = "black",
                                font = font_1,
                                width = 0.1,
                                height = 0.3,
                                corner_radius = 10,
                                )

   text_flechita = ctk.CTkLabel(master = button_flight,
                                text = arrow,
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
   #---------------------------TEXTOS---------------------------
   text_category = ctk.CTkLabel(master = button_flight,
                           text = category,
                           fg_color = "#a06553",
                           text_color = "white",
                           font = (font_1, 14),
                           width = 0.1,
                           height = 0.3,
                           corner_radius = 10,
                           bg_color = "transparent"
                           )
   text_viaje = ctk.CTkLabel(master = root4, 
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
   principal_frame.place(relx = 0.5, rely = 0.3, anchor = "center")
   text_category.place(x = 710, y = 30, relwidth = 0.1, relheight = 0.25)
   select_button.place(relx = 0.83, rely = 0.825, anchor = "center")
   text_viaje.place(x = 6, y = 8, relwidth = 0.3, relheight = 0.065)
   text_reservation.place(x = 50, y = 480, relwidth = 0.35, relheight = 0.07)
   root4.mainloop()
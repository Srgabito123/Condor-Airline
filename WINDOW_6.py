from customtkinter import *
def initialize_root6():

   #-------------------------------VENTANA 6-------------------------

   root6 = CTk()
   root6.title("CONDOR-AIRLINES")
   root6._set_appearance_mode("light")
   root6.geometry("1000x600")
   root6.resizable(0,0)
   root6.config(bg = "#d7bb9f")
   root6.iconbitmap("images/ICONO.ico")
   #
   #---------------------------VARIABLES---------------------------

   arrival_time = "13:00"
   departure_time = "10:00"
   departure_place = "Bogotá"
   arrival_place = "Cartagena"
   going = f"Going: {departure_place} - {arrival_place}"
   price = "2.000.000"
   date_ = "2024-06-13"
   arrow = "-------------------------------------->"
   category = "Aluminio"
   font_1 = CTkFont(family="Inherit", size=18, weight="bold")
   principal_frame = CTkFrame(master = root6,
                              width = 1000,
                              height = 600,
                              corner_radius = 10,
                              fg_color = "#d7bb9f",
                              border_color = "white",
                              border_width = 2,
                              bg_color = "transparent"
                              )
   #---------------------------BOTONES---------------------------
   select_button = CTkButton(master = principal_frame,
                                 text = "SELECT",
                                 bg_color="#d7bb9f", 
                                 fg_color="#a06553",
                                 text_color = "white",
                                 font = (font_1, 16, "bold"),
                                 width = 35,
                                 height = 35,
                                 corner_radius = 10,
                                 border_width = 1.5,
                                 hover_color = "beige",
                                 border_color = "#a06553"
                                 )
   option1 = CTkButton(master = principal_frame, 
                     bg_color = "#d7bb9f", 
                     width = 850, 
                     height = 100, 
                     corner_radius = 50,
                     fg_color = "beige",
                     hover_color = "beige",
                     text = " ",
                     border_width = 1.5,
                     border_color = "#a06553"
                     )
   #---------------------------FRAMES---------------------------
   journey_frame = CTkFrame(master = principal_frame, 
                        fg_color="white", 
                        bg_color = "#d7bb9f",  
                        corner_radius = 10, 
                        width = 0.11, 
                        height = 0.065, 
                        )
   #---------------------------TEXTOS---------------------------
   text_journey = CTkLabel(master= principal_frame, 
                        text = going, 
                        fg_color = "beige", 
                        width = 0.9, 
                        height = 0.7, 
                        text_color = "black", 
                        font = (font_1, 12),  
                        bg_color = "#d7bb9f",
                        corner_radius = 10
                        )
   text_departure_time = CTkLabel(master = option1, 
                              text = departure_time,
                              fg_color = "beige",
                              text_color = "black",
                              font = (font_1, 18),
                              width = 0.1,
                              height = 0.3,
                              corner_radius = 10,
                              bg_color = "beige"
                              )
   text_arrival_time = CTkLabel(master = option1, 
                              text = arrival_time,
                              fg_color = "beige",
                              text_color = "black",
                              font = (font_1, 18),
                              width = 0.1,
                              height = 0.3,
                              corner_radius = 10,
                              bg_color = "beige"
                              )
   text_departure_place = CTkLabel(master = option1, 
                              text = departure_place,
                              fg_color = "Beige",
                              text_color = "black",
                              font = (font_1, 13),
                              width = 0.1,
                              height = 0.3,
                              corner_radius = 10,
                              bg_color = "beige"
                              )
   text_arrival_place = CTkLabel(master = option1, 
                              text = arrival_place,
                              fg_color = "Beige",
                              text_color = "black",
                              font = (font_1, 13),
                              width = 0.1,
                              height = 0.3,
                              corner_radius = 10,
                              bg_color = "beige"
                              )
   text_desde = CTkLabel(master = option1,
                        text = """DESDE:

                           COP $""",
                        fg_color = "beige",
                        text_color = "black",
                        font = (font_1, 11),
                        width = 0.1,
                        height = 0.3,
                        corner_radius = 10,
                        bg_color = "beige"
                        )
   text_price = CTkLabel(master = option1, 
                        text = price, 
                        fg_color = "beige", 
                        text_color = "black", 
                        font = (font_1, 11), 
                        width = 0.1, 
                        height = 0.3, 
                        corner_radius = 10, 
                        bg_color = "beige"
                        )
   text_arrow = CTkLabel(master = option1,
                           text = arrow,
                           fg_color = "beige",
                           text_color = "black",
                           font = ("roboto", 20),
                           width = 0.3,
                           height = 0.3,
                           bg_color = "beige"
                           )
   text_reservation = CTkLabel(master = principal_frame,
                           text = f"Total reservation: COP ${price}",
                           fg_color = "#d7bb9f",
                           text_color = "black",
                           font = (font_1, 20),
                           width = 0.3,
                           height = 0.3,
                           bg_color = "#d7bb9f",
                           corner_radius = 10
                           )
   text_category = CTkLabel(master = option1,
                           text = category,
                           fg_color = "#a06553",
                           text_color = "white",
                           font = (font_1, 14),
                           width = 0.1,
                           height = 0.3,
                           corner_radius = 10,
                           bg_color = "transparent"
                           )
   #---------------------------POSICIONAMIENTO-----------------------
   principal_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
   journey_frame.place(x = 6, y = 5, relwidth = 0.3, relheight = 0.065)
   text_journey.place(x = 6, y = 5, relwidth = 0.3, relheight = 0.065)
   option1.place(relx = 0.5, rely = 0.25, anchor = "center")
   text_departure_time.place(x = 25, y = 30, relwidth = 0.08, relheight = 0.15)
   text_departure_place.place(x = 25, y = 55, relwidth = 0.08, relheight = 0.18)
   text_arrival_time.place(x = 369, y = 30, relwidth = 0.08, relheight = 0.15)
   text_arrival_place.place(x = 369, y = 55, relwidth = 0.08, relheight = 0.18)
   text_desde.place(x = 460, y = 27, relwidth = 0.19, relheight = 0.4)
   text_price.place(x = 596, y = 55, relwidth = 0.08, relheight = 0.085)
   text_arrow.place(x = 103, y = 37, relwidth = 0.3, relheight = 0.1)
   text_category.place(x = 710, y = 30, relwidth = 0.1, relheight = 0.25)
   select_button.place(relx = 0.83, rely = 0.825, anchor = "center")
   text_reservation.place(x = 50, y = 480, relwidth = 0.35, relheight = 0.07)
   root6.mainloop()
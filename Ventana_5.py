from tkinter import *
import customtkinter as ctk

root = ctk.CTk()
root.title("CONDOR")
root._set_appearance_mode("light")
root.geometry("1000x600")
root.resizable(0, 0)
root.config(bg="light pink")
# root.iconbitmap("logo.ico")

# ---------------------------functions---------------------------
def flight_selection():
    if flight_selection_frame.winfo_viewable():
        flight_selection_frame.place_forget()
    else:
        flight_selection_frame.place(relx=0.49, rely=0.6, anchor="center")

def close_window():
    flight_selection_frame.place_forget()

# ---------------------------VARIABLES---------------------------
arrival_time = "13:00"
departure_time = "10:00"
departure_location = "Bogotá"
arrival_location = "Cartagena"
one_way = f"One way: {departure_location} - {arrival_location}"
price = "2,000,000"
date = "2024-06-13"
arrow = "-------------------------------------->"
silver = """
1 artículo personal (bolso) 
(Debe caber debajo del asiento)

1 equipaje de mano (10 kg) 
(Desde $195,100 COP)

Equipaje facturado (23 kg) 
(Desde $175,600 COP)

Asiento de clase económica 
(Asignado al azar - Aluminio)

Cambios de vuelo (No permitidos)

Reembolso (No permitido)"""

diamond = """
1 artículo personal (bolso) 
(Debe caber debajo del asiento)

1 equipaje facturado (23 kg) 
(Debe caber en el compartimento superior)

1 equipaje de mano (10 kg) 
(Dejar el equipaje en el mostrador)

Asiento de clase económica 
(Filas específicas disponibles al azar)

Cambios de vuelo (No permitidos)

Reembolso (No permitido)"""

premium = """
1 artículo personal (bolso) 
(Debe caber debajo del asiento)

1 equipaje de mano (10 kg) 
(Debe caber en el compartimento superior)

1 equipaje facturado (23 kg) 
(Dejar el equipaje en el mostrador)

Asiento Plus 
(Sujeto a disponibilidad-Clase premium)

Cambios de vuelo 
(Sin cargo por cambios, antes del vuelo)

Reembolso (No permitido)"""

# ---------------------------FONTS---------------------------

font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")

# ---------------------------FRAMES---------------------------

main_frame = ctk.CTkFrame(master=root,
                          width=1000,
                          height=600,
                          corner_radius=10,
                          fg_color="light pink",
                          border_color="white",
                          border_width=2,
                          bg_color="transparent"
                          )

flight_frame = ctk.CTkScrollableFrame(master=main_frame,
                                      width=930,
                                      height=400,
                                      fg_color="transparent",
                                      corner_radius=30,
                                      scrollbar_button_color="beige",
                                      orientation="vertical"
                                      )

flight_selection_frame = ctk.CTkFrame(master=main_frame,
                                      width=940,
                                      height=470,
                                      fg_color="white",
                                      border_width=2,
                                      border_color="beige",
                                      corner_radius=32
                                      )

# ---------------------------BUTTONS---------------------------

option1 = ctk.CTkButton(master=flight_frame,
                        width=890,
                        height=160,
                        corner_radius=50,
                        fg_color="beige",
                        hover_color="beige",
                        text=" ",
                        border_color="black",
                        border_width=1.5,
                        command=flight_selection
                        )

option2 = ctk.CTkButton(master=flight_frame,
                        fg_color="beige",
                        width=890,
                        height=160,
                        corner_radius=50,
                        bg_color="light pink",
                        hover_color="beige",
                        text=" ",
                        border_color="black",
                        border_width=1.5,
                        command=flight_selection
                        )

option3 = ctk.CTkButton(master=flight_frame,
                        fg_color="beige",
                        width=890,
                        height=160,
                        corner_radius=50,
                        bg_color="light pink",
                        hover_color="beige",
                        text=" ",
                        border_color="black",
                        border_width=1.5,
                        command=flight_selection
                        )

option4 = ctk.CTkButton(master=flight_frame,
                        fg_color="beige",
                        width=890,
                        height=160,
                        corner_radius=50,
                        bg_color="light pink",
                        hover_color="beige",
                        text=" ",
                        border_color="black",
                        border_width=1.5,
                        command=flight_selection
                        )

days_button1 = ctk.CTkButton(master=main_frame,
                             text=f"Fecha: {date}",
                             font=(font_1, 13),
                             text_color="black",
                             width=100,
                             height=50,
                             corner_radius=32,
                             border_color="black",
                             border_width=1.5,
                             fg_color="beige",
                             hover_color="light blue"
                             )

days_button2 = ctk.CTkButton(master=main_frame,
                             text=f"Fecha: {date}",
                             font=(font_1, 13),
                             text_color="black",
                             width=100,
                             height=50,
                             corner_radius=32,
                             border_color="black",
                             border_width=1.5,
                             fg_color="beige",
                             hover_color="light blue"
                             )

days_button3 = ctk.CTkButton(master=main_frame,
                             text=f"Fecha: {date}",
                             font=(font_1, 13),
                             text_color="black",
                             width=100,
                             height=50,
                             corner_radius=32,
                             border_color="black",
                             border_width=1.5,
                             fg_color="beige",
                             hover_color="light blue"
                             )

days_button4 = ctk.CTkButton(master=main_frame,
                             text=f"Fecha: {date}",
                             font=(font_1, 13),
                             text_color="black",
                             width=100,
                             height=50,
                             corner_radius=32,
                             border_color="black",
                             border_width=1.5,
                             fg_color="beige",
                             hover_color="light blue"
                             )

days_button5 = ctk.CTkButton(master=main_frame,
                             text=f"Fecha: {date}",
                             font=(font_1, 13),
                             text_color="black",
                             width=100,
                             height=50,
                             corner_radius=32,
                             border_color="black",
                             border_width=1.5,
                             fg_color="beige",
                             hover_color="light blue"
                             )

best_price_button = ctk.CTkButton(master=main_frame,
                                  text="Mejor precio",
                                  font=(font_1, 13),
                                  text_color="black",
                                  width=100,
                                  height=50,
                                  corner_radius=32,
                                  border_color="black",
                                  border_width=1.5,
                                  fg_color="beige",
                                  hover_color="light blue"
                                  )

direct_flights_button = ctk.CTkButton(master=main_frame,
                                      text="Vuelos directos",
                                      font=(font_1, 13),
                                      text_color="black",
                                      width=100,
                                      height=50,
                                      corner_radius=32,
                                      border_color="black",
                                      border_width=1.5,
                                      fg_color="beige",
                                      hover_color="light blue"
                                      )

silver_class_button = ctk.CTkButton(master=flight_selection_frame,
                                    width=285,
                                    height=400,
                                    fg_color="beige",
                                    border_width=2,
                                    corner_radius=32,
                                    hover_color="beige",
                                    text=""
                                    )

diamond_class_button = ctk.CTkButton(master=flight_selection_frame,
                                     width=285,
                                     height=400,
                                     fg_color="beige",
                                     hover_color="beige",
                                     border_width=2,
                                     corner_radius=32
                                     )

premium_class_button = ctk.CTkButton(master=flight_selection_frame,
                                     width=285,
                                     height=400,
                                     fg_color="beige",
                                     hover_color="beige",
                                     border_width=2,
                                     corner_radius=32
                                     )

select_silver_button = ctk.CTkButton(master=silver_class_button,
                                     width=230,
                                     height=30,
                                     font=(font_1, 15),
                                     fg_color="light pink",
                                     hover_color="light blue",
                                     border_width=2,
                                     corner_radius=36,
                                     text_color="black",
                                     text="Select"
                                     )

select_diamond_button = ctk.CTkButton(master=diamond_class_button,
                                      width=230,
                                      height=30,
                                      font=(font_1, 15),
                                      fg_color="light pink",
                                      hover_color="light blue",
                                      border_width=2,
                                      corner_radius=36,
                                      text_color="black",
                                      text="Select"
                                      )

select_premium_button = ctk.CTkButton(master=premium_class_button,
                                      width=230,
                                      height=30,
                                      font=(font_1, 15),
                                      fg_color="light pink",
                                      hover_color="light blue",
                                      border_width=2,
                                      corner_radius=36,
                                      text_color="black",
                                      text="Select"
                                      )

close_window_button = ctk.CTkButton(master=flight_selection_frame,
                                    width=230,
                                    height=30,
                                    font=(font_1, 15),
                                    fg_color="light blue",
                                    hover_color="light pink",
                                    border_width=2,
                                    corner_radius=36,
                                    text_color="black",
                                    text="Close",
                                    command=close_window
                                    )

# ---------------------------LABELS---------------------------

travel_text = ctk.CTkLabel(master=main_frame,
                           text=one_way,
                           fg_color="beige",
                           width=0.2,
                           height=0.065,
                           text_color="black",
                           font=font_1,
                           corner_radius=10,
                           bg_color="light pink",
                           )

departure_time_label = ctk.CTkLabel(master=option1,
                                    text=departure_time,
                                    fg_color="transparent",
                                    bg_color="beige",
                                    text_color="black",
                                    font=font_1,
                                    width=0.1,
                                    height=0.3
                                    )

arrival_time_label = ctk.CTkLabel(master=option1,
                                  text=arrival_time,
                                  fg_color="beige",
                                  text_color="black",
                                  font=font_1,
                                  width=0.1,
                                  height=0.3,
                                  corner_radius=10,
                                  )

departure_location_label = ctk.CTkLabel(master=option1,
                                        text=departure_location,
                                        fg_color="Beige",
                                        text_color="black",
                                        font=font_1,
                                        width=0.1,
                                        height=0.3,
                                        corner_radius=10,
                                        )

arrival_location_label = ctk.CTkLabel(master=option1,
                                      text=arrival_location,
                                      fg_color="Beige",
                                      text_color="black",
                                      font=font_1,
                                      width=0.1,
                                      height=0.3,
                                      corner_radius=10,
                                      )

from_label = ctk.CTkLabel(master=option1,
                          text="""FROM:

COP $""",
                          fg_color="transparent",
                          text_color="black",
                          font=font_1,
                          width=0.1,
                          height=0.3,
                          corner_radius=10,
                          )

price_label = ctk.CTkLabel(master=option1,
                           text=price,
                           fg_color="beige",
                           text_color="black",
                           font=font_1,
                           width=0.1,
                           height=0.3,
                           corner_radius=10,
                           )

arrow_label = ctk.CTkLabel(master=option1,
                           text=arrow,
                           fg_color="beige",
                           text_color="black",
                           font=("roboto", 20),
                           width=0.3,
                           height=0.3,
                           )

filter_label = ctk.CTkLabel(master=main_frame,
                            text="Filter by:",
                            fg_color="transparent",
                            text_color="black",
                            font=(font_1, 16),
                            width=0.3,
                            height=0.3,
                            bg_color="transparent"
                            )

silver_name_label = ctk.CTkLabel(master=silver_class_button,
                                 text="Silver",
                                 fg_color="transparent",
                                 text_color="black",
                                 font=font_1,
                                 width=0.3,
                                 height=0.3
                                 )

silver_text_label = ctk.CTkLabel(master=silver_class_button,
                                 text=silver,
                                 fg_color="transparent",
                                 bg_color="transparent",
                                 text_color="black",
                                 font=(font_1, 14),
                                 width=100,
                                 height=100
                                 )

diamond_name_label = ctk.CTkLabel(master=diamond_class_button,
                                  text="Diamond",
                                  fg_color="transparent",
                                  text_color="black",
                                  font=font_1,
                                  width=0.3,
                                  height=0.3
                                  )

diamond_text_label = ctk.CTkLabel(master=diamond_class_button,
                                  text=diamond,
                                  fg_color="transparent",
                                  text_color="black",
                                  bg_color="transparent",
                                  font=(font_1, 14),
                                  width=100,
                                  height=100,
                                  )

premium_name_label = ctk.CTkLabel(master=premium_class_button,
                                  text="Premium",
                                  fg_color="transparent",
                                  text_color="black",
                                  font=font_1,
                                  width=0.3,
                                  height=0.3
                                  )

premium_text_label = ctk.CTkLabel(master=premium_class_button,
                                  text=premium,
                                  fg_color="transparent",
                                  bg_color="transparent",
                                  text_color="black",
                                  font=(font_1, 14),
                                  width=100,
                                  height=100
                                  )

# ---------------------------POSITIONING-----------------------

main_frame.place(relx=0.5, rely=0.5, anchor="center")
flight_frame.place(relx=0.5, rely=0.59, anchor="center")
flight_selection_frame.place_forget()
travel_text.place(x=6, y=8, relwidth=0.3, relheight=0.065)
filter_label.place(x=593, y=8, relwidth=0.08, relheight=0.05)
silver_class_button.place(relx=0.17, rely=0.03, anchor="n")
diamond_class_button.place(relx=0.50, rely=0.03, anchor="n")
premium_class_button.place(relx=0.83, rely=0.03, anchor="n")
silver_name_label.place(relx=0.5, rely=0.05, anchor="center")
silver_text_label.place(relx=0.5, rely=0.42, anchor="center")
diamond_name_label.place(relx=0.5, rely=0.05, anchor="center")
diamond_text_label.place(relx=0.5, rely=0.45, anchor="center")
premium_name_label.place(relx=0.5, rely=0.05, anchor="center")
premium_text_label.place(relx=0.5, rely=0.45, anchor="center")
close_window_button.place(relx=0.5, rely=0.93, anchor="center")
best_price_button.place(x=686, y=8, relwidth=0.12, relheight=0.05)
direct_flights_button.place(x=825, y=8, relwidth=0.14, relheight=0.05)
days_button1.place(x=20, y=76, relwidth=0.16, relheight=0.057)
days_button2.place(x=220, y=76, relwidth=0.16, relheight=0.057)
days_button3.place(x=420, y=76, relwidth=0.16, relheight=0.057)
days_button4.place(x=620, y=76, relwidth=0.16, relheight=0.057)
days_button5.place(x=820, y=76, relwidth=0.16, relheight=0.057)
option1.pack(padx=5, pady=10, expand=True, anchor="center")
option2.pack(padx=5, pady=10, expand=True, anchor="center")
option3.pack(padx=5, pady=10, expand=True, anchor="center")
option4.pack(padx=5, pady=10, expand=True, anchor="center")
departure_time_label.place(relx=0.1, rely=0.4, anchor="center")
departure_location_label.place(relx=0.1, rely=0.54, anchor="center")
arrival_time_label.place(relx=0.5, rely=0.4, anchor="center")
arrival_location_label.place(relx=0.5, rely=0.54, anchor="center")
from_label.place(relx=0.66, rely=0.4, anchor="center")
price_label.place(relx=0.83, rely=0.53, anchor="center")
arrow_label.place(relx=0.3, rely=0.45, anchor="center")
select_silver_button.place(relx=0.5, rely=0.93, anchor="center")
select_diamond_button.place(relx=0.5, rely=0.93, anchor="center")
select_premium_button.place(relx=0.5, rely=0.93, anchor="center")
root.mainloop()
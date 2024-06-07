from customtkinter import *
import tkinter as tk
#ventana 8
root8 = CTk()
root8.title("CONDOR-AIRLINES")
root8._set_appearance_mode("light")
root8.geometry("1000x600")
root8.resizable(0,0)
root8.config(bg = "#d7bb9f")
root8.iconbitmap("images/ICONO.ico")
#---------------------------VARIABLES---------------------------
arrival_time = "13:00"
departure_time = "10:00"
departure_place = "Bogotá"
arrival_place = "Cartagena"
going = f"Going: {departure_place} - {arrival_place}"
price = "2.000.000"
date_ = "2024-06-13"
arrow = "------------------------>"
category = "Aluminio"
font_1 = CTkFont(family="Inherit", size=18, weight="bold")
month = ["January", 
          "February", 
          "March", 
          "April", 
          "May", 
          "June", 
          "July", 
          "August", 
          "September", 
          "October", 
          "November", 
          "December"]
years = ["2024", "2025", "2026", "2027", "2028", "2029", "2030","2031", "2032", "2033", "2034", "2035"]
#---------------------------FRAMES---------------------------
principal_frame = CTkFrame(master = root8, 
                           width = 1000, 
                           height = 600, 
                           corner_radius = 10, 
                           fg_color = "#d7bb9f", 
                           border_color = "white", 
                           border_width = 2, 
                           bg_color = "transparent"
                           )
card_data_frame = CTkFrame(master = principal_frame,
                               width = 450,
                               height = 460,
                               corner_radius = 10,
                               fg_color = "beige",
                               border_color = "#a06553",
                               border_width = 2,
                               bg_color = "transparent"
                               )
purchase_summary_frame = CTkFrame(master = principal_frame,
                               width = 500,
                               height = 460,
                               corner_radius = 10,
                               fg_color = "beige",
                               border_color = "#a06553",
                               border_width = 2,
                               bg_color = "transparent"
                               )
#---------------------------COMBOBOXES---------------------------
month_ = CTkComboBox(master = card_data_frame,
                  values = month,
                  width = 120,
                  height = 30,
                  border_color = "#a06553",
                  border_width = 1.5,
                  fg_color = "beige",
                  text_color = "black",
                  bg_color = "transparent",
                  button_color = "#a06553",
                  dropdown_fg_color = "beige",
                  dropdown_text_color = "black",
                  dropdown_hover_color = "#a06553", 
                  dropdown_font = (font_1, 12),
                  )
year = CTkComboBox(master = card_data_frame,
                  values = years,
                  width = 120,
                  height = 30,
                  border_color = "#a06553",
                  border_width = 1.5,
                  fg_color = "beige",
                  text_color = "black",
                  bg_color = "transparent",
                  button_color = "#a06553",
                  dropdown_fg_color = "beige",
                  dropdown_text_color = "black",
                  dropdown_hover_color = "#a06553",
                  dropdown_font = (font_1, 12),
                  )
#---------------------------ENTRADAS---------------------------
titular_name = CTkEntry(master = card_data_frame,
                        width = 400,
                        height = 50,
                        border_color = "#a06553",
                        border_width = 1.5,
                        fg_color = "beige",
                        text_color = "black",
                        bg_color = "transparent",
                        placeholder_text = "Titular name",
                        placeholder_text_color = "#a06553",
                        font = (font_1, 16)
                        )
card_number = CTkEntry(master = card_data_frame,
                       width = 400,
                       height = 50,
                       border_color = "#a06553",
                       border_width = 1.5,
                       fg_color = "beige",
                       text_color = "black",
                       bg_color = "transparent",
                       placeholder_text = "Card number",
                       placeholder_text_color = "#a06553",
                       font = (font_1, 16)
                       )
ccv = CTkEntry(master = card_data_frame, 
               width = 120, 
               height = 30,
               border_color = "#a06553",
               border_width = 1.5,
               fg_color = "beige",
               text_color = "black",
               bg_color = "transparent",
               placeholder_text = "CCV",
               placeholder_text_color = "#a06553",
               font = (font_1, 12)
               )
#---------------------------BOTONES---------------------------
pay = CTkButton(master = principal_frame,
                text = "PAY",
                text_color = "white",
                font = (font_1, 16, "bold"),
                width = 80,
                height = 15,
                bg_color = "transparent",
                fg_color = "#a06553",
                border_color = "beige",
                border_width = 1.5,
                hover_color = "beige"
                )
option1 = CTkButton(master = purchase_summary_frame, 
                   bg_color = "beige", 
                   width = 480, 
                   height = 80, 
                   corner_radius = 30,
                   fg_color = "beige",
                   hover_color = "beige",
                   text = " ",
                   border_width = 1.5,
                   border_color = "#a06553"
                   )
#---------------------------TEXTOS---------------------------
data = CTkLabel(master = card_data_frame, 
                text = "DATA CARD",
                text_color = "black",
                font = (font_1, 20),
                width = 0.3,
                height = 0.3,
                bg_color = "transparent"
                )
summary = CTkLabel(master = purchase_summary_frame,
                                text = "PURCHASE SUMMARY",
                                text_color = "black",
                                font = (font_1, 20),
                                width = 0.3,
                                height = 0.3,
                                bg_color = "transparent"
                                )
date = CTkLabel(master = card_data_frame,
                text = "Expiration date",
                text_color = "black",
                font = (font_1, 12),
                width = 0.3,
                height = 0.3,
                bg_color = "transparent"
                )
text_departure_time = CTkLabel(master = option1, 
                            text = departure_time,
                            fg_color = "beige",
                            text_color = "black",
                            font = (font_1, 15),
                            width = 0.3,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_arrival_time = CTkLabel(master = option1, 
                            text = arrival_time,
                            fg_color = "beige",
                            text_color = "black",
                            font = (font_1, 15),
                            width = 0.3,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_departure_place = CTkLabel(master = option1, 
                            text = departure_place,
                            fg_color = "Beige",
                            text_color = "black",
                            font = (font_1, 11),
                            width = 0.3,
                            height = 0.3,
                            corner_radius = 10,
                            bg_color = "beige"
                            )
text_arrival_place = CTkLabel(master = option1, 
                            text = arrival_place,
                            fg_color = "Beige",
                            text_color = "black",
                            font = (font_1, 11),
                            width = 0.3,
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
                      width = 0.08,
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
                        font = ("roboto", 14),
                        width = 0.3,
                        height = 0.3,
                        bg_color = "beige"
                        )
text_total_to_pay = CTkLabel(master = purchase_summary_frame,
                             text = f"Total to pay: COP ${price}",
                             fg_color = "beige",
                             text_color = "black",
                             font = (font_1, 20),
                             width = 0.3,
                             height = 0.3,
                             bg_color = "beige"
                             )
text_category = CTkLabel(master = option1,
                         text = category,
                         fg_color = "#a06553",
                         text_color = "white",
                         font = (font_1, 13),
                         width = 10,
                         height = 25,
                         corner_radius = 10,
                         bg_color = "transparent"
                         )
#---------------------------POSICIONAMIENTO---------------------------
principal_frame.place(relx = 0.5, rely = 0.5, anchor = "center")
card_data_frame.place(relx = 0.24, rely = 0.45, anchor = "center")
purchase_summary_frame.place(relx = 0.733, rely = 0.45, anchor = "center")
data.place(relx = 0.5, rely = 0.1, anchor = "center")
titular_name.place(relx = 0.5, rely = 0.3, anchor = "center")
card_number.place(relx = 0.5, rely = 0.5, anchor = "center")
date.place(relx = 0.158, rely = 0.72, anchor = "center")
month_.place(relx = 0.2, rely = 0.8, anchor = "center")
year.place(relx = 0.5, rely = 0.8, anchor = "center")
ccv.place(relx = 0.8, rely = 0.8, anchor = "center")
summary.place(relx = 0.5, rely = 0.1, anchor = "center")
pay.place(relx = 0.5, rely = 0.93, anchor = "center")
option1.place(relx = 0.5, rely = 0.3, anchor = "center")
text_departure_time.place(relx = 0.08, rely = 0.37, anchor = "center")
text_departure_place.place(relx = 0.08, rely = 0.57, anchor = "center")
text_arrow.place(relx = 0.24, rely = 0.42, anchor = "center")
text_arrival_time.place(relx = 0.4, rely = 0.37, anchor = "center")
text_arrival_place.place(relx = 0.4, rely = 0.57, anchor = "center")
text_desde.place(relx = 0.583, rely = 0.45, anchor = "center")
text_price.place(relx = 0.743, rely = 0.615, anchor = "center")
text_category.place(relx = 0.88, rely = 0.3, anchor = "center")
text_total_to_pay.place(relx = 0.6, rely = 0.9, anchor = "center")

root8.mainloop() 
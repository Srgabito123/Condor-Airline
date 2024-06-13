import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox
import WINDOW_4
#ventana 8
def initialize_root7():
     
     root7 = ctk.CTk()
     root7.title("CONDOR-AIRLINES")
     root7._set_appearance_mode("light")
     root7.geometry("1000x600")
     root7.resizable(0,0)
     root7.config(bg = "#d7bb9f")
     root7.iconbitmap("images/ICONO.ico")

     def switch_to_root8(): 
          characters_16 = str(card_number.get())
          characters_3 = str(ccv.get())
          error_card = 0
          error_ccv = 0
          for i in characters_16:
               if i not in "0123456789":
                    error_card += 1
          for j in characters_3:     
               if j not in "0123456789":
                    error_ccv += 1

          if error_card != 0 or error_ccv != 0:
               messagebox.showerror("ERROR", "Ingrese solamente números en los campos")
               return
          if len(characters_16) != 16:
               messagebox.showerror("ERROR", "Ingrese un número de tarjeta válido")
               return
          if len(characters_3) != 3:
               messagebox.showerror("ERROR", "Ingrese un número de CCV válido")
               return
          
          else:
               root7.destroy()
               import WINDOW_8
               WINDOW_8.initialize_root8()
     #---------------------------VARIABLES---------------------------
     
     arrival_time = WINDOW_4.landing_hour_f
     departure_time = WINDOW_4.takeoff_hour_f
     departure_place = WINDOW_4.exit_city_f
     arrival_place = WINDOW_4.coming_city_f
     going = f"Ida: {departure_place} - {arrival_place}"
     price = WINDOW_4.price_f
     arrow = "---------------------->"
     category = "Aluminio"
     font_1 = ctk.CTkFont(family="Inherit", size=18, weight="bold")
     month = ["Enero", 
               "Febrero", 
               "Marzo", 
               "Abril", 
               "May0", 
               "Junio", 
               "Julio", 
               "Agosto", 
               "Septiembre", 
               "Octubre", 
               "Noviembre", 
               "Diciembre"]
     years = ["2024", "2025", "2026", "2027", "2028", "2029", "2030","2031", "2032", "2033", "2034", "2035"]
     #---------------------------FRAMES---------------------------
     principal_frame = ctk.CTkFrame(master = root7, 
                              width = 1000, 
                              height = 600, 
                              corner_radius = 10, 
                              fg_color = "#d7bb9f", 
                              border_color = "white", 
                              border_width = 2, 
                              bg_color = "transparent"
                              )
     card_data_frame = ctk.CTkFrame(master = principal_frame,
                                   width = 450,
                                   height = 460,
                                   corner_radius = 10,
                                   fg_color = "beige",
                                   border_color = "#a06553",
                                   border_width = 2,
                                   bg_color = "transparent"
                                   )
     purchase_summary_frame = ctk.CTkFrame(master = principal_frame,
                                   width = 500,
                                   height = 460,
                                   corner_radius = 10,
                                   fg_color = "beige",
                                   border_color = "#a06553",
                                   border_width = 2,
                                   bg_color = "transparent"
                                   )
     #---------------------------COMBOBOXES---------------------------
     month_ = ctk.CTkComboBox(master = card_data_frame,
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
     year = ctk.CTkComboBox(master = card_data_frame,
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
     titular_name = ctk.CTkEntry(master = card_data_frame,
                         width = 400,
                         height = 50,
                         border_color = "#a06553",
                         border_width = 1.5,
                         fg_color = "beige",
                         text_color = "black",
                         bg_color = "transparent",
                         placeholder_text = "Nombre del titular",
                         placeholder_text_color = "#a06553",
                         font = (font_1, 16)
                         )
     card_number = ctk.CTkEntry(master = card_data_frame,
                         width = 400,
                         height = 50,
                         border_color = "#a06553",
                         border_width = 1.5,
                         fg_color = "beige",
                         text_color = "black",
                         bg_color = "transparent",
                         placeholder_text = "Número de tarjeta",
                         placeholder_text_color = "#a06553",
                         font = (font_1, 16)
                         )
     ccv = ctk.CTkEntry(master = card_data_frame, 
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
     pay = ctk.CTkButton(master = principal_frame,
                    text = "PAGAR",
                    text_color = "white",
                    font = (font_1, 16, "bold"),
                    width = 80,
                    height = 15,
                    bg_color = "transparent",
                    fg_color = "#a06553",
                    border_color = "beige",
                    border_width = 1.5,
                    hover_color = "beige", 
                    command= switch_to_root8
                    )
     option1 = ctk.CTkButton(master = purchase_summary_frame, 
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
     data = ctk.CTkLabel(master = card_data_frame, 
                    text = "DATOS DE LA TARJETA",
                    text_color = "black",
                    font = (font_1, 20),
                    width = 0.3,
                    height = 0.3,
                    bg_color = "transparent"
                    )
     summary = ctk.CTkLabel(master = purchase_summary_frame,
                                   text = "RESUMEN DE COMPRA",
                                   text_color = "black",
                                   font = (font_1, 20),
                                   width = 0.3,
                                   height = 0.3,
                                   bg_color = "transparent"
                                   )
     date = ctk.CTkLabel(master = card_data_frame,
                    text = "Fecha de expiración",
                    text_color = "black",
                    font = (font_1, 12),
                    width = 0.3,
                    height = 0.3,
                    bg_color = "transparent"
                    )
     text_departure_time = ctk.CTkLabel(master = option1, 
                              text = departure_time,
                              fg_color = "beige",
                              text_color = "black",
                              font = (font_1, 15),
                              width = 0.3,
                              height = 0.3,
                              corner_radius = 10,
                              bg_color = "beige"
                              )
     text_arrival_time = ctk.CTkLabel(master = option1, 
                              text = arrival_time,
                              fg_color = "beige",
                              text_color = "black",
                              font = (font_1, 15),
                              width = 0.3,
                              height = 0.3,
                              corner_radius = 10,
                              bg_color = "beige"
                              )
     text_departure_place = ctk.CTkLabel(master = option1, 
                              text = departure_place,
                              fg_color = "Beige",
                              text_color = "black",
                              font = (font_1, 11),
                              width = 0.3,
                              height = 0.3,
                              corner_radius = 10,
                              bg_color = "beige"
                              )
     text_arrival_place = ctk.CTkLabel(master = option1, 
                              text = arrival_place,
                              fg_color = "Beige",
                              text_color = "black",
                              font = (font_1, 11),
                              width = 0.3,
                              height = 0.3,
                              corner_radius = 10,
                              bg_color = "beige"
                              )
     text_desde = ctk.CTkLabel(master = option1,
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
     text_price = ctk.CTkLabel(master = option1, 
                         text = price, 
                         fg_color = "beige", 
                         text_color = "black", 
                         font = (font_1, 11), 
                         width = 0.1, 
                         height = 0.3, 
                         corner_radius = 10, 
                         bg_color = "beige"
                         )
     text_arrow = ctk.CTkLabel(master = option1,
                         text = arrow,
                         fg_color = "beige",
                         text_color = "black",
                         font = ("roboto", 14),
                         width = 0.3,
                         height = 0.3,
                         bg_color = "beige"
                         )
     text_total_to_pay = ctk.CTkLabel(master = purchase_summary_frame,
                              text = f"Total a pagar: COP ${price}",
                              fg_color = "beige",
                              text_color = "black",
                              font = (font_1, 20),
                              width = 0.3,
                              height = 0.3,
                              bg_color = "beige"
                              )
     text_category = ctk.CTkLabel(master = option1,
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
     text_arrow.place(relx = 0.245, rely = 0.42, anchor = "center")
     text_arrival_time.place(relx = 0.42, rely = 0.37, anchor = "center")
     text_arrival_place.place(relx = 0.42, rely = 0.57, anchor = "center")
     text_desde.place(relx = 0.583, rely = 0.45, anchor = "center")
     text_price.place(relx = 0.743, rely = 0.615, anchor = "center")
     text_category.place(relx = 0.88, rely = 0.3, anchor = "center")
     text_total_to_pay.place(relx = 0.6, rely = 0.9, anchor = "center")

     root7.mainloop() 
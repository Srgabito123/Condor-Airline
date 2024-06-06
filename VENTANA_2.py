import customtkinter as ctk
from PIL import Image, ImageTk

#--------------------------------FUNCIONES---------------------------------------

def buscar():
    pass

#--------------------------------VENTANA 2---------------------------------------

ventana2 = ctk.CTk()
ventana2.resizable(0, 0)

screen_width = ventana2.winfo_screenwidth()
screen_height = ventana2.winfo_screenheight()
window_width = 1000
window_height = 600

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

ventana2.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
ventana2.config(background="#d7bb9f")
ventana2.title("Mapaula airline")

#-------------------------VARIBLES OPTION MENUS----------------------------------

opciones_ida_vuelta = ["Solo ida", "Ida y vuelta"] #Valores
valor_idavuelta = ctk.StringVar() #Tipo de variable
valor_idavuelta.set(opciones_ida_vuelta[0]) #Valor por defecto

ciudades_origen = ["Bogotá (BOG)", "Medellin (MDE)", "Santa Marta (SMR)", "Cali (CLO)", "Cartagena (CTG)"] 
valor_origen = ctk.StringVar() 
valor_origen.set(ciudades_origen[0]) 

ciudades_destino = ["Bogotá (BOG)", "Medellin (MDE)", "Santa Marta (SMR)", "Cali (CLO)", "Cartagena (CTG)"] 
valor_destino = ctk.StringVar() 

fechas_ida = ["5/06/2024", 
              "6/06/2024", 
              "12/06/2024", 
              "13/06/2024", 
              "19/06/2024", 
              "20/06/2024", 
              "26/06/2024", 
              "27/06/2024"]
valor_fechas = ctk.StringVar() 
valor_fechas.set(fechas_ida[0])

#----------------------------------FRAMES----------------------------------------

frame_1 = ctk.CTkFrame(ventana2,
                      bg_color="#d7bb9f", 
                      fg_color = "#d7bb9f", 
                      width = 860, 
                      height = 400, 
                      border_color = "beige", 
                      border_width = 4,
                      corner_radius = 15
                      )

roundtrip_frame = ctk.CTkFrame(ventana2, 
                      fg_color = "#d7bb9f",
                      bg_color = "#d7bb9f", 
                      width = 257, 
                      height = 57, 
                      border_color = "#a06553", 
                      border_width = 3,
                      corner_radius = 3
                      )

amountpeople_frame = ctk.CTkFrame(ventana2, 
                      fg_color = "#d7bb9f",
                      bg_color = "#d7bb9f", 
                      width = 77, 
                      height = 56, 
                      border_color = "#a06553", 
                      border_width = 3,
                      corner_radius = 3
                      )

origin_frame = ctk.CTkFrame(ventana2, 
                      fg_color = "#d7bb9f",
                      bg_color = "#d7bb9f", 
                      width = 226, 
                      height = 73, 
                      border_color = "#a06553", 
                      border_width = 3,
                      corner_radius = 3
                      )

destination_frame = ctk.CTkFrame(ventana2, 
                      fg_color = "#d7bb9f",
                      bg_color = "#d7bb9f", 
                      width = 226, 
                      height = 73, 
                      border_color = "#a06553", 
                      border_width = 3,
                      corner_radius = 0
                      )

dateflight_frame = ctk.CTkFrame(ventana2, 
                      fg_color = "#d7bb9f",
                      bg_color = "#d7bb9f", 
                      width = 226, 
                      height = 73, 
                      border_color = "#a06553", 
                      border_width = 3,
                      corner_radius = 0
                      )

image_frame = ctk.CTkFrame(ventana2, 
                           fg_color="beige",
                           bg_color="#d7bb9f", 
                           corner_radius = 2,
                           border_width = 3, 
                           border_color = "beige"
                           )

linea_divisora = ctk.CTkFrame(ventana2, 
                      fg_color = "#d7bb9f", 
                      width = 860, 
                      height = 12,
                      corner_radius = 0,
                      border_color = "beige", 
                      border_width = 4
                      )

#--------------------------------------IMÁGEN----------------------------------------

icon_image = Image.open("D:/GABO/2024/UNIVERSIDAD/SEMESTRE 1/FUNDAMENTOS DE PROGRAMACIÓN IMPERATIVA/PROYECTO FINAL/Repositorio/PERSONAS.png")
icon_image = icon_image.resize((20, 20), Image.Resampling.LANCZOS)
icon_photo = ImageTk.PhotoImage(icon_image)

#----------------------------------OPTION MENUS----------------------------------------

roundtrip_optionmenu = ctk.CTkOptionMenu(ventana2, 
                                        variable = valor_idavuelta, 
                                        values = opciones_ida_vuelta,
                                        width = 250,
                                        height=50,
                                        font=("Poppins", 16),
                                        text_color = "brown",
                                        bg_color = "#a06553",
                                        fg_color = "beige",
                                        cursor = "hand2",
                                        button_color = "beige",
                                        button_hover_color = "#a06553",
                                        dropdown_font = ("Poppins", 16),
                                        dropdown_text_color = "brown",
                                        dropdown_hover_color = "#a06553",
                                        dropdown_fg_color = "beige",
                                        corner_radius = 2
                                        )

origin_optionmenu = ctk.CTkOptionMenu(ventana2, 
                                        variable = valor_origen, 
                                        values = ciudades_origen,
                                        width = 220,
                                        height=50,
                                        font=("Poppins", 16),
                                        text_color = "brown",
                                        bg_color = "beige",
                                        fg_color = "beige",
                                        cursor = "hand2",
                                        button_color = "beige",
                                        button_hover_color = "#a06553",
                                        dropdown_font = ("Poppins", 16),
                                        dropdown_text_color = "brown",
                                        dropdown_hover_color = "#a06553",
                                        dropdown_fg_color = "beige",
                                        corner_radius = 2
                                        )

destination_optionmenu = ctk.CTkOptionMenu(ventana2, 
                                        variable = valor_destino, 
                                        values = ciudades_destino,
                                        width = 220,
                                        height=50,
                                        font=("Poppins", 16),
                                        text_color = "brown",
                                        bg_color = "beige",
                                        fg_color = "beige",
                                        cursor = "hand2",
                                        button_color = "beige",
                                        button_hover_color = "#a06553",
                                        dropdown_font = ("Poppins", 16),
                                        dropdown_text_color = "brown",
                                        dropdown_hover_color = "#a06553",
                                        dropdown_fg_color = "beige",
                                        corner_radius = 2
                                        )

dateflight_optionmenu = ctk.CTkOptionMenu(ventana2, 
                                        variable = valor_fechas, 
                                        values = fechas_ida,
                                        width = 220,
                                        height=50,
                                        font=("Poppins", 16),
                                        text_color = "brown",
                                        bg_color = "beige",
                                        fg_color = "beige",
                                        cursor = "hand2",
                                        button_color = "beige",
                                        button_hover_color = "#a06553",
                                        dropdown_font = ("Poppins", 16),
                                        dropdown_text_color = "brown",
                                        dropdown_hover_color = "#a06553",
                                        dropdown_fg_color = "beige",
                                        corner_radius = 2
                                        )

#--------------------------------------CAJAS DE TEXTO----------------------------------------

amountpeople_textbox = ctk.CTkEntry(image_frame, 
                     width = 40,  
                     height = 50,  
                     fg_color="beige", 
                     border_width=0, 
                     font=("Poppins", 14, "bold")
                     )

#-----------------------------------LABELS----------------------------------------

icon_people_label = ctk.CTkLabel(image_frame, 
                                   image=icon_photo, 
                                   text="", 
                                   fg_color="beige",
                                   height = 30
                                   )

origin_label = ctk.CTkLabel(ventana2, 
                            text = "Origen",
                            width = 220,
                            height = 16,
                            font=("Poppins", 12), 
                            text_color = "brown",
                            fg_color = "beige", 
                            bg_color = "#d7bb9f",
                            anchor = "w"
                            )

destination_label = ctk.CTkLabel(ventana2, 
                            text = "Destino",
                            width = 220,
                            height = 16,
                            font=("Poppins", 12), 
                            text_color = "brown",
                            fg_color = "beige", 
                            bg_color = "#d7bb9f",
                            anchor = "w"
                            )

dateflight_label = ctk.CTkLabel(ventana2, 
                            text = "Fecha ida",
                            width = 220,
                            height = 16,
                            font=("Poppins", 12), 
                            text_color = "brown",
                            fg_color = "beige", 
                            bg_color = "#d7bb9f",
                            anchor = "w"
                            )

#------------------------------------BOTON----------------------------------------

boton_buscar = ctk.CTkButton(ventana2, 
                      text="Buscar",
                      text_color="white", 
                      width=150, 
                      height=40,
                      font=("Poppins", 16, "bold"),
                      bg_color="#d7bb9f",
                      fg_color="#a06553",
                      cursor="hand2",
                      hover_color="lightblue",
                      command = buscar)

#----------------------------------POSICIONAMIENTO----------------------------------------

frame_1.place(x = 70, y = 70)
roundtrip_frame.place(x = 97, y = 105)
amountpeople_frame.place(x = 797, y = 104.8)
origin_frame.place(x = 97, y = 241)
destination_frame.place(x = 320, y = 241)
dateflight_frame.place(x = 647, y = 241)
linea_divisora.place(x = 70, y = 190)
roundtrip_optionmenu.place(x = 100, y = 108)
image_frame.place(x = 800, y = 108)
amountpeople_textbox.grid(row=0, column=1, sticky="nsew", padx=(0, 5))
icon_people_label.grid(row=0, column=0, sticky="nsew", padx=(5, 0))
origin_label.place(x = 100, y = 244)
destination_label.place(x = 323, y = 244)
origin_optionmenu.place(x = 100, y = 260)
destination_optionmenu.place(x = 323, y = 260)
dateflight_optionmenu.place(x = 650, y = 260)
dateflight_label.place(x = 650, y = 244)
boton_buscar.place(x=425, y=370)

ventana2.mainloop()
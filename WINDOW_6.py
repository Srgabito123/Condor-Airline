import customtkinter as ctk

def initialize_root6(category):
    #--------------------------------------FUNCIONES---------------------------------------

    def switch_to_root7(category): 
        root6.destroy()
        import WINDOW_7
        WINDOW_7.initialize_root7(category)

    def is_seat_selected(row, col):
        seat = (row, col)
        button = seat_buttons[row][col]
        if seat in selected_seats:
            selected_seats.remove(seat)
            button.configure(fg_color="beige")
        else:
            selected_seats.add(seat)
            button.configure(fg_color="#a06553")

    #--------------------------------------VENTANA3----------------------------------------

    root6 = ctk.CTk()
    root6.resizable(0, 0)

    screen_width = root6.winfo_screenwidth()
    screen_height = root6.winfo_screenheight()
    window_width = 1000
    window_height = 600

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root6.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
    root6.config(background="#d7bb9f")
    root6.title("CONDOR-AIRLINES")
    root6.iconbitmap("images/ICONO.ico")

    #---------------------------------------FRAMES-----------------------------------------

    outside_line = ctk.CTkFrame(root6, 
                                width=860, 
                                height=515,
                                bg_color="#d7bb9f",
                                fg_color="#d7bb9f",
                                corner_radius=20,
                                border_color="beige",
                                border_width=4
                                )

    text_frame = ctk.CTkFrame(root6, 
                            width=230, 
                            height=40,
                            bg_color="#d7bb9f",
                            fg_color="beige",
                            corner_radius=25
                            )

    seatsbutton_frame = ctk.CTkFrame(root6,
                                width=320, 
                                height=420,
                                bg_color="#d7bb9f",
                                fg_color="beige",
                                corner_radius=20
                                )

    premium_zone_frame = ctk.CTkFrame(seatsbutton_frame, 
                                width=300, 
                                height=133,
                                bg_color="beige",
                                fg_color="#ddbdb2",
                                corner_radius=4
                                )

    diamond_zone_frame = ctk.CTkFrame(seatsbutton_frame, 
                                width=300, 
                                height=133,
                                bg_color="beige",
                                fg_color="#d2a798",
                                corner_radius=4
                                )


    plata_zone_frame = ctk.CTkFrame(seatsbutton_frame, 
                                width=300, 
                                height=133,
                                bg_color="beige",
                                fg_color="#c7917e",
                                corner_radius=4
                                )

    premium_frame = ctk.CTkFrame(root6, 
                                width=150, 
                                height=40,
                                bg_color="#d7bb9f",
                                fg_color="#ddbdb2",
                                corner_radius=5,
                                border_color="#b38371",
                                border_width=3
                                )

    diamante_frame = ctk.CTkFrame(root6, 
                                width=150, 
                                height=40,
                                bg_color="#d7bb9f",
                                fg_color="#d2a798",
                                corner_radius=5,
                                border_color="#b38371",
                                border_width=3
                                )

    plata_frame = ctk.CTkFrame(root6, 
                                width=150, 
                                height=40,
                                bg_color="#d7bb9f",
                                fg_color="#c7917e",
                                corner_radius=5,
                                border_color="#b38371",
                                border_width=3
                                )

    #---------------------------------------LABELS---------------------------------------

    letter_seats_text = ctk.CTkLabel(root6, 
                                text=" A         B          C          D          E          F  ", 
                                font=("Poppins", 16),
                                text_color="brown",
                                bg_color="#d7bb9f",
                                fg_color="beige",
                                width = 260,
                                corner_radius=5
                                )

    seats_text = ctk.CTkLabel(text_frame, 
                                text="SELECCIÓN DE ASIENTOS", 
                                font=("Poppins", 18),
                                text_color="brown",
                                bg_color="beige",
                                fg_color="beige",
                                corner_radius=15
                                )

    premium_label = ctk.CTkLabel(premium_frame, 
                                text="Premium", 
                                font=("Poppins", 16, "bold"),
                                text_color="white",
                                bg_color="#d7bb9f",
                                fg_color="#ddbdb2",
                                corner_radius=5
                                )

    diamante_label = ctk.CTkLabel(diamante_frame, 
                                text="Diamante", 
                                font=("Poppins", 16, "bold"),
                                text_color="white",
                                bg_color="#d7bb9f",
                                fg_color="#d2a798",
                                corner_radius=5
                                )

    plata_label = ctk.CTkLabel(plata_frame, 
                                text="Plata", 
                                font=("Poppins", 16, "bold"),
                                text_color="white",
                                bg_color="#d7bb9f",
                                fg_color="#c7917e",
                                corner_radius=5
                                )

    #---------------------------------------BOTONES---------------------------------------

    select_button = ctk.CTkButton(root6, 
                                    text="Seleccionar",
                                    text_color="white", 
                                    width=150, 
                                    height=40,
                                    font=("Poppins", 16, "bold"),
                                    bg_color="#d7bb9f",
                                    fg_color="#a06553",
                                    cursor="hand2",
                                    border_width=3,
                                    border_color="beige",
                                    hover_color="lightblue",
                                    command=lambda: switch_to_root7(category)
                                    )

    seat_buttons = []
    selected_seats = set()
    rows = 12
    columns = 6

    def disable_all_buttons():
        for row_buttons in seat_buttons:
            for button in row_buttons:
                button.configure(state="disabled")

    def is_seat_selected(row, col):
        print(f"Asiento seleccionado: Fila {row}, Columna {col}")

        seat_buttons[row][col].configure(fg_color="yellow")  
        disable_all_buttons()

    for row in range(rows):
        row_buttons = []
        for col in range(columns):
            if row < 4:
                button = ctk.CTkButton(premium_zone_frame,
                                    width=22,
                                    height=22,
                                    text="",
                                    command=lambda row=row, col=col: is_seat_selected(row, col),
                                    fg_color="beige",
                                    hover_color="gray",
                                    border_color="#a06553",
                                    border_width=2)
                button.grid(row=row, column=col, padx=14, pady=8, sticky="nsew")
            elif row < 8:
                button = ctk.CTkButton(diamond_zone_frame,
                                    width=22,
                                    height=22,
                                    text="",
                                    command=lambda row=row, col=col: is_seat_selected(row, col),
                                    fg_color="beige",
                                    hover_color="gray",
                                    border_color="#a06553",
                                    border_width=2)
                button.grid(row=row-4, column=col, padx=14, pady=8, sticky="nsew")
            else:
                button = ctk.CTkButton(plata_zone_frame,
                                    width=22,
                                    height=22,
                                    text="",
                                    command=lambda row=row, col=col: is_seat_selected(row, col),
                                    fg_color="#a06553",
                                    hover_color="#a06553",
                                    border_color="#a06553",
                                    border_width=2)
                button.grid(row=row-8, column=col, padx=14, pady=8, sticky="nsew")
            row_buttons.append(button)
        seat_buttons.append(row_buttons)

    

    #------------------------------------POSICIONAMIENTO----------------------------------------

    outside_line.place(x=70, y = 25)
    text_frame.place(x=-20, y = 15)
    letter_seats_text.place(x=308, y = 60)
    seats_text.pack(fill="both", expand=True, pady = 10, padx = 10)
    seatsbutton_frame.place(x=290, y = 80)
    premium_zone_frame.grid(row= 0, column = 0, padx = 10, pady = 10)
    diamond_zone_frame.grid(row = 1, column = 0)
    plata_zone_frame.grid(row = 2, column = 0, padx = 10, pady = 10)
    premium_frame.place(x=635, y=142)
    diamante_frame.place(x=635, y=280)
    plata_frame.place(x=635, y=428)
    premium_label.pack(fill="both", expand=True, pady=5, padx=5)
    diamante_label.pack(fill="both", expand=True, pady=5, padx=5)
    plata_label.pack(fill="both", expand=True, pady=5, padx=5)
    select_button.place(x=790, y=515)

    root6.mainloop()


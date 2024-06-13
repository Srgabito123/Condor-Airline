import tabulate as tb
import WINDOW_2
import WINDOW_5

#--------------------------------------SACAR DATOS DEL TXT------------------------------------
file = open("Datos_Vuelos _Finales.txt", 'r')

matriz = []

for line in file:
    linea_final = line.replace("[", "").replace("]", "").replace("'", "").replace("\n", "")
    lista = linea_final.split(", ")
    lista = [element.strip() for element in lista]
    matriz.append(lista)


def recive_data(origin, destiny, date):
    global flights, departure_hour, arrival_hour, price, all_dates, mid_price, max_price, min_price, takeoff_hour, landing_hour, exit_city, coming_city, flight_code, flight_date_

    flights = []
    all_flights = []
    for i in range(len(matriz)):

        if matriz[i][7] == origin and matriz[i][8] == destiny:
            all_flights.append(matriz[i])

        if matriz[i][7] == origin and matriz[i][8] == destiny and matriz[i][1] == date:
                flights.append(matriz[i])
    
    all_dates = set()

    for i in range(len(all_flights)):
        all_dates.add(all_flights[i][1])

    
    all_dates = list(all_dates)

    departure_hour = [flights[i][2] for i in range(len(flights))]
    arrival_hour = [flights[i][3] for i in range(len(flights))]
    price = [flights[i][4] for i in range(len(flights))]

    min_price = [flights[i][4] for i in range(len(flights))]
    mid_price = [flights[i][5] for i in range(len(flights))]
    max_price = [flights[i][6] for i in range(len(flights))]

    takeoff_hour = [flights[i][2] for i in range(len(flights))]
    landing_hour = [flights[i][3] for i in range(len(flights))]
    exit_city = [flights[i][7] for i in range(len(flights))]
    coming_city = [flights[i][8] for i in range(len(flights))]

    flight_code = [flights[i][0] for i in range(len(flights))]
    flight_date_ = [flights[i][1] for i in range(len(flights))]
 

    #print(tb.tabulate(prices))
    #print(tb.tabulate(flights))


       
#--------------------------------------VARIABLES------------------------------------

origin_city = set(matriz[i][7] for i in range(1, len(matriz)))
destiny_city = set(matriz[i][8] for i in range(1, len(matriz)))
departure_date = set(matriz[i][1] for i in range(1, len(matriz)))

origin_city = list(origin_city)
destiny_city = list(destiny_city)
departure_date = list(departure_date)

file.close()



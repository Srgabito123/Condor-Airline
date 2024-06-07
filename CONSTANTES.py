import tabulate as tb
import WINDOW_2

#--------------------------------------SACAR DATOS DEL TXT------------------------------------
file = open("Datos_Vuelos _Finales.txt", 'r')

matriz = []

for line in file:
    linea_final = line.replace("[", "").replace("]", "").replace("'", "").replace("\n", "")
    lista = linea_final.split(", ")
    lista = [element.strip() for element in lista]
    matriz.append(lista)

#print(tb.tabulate(matriz))

def recive_data(origin, destiny, date):
    global flights
    flights = []

    for i in range(len(matriz)):
        if matriz[i][7] == origin and matriz[i][8] == destiny and matriz[i][1] == date:
                flights.append(matriz[i])



       
#--------------------------------------VARIABLES------------------------------------

origin_city = set(matriz[i][7] for i in range(1, len(matriz)))
destiny_city = set(matriz[i][8] for i in range(1, len(matriz)))
departure_date = set(matriz[i][1] for i in range(1, len(matriz)))

origin_city = list(origin_city)
destiny_city = list(destiny_city)
departure_date = list(departure_date)

file.close()



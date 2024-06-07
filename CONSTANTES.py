import tabulate as tb

#--------------------------------------SACAR DATOS DEL TXT------------------------------------
file = open("Datos_Vuelos _Finales.txt", 'r')

matriz = []

for line in file:
    linea_final = line.replace("[", "").replace("]", "").replace("'", "").replace("\n", "")
    lista = linea_final.split(", ")
    lista = [element.strip() for element in lista]
    matriz.append(lista)

#print(tb.tabulate(matriz))
#--------------------------------------VARIABLES------------------------------------

origin_city = set(matriz[i][7] for i in range(1, len(matriz)))
destiny_city = set(matriz[i][8] for i in range(1, len(matriz)))
departure_date = set(matriz[i][1] for i in range(1, len(matriz)))

origin_city = list(origin_city)
destiny_city = list(destiny_city)
departure_date = list(departure_date)

file.close()

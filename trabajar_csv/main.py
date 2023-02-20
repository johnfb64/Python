#forma sencilla de guardar los valores csv en un arreglo
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

#usando la libreria csv
# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for fila in data:
#         if fila[1] != "temp":
#             temperatures.append(int(fila[1]))
#     print(temperatures)

print("----PRESENTACIÓN DE ARCHIVO CSV Y EXTRACCIÓN COLUMNA POR ENCABEZADO-------")
import pandas
data = pandas.read_csv("weather_data.csv")
print(data)
print("---------------------")
print(data["temp"])
print("----CONVERSION ARCHIVO A DICCIONARIO-------")
#Conceptos: Pandas core data frame -> Hace referencia a toda la tabla.
#Pandas series object = a una singular columna.
#Convertir a diccionario:
data_dict = data.to_dict()
print(data_dict)
#Documentación series pandas: andas.pydata.org/docs/reference/api/pandas.Series.html
#convertido a lista la columna de temperatura:
print("----CONVERSION A LISTA DE DICCIONARIO-------")
temp_list = data["temp"].to_list()
print(temp_list)
#promedio temperatura
print("----PROMEDIO TEMPERATURA-------")
avg_temp = sum(temp_list)/len(temp_list)
print(avg_temp)
max_val = data["temp"].max()
print(f"valor maximo de temperatura: {max_val}")
print("")
print("----FILTRANDO FILA-------")
#NOTESE QUE... el encabezado de columna se puede llamar como si fuera un metodo
#data.day, day es el encabezado de la columna.
print(data[data.day == "Monday"])
print("")
print("----COLUMNA CON EL DIA DE TEMPERATURA MAS ALTA-------")
print(data[data.temp == data.temp.max()])
#CREANDO UN DATAFRAME DE 0
print("")
print("----DATA FRAME CREADO DE 0's-------")
data_dicc = {
    "students": ["Amy","James","Angela"], "scores": [76, 56, 65]
}
datos = pandas.DataFrame(data_dicc)
print(datos)
print("")
print("----CREANDO ARCHIVO CSV-------")
datos.to_csv("nuevo_archivo.csv")







import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_squirrel = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel = len(data[data["Primary Fur Color"] == "Black"])
# print(grey_squirrel)
# print(cinnamon_squirrel)
# print(black_squirrel)

#Diccionario que ordena el dato de color de la ardilla
data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "count": [grey_squirrel,cinnamon_squirrel,black_squirrel]
}

#data frame = metodo DataFrame de pandas toma como parametro "data_dict"
#data_dict como ya se observo es el diccionario.
df = pandas.DataFrame(data_dict)
df.to_csv("contador_de_ardillas.csv")
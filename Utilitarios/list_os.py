import os
directorio = os.getcwd() #obtiene ruta actual

list_dir = []
folder = input("Agregue una ruta de carpeta: ")
class Carpetas:
    def __init__(self,carpeta):
        self.carpeta = folder
        list_dir = os.listdir(self.carpeta) #lista archivos carpeta
        for i in list_dir:
           print(i)



folder1 = Carpetas(folder)
print(folder1)





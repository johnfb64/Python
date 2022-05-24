#Usar una lista y acceder a los items del 0 al n.
import this


print("----------------ACCEDE A ITEMS---------------------------------")
mi_lista=["Perro","Loro","Gato","Vaca","Leon","Oso","Pantera"]
print(mi_lista[2])
print(mi_lista[2:5])
print(mi_lista[:5])
print(mi_lista[-1])
print("-----------------CAMBIA E INSERTA ITEMS--------------------------------")
#Cambiar listas de items

mi_lista[1]="Colibri"
print(mi_lista)
#Llama metodo insert
mi_lista.insert(3,"Pulpo")
print(mi_lista)

print("-----------------ADICIONA ITEMS--------------------------------")

mi_lista.append("Zorro")
print(mi_lista)

print("-----------------REMUEVE ITEMS--------------------------------")

mi_lista.remove("Vaca")
print(mi_lista)
mi_lista.pop(1)
print(mi_lista)
del mi_lista[0]
print(mi_lista)
#Clarear lista
mi_lista.clear()
print(mi_lista)

print("-----------------RECORRER LISTAS--------------------------------")
mi_lista=["Perro","Loro","Gato","Vaca","Leon","Oso","Pantera"]
#len cuenta la cantidad de items en la lista
for i in range(len(mi_lista)):
    print(mi_lista[i])


print("-----------------List Comprehension--------------------------------")
#Se crea una nueva lista la cual se llenara automaticamente
#for x recorre mi lista
#Si "o" esta en x (cada palabra que tenga o)
#Hara la indexación con append en new_list
new_list = []
for x in mi_lista:
    if "o" in x:
        new_list.append(x)

print(new_list)

print("---------------------------ORGANIZAR--------------------------------")
#Organiza alfanumericamente
mi_lista.sort()
print(mi_lista)
#Organiza descendiente
mi_lista.sort(reverse=True)
print(mi_lista)

print("---------------------------COPIAR LISTA--------------------------------")
lista_mamiferos = mi_lista.copy()
print(lista_mamiferos)

print("---------------------------UNION LISTAS--------------------------------")

lista_insectos = ["Abeja","Araña","Cucaracha","Grillo"]

lista_animales = lista_mamiferos + lista_insectos
print(lista_animales)
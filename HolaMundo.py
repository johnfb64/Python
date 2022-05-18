print("Hola mundo")

nombre = input("Introduce tu nombre: ")
edad = int(input("Que edad tienes?: "))
ano = (2022-edad)-1

print("Hola ", nombre, ", naciste en el año ", ano)

print("Ahora algo mas interesante...")
dec = input("Deseas ver una tabla de multiplicar? si/no: ")

if (dec == "si"):
    print("Genial!....")
    print("TABLA DE MULTIPLICAR")
    numMul = int(input("Ingresa un numero del 1 al 10: "))
    for i in range(11):
        res=i*numMul
        print(i,"x",numMul,"=",res)
elif (dec == "no"):
    print ("Ok, dejemos asi, Adios!")
else:
    print("No entendi la respuesta, igual termina aqui.")








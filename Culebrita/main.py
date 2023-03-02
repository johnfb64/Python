from turtle import Screen, Turtle
import time

#Esto llama al frame para poner la culebra, con marco 600x00 en fondo negro, titulo Culebrita
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Culebrita")
screen.tracer(0)
#Ubicación inicial de elementos.
starting_positions = [(0,0),(-20,0),(-40,0)]
segments = []

#For va creando nuevos objetos.
for position in starting_positions:
    #Esto es un segmento, turtle
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    #Este codigo agrega nuevos segmentos al arreglo segments.
    segments.append(new_segment)




game_is_on = True
while game_is_on:
    #update actualiza ventana de juego, a frames de 0.1.
    screen.update()
    time.sleep(0.1)
    #For actualiza la posición respecto a segments (el arreglo)
    for seg_num in range(len(segments) -1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x,new_y)
    #Con forward se mueve un segmento hacia adelante
    segments[0].forward(20)

screen.exitonclick()
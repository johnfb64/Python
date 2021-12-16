from MundoPC.Computadora import Computadora
from MundoPC.Monitor import Monitor
from MundoPC.Mouse import Mouse
from MundoPC.Orden import Orden
from MundoPC.Teclado import Teclado

mouse1 = Mouse('laser','HP')
teclado1 = Teclado('Mecanico','Redragon')
monitor1 = Monitor('Lenovo', '22 pulgadas')
pc1 = Computadora('PC Master Race', monitor1, teclado1, mouse1)
print(pc1)

mouse2 = Mouse('clasico', 'Logi')
teclado2 = Teclado('Membrana', 'Generico')
monitor2 = Monitor('Asus', '38 pulgadas')
pc2 = Computadora('Oficina', monitor2, teclado2, mouse2)
print(pc2)

computadoras1 = [pc1, pc2]

orden1 = Orden(computadoras1)
print(orden1)
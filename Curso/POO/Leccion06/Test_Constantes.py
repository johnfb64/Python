#Importación de constante desde Constantes.py
import Constantes
from Constantes import MI_CONSTANTE
#Renombrar importado
from Constantes import circunferencia_PI as PI

#Se llama a la constante definida en Constantes.py

print(MI_CONSTANTE)
#No se debe cambiar el valor de una constante, pero se puede hacer, recuerde que es convencionalidad.
#MI_CONSTANTE = 'Nuevo valor'
#print(MI_CONSTANTE)
print(PI.PI)




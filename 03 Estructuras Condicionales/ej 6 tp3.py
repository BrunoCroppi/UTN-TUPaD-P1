#escribir un programa que tome la lista
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
import random
from statistics import mode, mean, median
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
valorMode = mode (numeros_aleatorios)
valorMean = mean (numeros_aleatorios)
valorMedian = median (numeros_aleatorios)
print(f"Numeros: {numeros_aleatorios}")
print(f"Media: {mean}")
print(f"Mediana: {median}") 
print(f"Moda: {mode}")

if valorMode < valorMedian < valorMean:
    print("Sesgo positivo (asimetría a la derecha)")
elif valorMean < valorMedian < valorMode:
    print("Sesgo negativo (asimetría a la izquierda)")
else:
    print("No hay sesgo (distribución simétrica)")
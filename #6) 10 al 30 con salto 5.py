#6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
#pantalla los dos primeros.
lista = [i for i in range(10, 31, 5)] # Crear una lista con números del 10 al 30 con saltos de 5
print(lista[:2])  # Muestra los dos primeros elementos de la lista
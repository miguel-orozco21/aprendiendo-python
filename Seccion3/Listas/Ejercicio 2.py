"""
Calificaciones

~ Crea una lista con las calificaciones 8,9,7,10 y 6
~ Calcula e imprime el promedio, la calificacion más alta y la más baja.
~ Debe salir: 8.0, 10 y 6
"""

calificaciones = [8,9,7,10,6]
promedio = sum(calificaciones) / len(calificaciones)
print(promedio, max(calificaciones), min(calificaciones))


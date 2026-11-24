"""
Ejercicio 1: ficha de platillo
Crea un diccionario platillo con las llaves 'nombre' (tacos al pastor) 'precio' (18)
y porciones (50). Imprime el diccionario completo, luego solo el nombre, y luego el ingreso total
(precio por porciones) con el texto "ingreso total:".
"""

platillo = {
    "nombre": "Tacos al pastor",
    "precio": 18,
    "porciones": 50
}
# -- Impresiones --

#Diccionario completo
print(platillo)
#Nombre
print(platillo["nombre"])
#ingreso total
print("Ingreso total:", platillo["precio"] * platillo["porciones"])

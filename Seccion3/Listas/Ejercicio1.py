"""
Lista de compras

~ Crea una lista con 3 productos
~ Agregale un cuarto producto al final
~ Imprime el primer producto, el ultimo y cuantos productos hay
~ Practica: crear listas, append, indices, len
~ Debe salir: el primer producto, el ultimo (el que agregaste)  y el numero 4
"""

productos = ["Jabon", "Cereal", "Chocolate"]
print(productos)
productos.append("Rastrillo")
print(productos)
print(productos[0], productos[-1], len(productos))
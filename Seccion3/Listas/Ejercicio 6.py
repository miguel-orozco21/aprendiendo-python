"""
Cola y pila

Crea una lista vacía de pedidos y agrega 3 pedidos con append.
Atiende el primero que llegó: sácalo de la lista, guárdalo en
una variable e imprímelo junto con los pedidos que quedan.
Crea otra lista llamada historial con “escribir”, “borrar”, “pegar”.
Haz “deshacer”: saca el último elemento e imprime cuál fue y cómo
quedó el historial.
"""

pedidos = []

pedidos.append("Hamburguesa triple")
pedidos.append("Hamburguesa Clasica")
pedidos.append("Hamburguesa BBQ")

x = pedidos.pop(0)

print(pedidos)
print(x)

historial = ["escribir", "borrar", "pegar"]

historial.append("deshacer")

print(historial)
y = historial.pop()
print(y)
print(historial)

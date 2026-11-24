"""
Inventario
Pide con input el nombre de un producto y su cantidad (conviértela
a número) y agrégalo al inventario.
Con update, mete {"pera": 12, "mango": 7}.
Imprime el inventario.
Con get, imprime el stock de “sandia” usando 0 como valor por defecto.
Elimina “uva” con pop e imprime lo que devolvió.
Imprime cuántos productos quedaron.
"""

inventario = {"manzana": 10, "pera": 5, "uva": 8}

#input

producto = input("Producto: ")
cantidad = int(input("Cantidad: "))
inventario[producto] = cantidad

# agregar con update
inventario_nuevos = {"pera": 12, "mango": 7}
inventario.update(inventario_nuevos)
print(inventario)

#Get
print("Stock de sandia: ",inventario.get("sandia", 0))

#pop
quitar_uva = inventario.pop("uva")
print("Uvas eliminadas: ",quitar_uva)

#Impresion final
print("Productos en inventario: ", len(inventario))
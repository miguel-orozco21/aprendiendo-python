"""
Pedidos
1. A cada pedido agrégale la llave total (cantidad por precio), una por una.
2. Imprime la lista completa.
3. Agrega un cuarto pedido: Diego, Taco, cantidad 5, precio 15, con su total calculado.
4. Imprime la venta total sumando los 4 totales, el producto del último pedido (usa índice negativo) y cuántos pedidos hay.

"""

pedidos = [
    {"cliente" : "Ana", "producto": "Taco", "cantidad": 3, "precio": 15},
    {"cliente": "Beto", "producto": "Torta", "cantidad": 2, "precio": 40},
    {"cliente": "Carla", "producto": "Agua", "cantidad": 4, "precio": 20},
]

#1
pedidos[0]["total"] = pedidos[0]["cantidad"] * pedidos[0]["precio"]
pedidos[1]["total"] = pedidos[1]["cantidad"] * pedidos[1]["precio"]
pedidos[2]["total"] = pedidos[2]["cantidad"] * pedidos[2]["precio"]

#2
print(pedidos)

#3
pedido_nuevo = {"cliente": "Diego", "producto": "Taco", "cantidad": 5, "precio": 15}
pedidos.append(pedido_nuevo)
pedidos[3]["total"] = pedidos[3]["cantidad"] * pedidos[3]["precio"]

#4
venta_total = pedidos[0]["total"] + pedidos[1]["total"] + pedidos[2]["total"] + pedidos[3]["total"]
print(venta_total)
print("Ultimo producto:",pedidos[-1]["producto"])
print(len(pedidos))



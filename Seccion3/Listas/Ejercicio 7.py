"""
Crea una tabla (lista de listas) con tres filas:
Ana, 1200, norte / Luis, 850, sur / Sofia, 2300, norte.
Imprime el nombre y la venta de la fila 2.
Agrega una cuarta fila: Pedro, 990, sur.
Calcula el total vendido sumando la columna de ventas de las 4 filas.
Crea una lista solo con los montos y ordénala de mayor a menor
sin modificar la tabla.
"""

registro_de_ventas = [
    ["Ana", 1200, "norte"],
    ["Luis", 850, "sur"],
    ["Sofia", 2300, "norte"]
]

print(registro_de_ventas)
print(registro_de_ventas[1][0], registro_de_ventas[1][1])

registro_de_ventas.append(["Pedro", 990, "sur"])
print(registro_de_ventas)

total_ventas = registro_de_ventas[0][1] + registro_de_ventas[1][1] + registro_de_ventas[2][1] + registro_de_ventas[3][1]
print(total_ventas)

lista_montos = [registro_de_ventas[0][1], registro_de_ventas[1][1], registro_de_ventas[2][1], registro_de_ventas[3][1]]
print(sorted(lista_montos, reverse=True))



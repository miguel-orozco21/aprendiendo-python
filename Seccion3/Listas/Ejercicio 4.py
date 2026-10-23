"""
Reporte de ventas

~ Lista de ventas de 5 dias: 1200,850,2300,1500,990
~ Calcula e imprime: total, promedio, la mejor venta, en qué día fue
(contando el dia desde 1), las ventas de los días 2 al 4
y las 3 mejores ventas de mayor a menor.
"""


lista_ventas = [1200,850,2300,1500,990]


print("Total:", sum(lista_ventas))

print("Promedio:", sum(lista_ventas) / len(lista_ventas))

print("Mejor venta:", max(lista_ventas),  "Día:", lista_ventas.index(max(lista_ventas)) + 1)

print("Ventas día 2 al 4:", lista_ventas[1:4])

print("Las 3 mejores ventas:", sorted(lista_ventas, reverse=True)[:3])


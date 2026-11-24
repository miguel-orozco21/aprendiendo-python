"""
Empleados anidados
1. Imprime el nombre del empleado e2.
2. Sube 10% el sueldo de e1 y guárdalo en el mismo lugar.
3. Imprime el sueldo nuevo de e1.
4.Agrega a e2 la llave antiguedad con valor 3.
5. Imprime solo el diccionario de e2.
6. Imprime la lista de llaves de empleados.
"""

empleados = {
    "e1": {"nombre": "Marta", "puesto": "Cajera", "sueldo": 8000},
    "e2": {"nombre": "Jorge", "puesto": "Repartidor", "sueldo": 7000},
}

# 1
print(empleados["e2"]["nombre"])

# 2
empleados["e1"]["sueldo"] = empleados["e1"]["sueldo"] * 1.10

#3
print(empleados["e1"]["sueldo"])

#4
empleados["e2"]["antiguedad"] = 3

#5
print(empleados["e2"])

#6
print(list(empleados.keys()))




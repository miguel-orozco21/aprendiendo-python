"""

"""

#Texto a lista
linea = "id=101;nombre=Luis;depto=ventas;sueldo=9500"
partes = linea.split(";")

#Dic
registro = {
    "id": int(partes[0].split("=")[1]),
    "nombre": partes[1].split("="[1]),
    "depto": partes[2].split("=")[1],
    "sueldo": int(partes[3].split("=")[1]),
}
print(registro)

#
referencia = registro
referencia["depto"] = "compras"
print(registro)

#
copia = registro.copy()
copia["sueldo"] = 12000
print(registro)
print(copia)

#
sueldo_anual = registro["sueldo"] * 12
print(sueldo_anual)

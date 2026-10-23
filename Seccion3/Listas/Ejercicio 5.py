"""
Leer una linea de log

Parte de esta línea: “2026-10-19 14:32:10,ERROR,pagos,
Timeout al conectar”
Sepárala por comas y guarda en variables distintas: fecha, hora, nivel,
 módulo y mensaje.
 La fecha y la hora vienen juntas en el primer pedazo, así que ese
pedazo se tiene que separar otra vez, ahora por espacio.
Imprime las cinco variables.
"""

texto = "2026-10-19 14:32:10,ERROR,pagos,Timeout al conectar"
lista = texto.split(",")
fecha_y_hora = lista[0].split(" ")

fecha = fecha_y_hora[0]
hora = fecha_y_hora[1]
nivel = lista[1]
modulo = lista[2]
mensaje = lista[3]

print(fecha)
print(hora)
print(nivel)
print(modulo)
print(mensaje)


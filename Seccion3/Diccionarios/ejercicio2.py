"""
Ejercicio 2: Modificar un diccionario
Parte de alumno = {"nombre": "Ana", "semestre": 4}. En este orden:
agrega la llave carrera con “Informática”, cambia semestre a 5 y elimina nombre.
Imprime el diccionario después de cada cambio y al final imprime cuántas parejas tiene
"""

alumno = {"nombre": "Ana", "semestre": 4,}
print(alumno)
#Agrego carrera
alumno["carrera"] = "Informática"
print(alumno)
#Modifico semestre
alumno["semestre"] = 5
print(alumno)
#Elimino nombre
del alumno["nombre"]
print(alumno)
#Len
print(len(alumno))


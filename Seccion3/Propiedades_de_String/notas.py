# =========== PROPIEDADES DE LOS STRINGS ===========

#1. INMUTABLES: no puedes cambiar una parte, pero si reasignar la variable
palabra = "hola"
# palabra[0] = "H" #TypeError: no soporta asignación de ítems
palabra = "H" + palabra[1:] # Se crea un string nuevo y se reasigna
print(palabra) # Hola

#2. CONCATENABLES
print(palabra + " " + "mundo") # Hola mundo
# Solo se pueden unir strings con strings:
# "Edad: " + 25 TypeError
print("Edad: "+ str(25)) #str convierte el int

#3. MULTIPLICABLES
print("ab" * 3)
print("=" * 20)

#4. MULTILINEALES
texto = """Línea 1
Línea 2
Línea 3"""
print(texto)

#5. LONGITUD
print(len("hola")) # 4

#6. CONTENIDO: in / not in
print("mundo" in "hola mundo")
print("x" not in "hola")
print("HOLA" in "hola mundo") # False (distingue mayúsculas y minúsculas)

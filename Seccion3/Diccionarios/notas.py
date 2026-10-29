#DICCIONARIOS EN PYTHON


"""
1.Qué es un DICCIONARIO
Un diccionario guarda datos en parejas: llave : valor

Analogía: la agenda de contactos de tu celular.
-Buscas por el NOMBRE de la persona (llave)
=Te sale su TELEFONO (valor)

Diferencia clave con las listas:
-Lista: Buscas por POSICIÓN (indice 0, 1, 2...)
-Diccionario: buscas por LLAVE
"""
#==============================================================================
print("--- 1. Crear un diccionario ---")

# Con llaver { }, cada pareja es llave : valor y se separan con comas
producto = {"nombre": "Tacos", "precio": 15, "stock": 40}
print(producto)

#Diccionario vacio (dos formas)
vacio_1 = {}
vacio_2 = dict()
print(vacio_1, vacio_2)

#Otra forma con dict(): aqui las llaves se escriben SIN comillas y con =
persona_2 = dict(nombre="Ana", edad=20)
print(persona_2)

#Las llaves normalmente son strings, pero tambien pueden ser numeros
codigos = {101: "Taco", 102:"Torta"}
print(codigos[101])
#==============================================================================
print("\n--- 2. Acceder a un valor ---")

persona = {"nombre": "Luis", "edad":21, "semestre": 4}
#Se usa la LLAVE entre corchetes (no un indice)
print(persona["nombre"])
print(persona["edad"])

#Puedes guardar un valor en una variable y usarlo
nombre = persona["nombre"]
print("Hola", nombre)

#Puedes usar el valor en operaciones normales
print(producto["precio"] * producto["stock"])
#==============================================================================
print("\n--- 3. Agregar y Modificar ---")
"""
La sintaxis es la misma para agregar y para modificar:
diccionario[llave] = valor
-Si la llave NO existe, la agrega
-Si la llave YA existe, sobreescribe su valor

"""
#llave nueva
persona["ciudad"] = "Guadalajara"
print(persona)

#llave existente
persona["edad"] = 22
print(persona)

#usar el valor actual para calcular el nuevo
persona["edad"] = persona["edad"] + 1
print(persona["edad"])
#==============================================================================
print("\n--- 4. Eliminar ---")

#del borra la pareja completa
del persona["ciudad"]
print(persona)

#pop borra la pareja y te devuelve el valor que tenia
semestre_borrado = persona.pop("semestre")
print(semestre_borrado)
print(persona)

#clear vacia todo el diccionario
copia_temporal = {"x": 1, "y": 2}
copia_temporal.clear()
print(copia_temporal)
#==============================================================================
print("\n--- 5. Get ---")

#Con corchetes, si la llave no existe te sale KeyError y el programa se detiene.
#Con get, si la llave no existe te devuelve None (o el valor que tú le pongas).
print(persona.get("nombre"))
print(persona.get("telefono"))
print(persona.get("telefono", "No registrado"))

#get no agrega nada al diccionario, solo consulta
print(persona)

#setdefault: si la llave no existe, la AGREGA con ese valor; si existe, no la toca
persona.setdefault("pais", "Mexico")
persona.setdefault("nombre", "Otro nombre") #ya existe, no cambia
print(persona)
#==============================================================================
print("\n--- 6. Keys,Values e Items ---")
producto = {"nombre": "Tacos", "precio": 15, "stock": 40}

print(producto.keys())
print(producto.values()) #Se pueden convertir a lista con "list"
print(producto.items())
#==============================================================================
print("\n--- 7. Len e In ---")
#len cuenta cuántas PAREJAS hay
print(len(producto))

#in pregunta si algo existe y responde con True o False
print("precio" in producto)
print("color" in producto)
print("Tacos" in producto) #False -> "Tacos" es un valor, no una llave

# Para buscar entre los valores hay que pedir los values()
print("Tacos" in producto.values()) # True
#==============================================================================
print("\n--- 8. Update ---")
datos_extra = {"stock": 35, "categoria": "comida"}
producto.update(datos_extra)
print(producto)
#==============================================================================
print("\n--- 9. Valores variados y anidados ---")

#Un valor puede ser: string,numero, booleano, lista o incluso otro diccionario
alumno = {
    "nombre": "Ana",
    "calificaciones": [90,85,100],
    "activo": True,
    "direccion": {"calle": "Av. Revolución", "numero": 123}
}

# Para entrar a un valor anidando se va encadenando corchetes, de afuera hacia adentro
print(alumno)
print(alumno["calificaciones"][0]) # 90 (diccionario -> lista -> indice)
print(alumno["direccion"]["calle"]) # Av. Rev (diccionario -> diccionario)

# Se pueden usar los metodos del tipo que sea ese valor
alumno["calificaciones"].append(95)
alumno["direccion"]["numero"] = 456
print(alumno)
#==============================================================================
print("\n--- 10. Lista de diccionarios ---")

#Cada diccionario es UNA FILA, las llaves son los NOMBRES DE LAS COLUMNAS
pedidos =  [
    {"cliente": "Ana", "producto": "Taco", "cantidad": 3, "precio": 15},
    {"cliente": "Beto", "producto": "Torta", "cantidad": 2, "precio": 40}
]

print(pedidos[0])
print(pedidos[0]["cliente"])
print(pedidos[1]["cantidad"] * pedidos[1]["precio"])

#Agregar una fila nueva = append de un diccionario nuevo
pedidos.append({"cliente": "Carla", "producto": "Agua", "cantidad": 1, "precio": 20})
print(len(pedidos))
#==============================================================================
print("\n--- 11. Referencia vs copia ---")
#Igualar NO copia: las dos variables apuntan al mismo diccionario
original = {"a": 1, "b": 2}
referencia = original
referencia["a"] = 999
print(original)  # {'a': 999, 'b': 2}  <- el original también cambió

# .copy() sí crea un diccionario nuevo e independiente
original = {"a": 1, "b": 2}
copia = original.copy()
copia["a"] = 999
print(original)  # {'a': 1, 'b': 2}    <- el original sigue igual
print(copia)  # {'a': 999, 'b': 2}

# Cuidado: .copy() es una copia "superficial". Si el diccionario tiene una lista
# o un diccionario ADENTRO, esa parte interna se sigue compartiendo.
anidado = {"nombre": "X", "notas": [1, 2]}
copia_superficial = anidado.copy()
copia_superficial["notas"].append(3)
print(anidado)  # {'nombre': 'X', 'notas': [1, 2, 3]}  <- ¡también cambió!
#==============================================================================
print("\n--- 13. Otros detalles ---")
# Los diccionarios recuerdan el orden en que agregaste las parejas,
# pero NO tienen índices: no puedes pedir "el elemento 0".
orden = {"z": 1, "a": 2, "m": 3}
print(orden)  # {'z': 1, 'a': 2, 'm': 3}

# sorted te da una LISTA con las llaves ordenadas (no modifica el diccionario)
print(sorted(orden))  # ['a', 'm', 'z']

# Las llaves son únicas: una llave no puede aparecer dos veces
# Los valores sí se pueden repetir
repetidos = {"a": 5, "b": 5}
print(repetidos)  # {'a': 5, 'b': 5}


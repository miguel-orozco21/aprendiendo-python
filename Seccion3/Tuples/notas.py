# =====================================================
# TUPLAS (tuples) EN PYTHON - CÓDIGO EXPLICADO
# =====================================================
# Corre el archivo completo o ve bloque por bloque.
# Las líneas que dicen "ERROR:" están comentadas a propósito.
# Si quieres ver el error en vivo, quítales el # una por una
# (de una en una, porque el programa se detiene en el primer error).


# -----------------------------------------------------
# 1. QUÉ ES UNA TUPLA
# -----------------------------------------------------
# Una tupla es una colección ORDENADA de datos que NO se puede
# modificar después de crearla (es inmutable).
# Analogía: una lista es una libreta con lápiz, puedes borrar y
# escribir. Una tupla es la misma libreta pero escrita con pluma
# y laminada: lo que quedó escrito, ahí se queda.

coordenadas = (20.6597, -103.3496)  # latitud y longitud de Guadalajara
print(coordenadas)
print(type(coordenadas))  # <class 'tuple'>


# -----------------------------------------------------
# 2. CÓMO SE CREAN
# -----------------------------------------------------
dias = ("lunes", "martes", "miércoles")  # con paréntesis
mezclada = ("Pastel", 150, 4.5, "chocolate")  # acepta tipos mezclados, igual que las listas
print(dias)
print(mezclada)

# Lo que realmente hace a una tupla son las COMAS, no los paréntesis
sin_parentesis = 1, 2, 3
print(sin_parentesis, type(sin_parentesis))  # sí es tupla

# Tupla vacía (de dos formas)
vacia1 = ()
vacia2 = tuple()
print(vacia1, vacia2, len(vacia1))

# ERROR COMÚN 1: tupla de un solo elemento SIN la coma
una_sola = (10,)      # con coma -> es tupla
no_es_tupla = (10)    # sin coma -> son solo paréntesis de agrupar, es un int
print(type(una_sola))
print(type(no_es_tupla))

# Convertir otras cosas a tupla con tuple()
desde_lista = tuple(["a", "b", "c"])
desde_texto = tuple("hola")  # un texto se separa letra por letra
print(desde_lista)
print(desde_texto)


# -----------------------------------------------------
# 3. CÓMO SE ACCEDE (igual que las listas)
# -----------------------------------------------------
meses = ("enero", "febrero", "marzo", "abril", "mayo", "junio")

print(meses[0])     # primer elemento
print(meses[-1])    # último elemento
print(meses[1:4])   # rebanada: del índice 1 al 3
print(meses[:2])    # los primeros dos
print(meses[::2])   # de dos en dos
print(meses[::-1])  # al revés

# Una rebanada de una tupla SIEMPRE devuelve otra tupla
print(type(meses[1:4]))


# -----------------------------------------------------
# 4. INMUTABILIDAD (lo más importante del tema)
# -----------------------------------------------------
# No puedes cambiar, agregar ni quitar elementos.

# ERROR: meses[0] = "ENERO"
#   -> TypeError: 'tuple' object does not support item assignment
# ERROR: meses.append("julio")
#   -> AttributeError: 'tuple' object has no attribute 'append'
# ERROR: del meses[0]
#   -> TypeError: 'tuple' object doesn't support item deletion
# Tampoco existen sort, remove, insert, pop, etc.

# ERROR COMÚN 2: pensar que reasignar la variable "modifica" la tupla.
# No la modifica: crea una tupla NUEVA y la variable ahora apunta a ella.
precio = (100, 200)
viejo = precio          # otra variable apuntando a la misma tupla
precio = (100, 250)     # ahora "precio" apunta a una tupla NUEVA
print(precio)           # (100, 250)
print(viejo)            # (100, 200) -> la tupla original sigue intacta


# -----------------------------------------------------
# 5. LO QUE SÍ SE PUEDE HACER
# -----------------------------------------------------
a = (1, 2, 3)
b = (4, 5)

print(a + b)      # unir tuplas -> crea una nueva (1, 2, 3, 4, 5)
print(a * 2)      # repetir -> (1, 2, 3, 1, 2, 3)
print(2 in a)     # True
print(9 in a)     # False
print(len(a))     # 3

# ERROR COMÚN 3: sumar tupla con algo que no es tupla
# ERROR: (1, 2) + (3)
#   -> TypeError: can only concatenate tuple (not "int") to tuple
# Ojo, (3) es un int. Lo correcto es (1, 2) + (3,)
print((1, 2) + (3,))

# --- Los únicos 2 métodos que tiene una tupla ---
ventas = (1200, 850, 1430, 990, 1430)

# count: cuántas veces aparece un valor
print(ventas.count(1430))   # 2

# index: en qué posición está la PRIMERA vez que aparece el valor
print(ventas.index(990))    # 3
print(ventas.index(1430))   # 2 (solo te da la primera aparición)

# ERROR COMÚN 4: index de algo que no existe
# ERROR: ventas.index(5000)
#   -> ValueError: tuple.index(x): x not in tuple
# Para evitarlo, primero revisa con in que el valor exista
print(5000 in ventas)   # False -> mejor no pedir su index

# sorted funciona, pero devuelve una LISTA (como viste con listas)
ordenadas = sorted(ventas)
print(ordenadas)
print(type(ordenadas))  # <class 'list'>
# ERROR: ventas.sort()  -> no existe, la tupla no se puede ordenar "en sitio"


# -----------------------------------------------------
# 6. DESEMPAQUETADO (unpacking)
# -----------------------------------------------------
# Sacar cada elemento de la tupla a su propia variable en una línea.
registro = ("Miguel", 4, "Ingeniería Informática")
nombre, semestre, carrera = registro
print(nombre)
print(semestre)
print(carrera)

# ERROR COMÚN 5: no coincide la cantidad de variables con la de elementos
# ERROR: x, y = (1, 2, 3)
#   -> ValueError: too many values to unpack (expected 2)
# ERROR: x, y, z, w = (1, 2, 3)
#   -> ValueError: not enough values to unpack (expected 4, got 3)

# Intercambiar dos variables sin variable auxiliar
x = 5
y = 9
x, y = y, x   # por dentro Python arma la tupla (y, x) y la desempaqueta
print(x, y)   # 9 5

# Ignorar un valor que no necesitas: se usa el guion bajo
nombre, _, carrera = registro
print(nombre, carrera)

# Con asterisco, una variable recoge "todo el resto" (siempre queda como LISTA)
primero, *resto = (10, 20, 30, 40)
print(primero)   # 10
print(resto)     # [20, 30, 40]

primero, *medio, ultimo = (10, 20, 30, 40, 50)
print(primero, medio, ultimo)  # 10 [20, 30, 40] 50


# -----------------------------------------------------
# 7. LA TRAMPA: TUPLA CON UNA LISTA ADENTRO
# -----------------------------------------------------
# La tupla guarda "referencias" a sus elementos. No puede cambiar
# a cuál elemento apunta, pero si ese elemento es una lista, la
# lista SÍ puede cambiar por dentro.
# Analogía: la tupla es un llavero con llaves fijas. No puedes
# cambiar las llaves, pero lo que hay dentro de la bodega que abre
# una de ellas sí puede cambiar.

pedido = ("Boda García", 150, ["pastel", "bebidas"])
pedido[2].append("mesa de postres")  # esto SÍ funciona
print(pedido)  # ('Boda García', 150, ['pastel', 'bebidas', 'mesa de postres'])

# ERROR: pedido[2] = ["otra lista"]
#   -> TypeError: 'tuple' object does not support item assignment
# (cambiar a CUÁL lista apunta sí está prohibido; cambiar lo de adentro no)


# -----------------------------------------------------
# 8. "MODIFICAR" UNA TUPLA (en realidad, crear otra)
# -----------------------------------------------------
# Forma 1: convertir a lista, cambiar, volver a tupla
tupla = (1, 2, 3)
lista = list(tupla)
lista.append(4)
lista[0] = 99
tupla = tuple(lista)
print(tupla)  # (99, 2, 3, 4)

# Forma 2: rebanadas + suma de tuplas (cambiar el 20 por 25)
original = (10, 20, 30)
nueva = original[:1] + (25,) + original[2:]
print(nueva)     # (10, 25, 30)
print(original)  # (10, 20, 30) -> la original sigue intacta


# -----------------------------------------------------
# 9. LISTA DE TUPLAS (patrón muy usado en datos)
# -----------------------------------------------------
# Cada tupla es una "fila" y la lista es la "tabla".
ventas_dia = [("lunes", 1200), ("martes", 850), ("miércoles", 1430)]

print(ventas_dia[0])      # ('lunes', 1200) -> una fila completa
print(ventas_dia[0][1])   # 1200 -> primer índice elige la fila, segundo la columna
print(ventas_dia[-1][0])  # 'miércoles'

ventas_dia.append(("jueves", 990))  # la LISTA sí crece, las tuplas no cambian
print(len(ventas_dia))              # 4

dia, monto = ventas_dia[1]          # desempaquetar una fila
print(dia, monto)

ventas_dia.sort()  # ordena comparando primero el elemento 0 de cada tupla
print(ventas_dia)  # (si hay empate en el 0, desempata con el 1, y así)


# -----------------------------------------------------
# 10. TUPLAS + SPLIT: parsear una línea de datos
# -----------------------------------------------------
# Caso típico: una línea de un log o un archivo de texto
linea = "ERROR|2026-11-24 10:32|conexion_db|timeout"
campos = tuple(linea.split("|"))
print(campos)

nivel, hora, modulo, mensaje = campos
print("Nivel:", nivel)
print("Módulo:", modulo)
print("Mensaje:", mensaje)



# -----------------------------------------------------
# 11. ¿TUPLA O LISTA? CÓMO DECIDIR
# -----------------------------------------------------
# Usa TUPLA cuando:
#   - Los datos describen UNA sola cosa y no deben cambiar
#     (una coordenada, un registro, una fila, un RGB, una fecha)
#   - Quieres protegerte de cambiar datos por accidente
#   - Los elementos tienen significado por su POSICIÓN
#     (posición 0 = nombre, posición 1 = edad...)
#
# Usa LISTA cuando:
#   - La colección va a crecer, encogerse u ordenarse
#   - Son muchos elementos "del mismo tipo" (todas las ventas del mes)
#
# Extra: la tupla ocupa un poco menos memoria y se crea más rápido
# que una lista.


# -----------------------------------------------------
# 11.B TUPLAS Y DICCIONARIOS
# -----------------------------------------------------
# Como las tuplas son inmutables, SÍ pueden ser llave de un diccionario.
# Las listas no pueden.
ventas_ciudad_mes = {
    ("Guadalajara", "enero"): 12000,
    ("Guadalajara", "febrero"): 9500,
    ("Zapopan", "enero"): 7000,
}
print(ventas_ciudad_mes[("Guadalajara", "febrero")])  # 9500

# ERROR: {["Guadalajara", "enero"]: 12000}
#   -> TypeError: unhashable type: 'list'

# Además, .items() te da los pares del diccionario como TUPLAS
datos = {"nombre": "Miguel", "semestre": 4}
pares = list(datos.items())
print(pares)        # [('nombre', 'Miguel'), ('semestre', 4)]
print(pares[0])     # ('nombre', 'Miguel')
print(pares[0][1])  # 'Miguel'


# -----------------------------------------------------
# 12. APLICACIONES: VIDA, NEGOCIO E INGENIERÍA DE DATOS
# -----------------------------------------------------
# VIDA DIARIA
#   - Fecha de nacimiento (día, mes, año): no cambia.
#   - Coordenadas de tu casa (lat, lon): son un solo "punto".
#   - Color RGB (255, 128, 0): tres valores que forman un solo color.
#
# NEGOCIO (ej. el catering)
#   - Un pedido como registro fijo: (cliente, fecha, total).
#   - Una lista de tuplas como tabla simple de ventas.
#   - Datos que no quieres que alguien modifique por error
#     (precios del menú de un evento ya cotizado).
#
# INGENIERÍA DE DATOS (aquí es donde más aparecen)
#   - Una fila de una base de datos: cuando haces una consulta SQL
#     desde Python (psycopg2, sqlite3), cada fila te llega como una
#     TUPLA y todo el resultado es una LISTA DE TUPLAS. Justo el
#     patrón de la sección 9.
#   - Parsear archivos: línea de texto -> split -> tupla -> desempaquetar
#     en variables con nombre (sección 10).
#   - Funciones que devuelven varios valores: en realidad devuelven
#     una tupla (lo verás cuando llegues a funciones).
#   - Llaves compuestas: identificar un registro por varios campos
#     juntos, como (id_cliente, fecha), usadas como llave de un
#     diccionario (sección 11.B).
#   - Diccionario -> lista de tuplas con .items(): puente natural
#     hacia tablas y DataFrames.
#   - Inmutabilidad = seguridad: en un pipeline, los datos crudos que
#     llegan no deben alterarse a media ruta. La tupla lo garantiza.
#
# REGLA PARA RECORDAR:
#   "Si es un registro fijo, tupla. Si es una colección que cambia, lista."
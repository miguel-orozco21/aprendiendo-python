
print("LISTAS EN PYTHON")
print("Lista = coleccion ORDENADA y MUTABLE\n")


# ---------- 1. CREAR ----------

vacia = []
numeros = [10, 20, 30, 40, 50]
mezclada = ["Ana", 25, True]          # acepta tipos mezclados
desde_texto = "a,b,c".split(",")      # split devuelve una lista -> ['a','b','c']

print(numeros)

# ---------- 2. ÍNDICES ----------
print("-" * 40)
# posición:  0   1   2   3   4
# negativo: -5  -4  -3  -2  -1
print("Primer numero: ", numeros[0])        # 10  (primero)
print("Ultimo numero: ", numeros[-1])       # 50  (último)
print("Cantidad: ", len(numeros))      # 5   (cantidad)
# print(numeros[5])      # IndexError: el último índice es len-1 = 4
print("-" * 40)

# ---------- 3. SLICING [inicio:fin:paso] (el fin NO se incluye) ----------
print("SLICING")
print(numeros[1:4])      # [20, 30, 40]
print(numeros[:2])       # [10, 20]
print(numeros[-2:])      # [40, 50]
print(numeros[::2])      # [10, 30, 50]
print(numeros[::-1])     # [50, 40, 30, 20, 10] (invertida)
print("-" * 40)

# ---------- 4. MODIFICAR (mutable) ----------
print("Modificar (mutable)")
numeros[0] = 99
print(numeros)           # [99, 20, 30, 40, 50]
print("-" * 40)
# ---------- 5. MÉTODOS ----------
print("Metodos")
l = [3, 1, 2]
print(l)
l.append(4)              # agrega al final        -> [3, 1, 2, 4]
print("agrega al final: ", l)
l.insert(1, 99)          # inserta en posición 1  -> [3, 99, 1, 2, 4]
print("inserta en posicion 1: ", l)
l.extend([7, 8])         # agrega varios sueltos  -> [3, 99, 1, 2, 4, 7, 8]
print("agrega varios sueltos: ", l)
l.remove(99)             # quita el PRIMER 99     -> [3, 1, 2, 4, 7, 8]
print("quita el primer 99: ", l)
ultimo = l.pop()         # quita y devuelve el último (8)
primero = l.pop(0)       # quita y devuelve el primero (3)
print("quita y devuelve el primero y el ultimo: ", l, primero, ultimo)  # [1, 2, 4, 7] 8 3
print("Cuantas veces aparece el 2: ", l.count(2))        # 1  (cuántas veces aparece el 2)
print("posicion del primer 4: ", l.index(4))        # 2  (posición del primer 4)
print("-" * 40)

# append vs extend
print("append vs extend")
x = [1, 2]
print("x", x)
x.append([3, 4])         # [1, 2, [3, 4]]  <- metió una lista adentro
y = [1, 2]
print("y", y)
y.extend([3, 4])         # [1, 2, 3, 4]    <- metió los elementos sueltos
print("append metio una lista dentro: ", x)
print("extend metio los elementos sueltos: ", y)
print("-" * 40)
# ---------- 6. OPERADORES Y FUNCIONES ----------
print("Operadores y Funciones")
a = [1, 2]
b = [3, 4]
print("a", a)
print("b", b)
print("a + b", a + b)          # [1, 2, 3, 4]
print("a * 3", a * 3)             # [1, 2, 1, 2, 1, 2]
print("2 esta en a?", 2 in a)            # True
ll = [1, 2, 50, 5, 25]
print(ll)
print("Suma, minimo y maximo: ", sum(ll), min(ll), max(ll))  # 30 2 9
print("-" * 40)

# ---------- 7. sort() vs sorted() ----------
#sorted devuelve una lista nueva, sort modifica la misma

datos = [3, 1, 2]
nueva = sorted(datos)                 # lista nueva; datos NO cambia
mayor_a_menor = sorted(datos, reverse=True)   # [3, 2, 1]
datos.sort()                          # ordena datos MISMO y devuelve None
# ERROR típico: datos = datos.sort()  -> datos queda en None

# ---------- 8. REFERENCIA vs COPIA ----------
print("Referencia vs Copia")
a = [1, 2, 3]
b = a                    # MISMA lista con 2 nombres
c = a.copy()             # copia independiente (también sirve a[:])
b.append(99)
c.append(55)
print(a)                 # [1, 2, 3, 99]  <- a cambió por b
print(c)                 # [1, 2, 3, 55]
print("-" * 40)
# ---------- 9. LISTAS ANIDADAS (tabla) ----------
print("Listas Anidadas")
tabla = [
    ["Ana",   1200, "norte"],
    ["Luis",   850, "sur"],
    ["Sofia", 2300, "norte"],
]
print(tabla)
print(tabla[1])          # ['Luis', 850, 'sur']  (fila)
print(tabla[1][0])       # 'Luis'                (fila 1, columna 0)
tabla.append(["Pedro", 990, "sur"])
print("-" * 40)
# TRAMPA: multiplicar listas anidadas
print("Multiplicar listas anidadas")
malo = [[0, 0]] * 3
malo[0][0] = 9
print(malo)              # [[9, 0], [9, 0], [9, 0]] <- las 3 filas son la MISMA
print("-" * 40)
# ---------- 10. split y join ----------
print("Split y join")
texto = "Ana,Zeus,Pedro,Sofia"
print("texto:", texto)
print("texto -> lista")
nombres = texto.split(",")            # texto -> lista
print(nombres)
print("lista -> texto con sorted")
print("-".join(sorted(nombres)[:4]))  #  (lista -> texto)
print("-" * 40)


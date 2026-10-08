# ---------- index() ----------
# Devuelve la posición (empezando en 0) donde empieza el texto buscado.
# Si no lo encuentra, lanza ValueError (find() devuelve -1).

texto = "data engineering"
texto.index("eng")      # 5
texto.index("data")     # 0

# Es sensible a mayúsculas:
"Hola".index("h")       # ValueError: substring not found

# Solo regresa la PRIMERA aparición:
"banana".index("a")     # 1

# Segundo argumento: desde qué posición empezar a buscar
"banana".index("a", 2)  # 3

# rindex(): igual pero busca desde el final (última aparición)
"banana".rindex("a")    # 5
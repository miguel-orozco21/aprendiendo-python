"""
De texto a lista y de regreso

Parte del texto "Ana,Luis,Pedro,Sofia"
Conviertelo en lista separando por coma
Ordenala alfabeticamente sin modificar la original
Quedate con los primeros 2 nombres
Juntalos en un solo texto separados por un guion e imprimelo
"""

texto = "Ana,Luis,Pedro,Sofia"
nombres = texto.split(",")
print(nombres)
print("-".join(sorted(nombres)[:2]))
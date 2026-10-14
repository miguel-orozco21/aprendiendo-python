#Separador
print("=" * 30)
print("REPORTE DE VENTAS".center(30))
print("=" * 30)

#Multilinea + len + in
menu = """burritos
tacos dorados
tamales"""
print(len(menu))
print("tamales" in menu)

#Inmutabilidad
palabra = "python"
palabra = palabra[0].upper() + palabra[1:]
print(palabra)


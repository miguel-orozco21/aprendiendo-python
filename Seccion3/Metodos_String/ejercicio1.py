#Dado correo = " MIGUEL@Gmail.COM \n", déjalo limpio y en minúsculas.
correo = " MIGUEL@Gmail.COM \n"
print(correo.strip().lower())

#Dado fecha = "08/10/2026", conviértelo a "08-10-2026" y luego sácale solo el año con slicing
fecha = "08/10/2026"

print(fecha.replace("/", "-"))
print(fecha[6:])

#Dado id_cliente = "7", déjalo como "CLI-00007" (pista: zfill y concatenación).
id_cliente = "7"
print(f"CLI-{id_cliente.zfill(5)}")

#Dado linea = "Silvias,Banquete,1500,Guadalajara", sácale el tercer campo y revisa con isdigit() si es un número válido.
linea = "Silvias,Banquete,1500,Guadalajara".split(",")
print(linea[2].isdigit())

#Dado archivo = "ventas_2026.csv", comprueba si termina en .csv y cuenta cuántas veces aparece la letra "s".
archivo = "ventas_2026.csv"
print(archivo.endswith(".csv"))
print(archivo.count("s"))

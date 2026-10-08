texto = "ABCDEFGHIJKLM"

fragmento = texto[2] #Extrar un caracter
fragmento2 = texto[2:5] #Extrar un rango de caracteres
fragmento3 = texto[2:] #Extrar desde el caracter 2 hasta el final
fragmento4 = texto[:5:] #Extrar desde el inicio hasta el 5 sin incluirlo
fragmento5 = texto[::-1] #Extraer de la derecha a la izquierda (voltear cadenas)
fragmento6 = texto[:10:2] #Extraer saltandose de 2 en 2 caracteres


print(fragmento)
print(fragmento2)
print(fragmento3)
print(fragmento4)
print(fragmento5)
print(fragmento6)


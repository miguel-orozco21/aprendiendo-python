#Input siempre devuelve un string
edad = input("Ingresa tu edad: ") # str -> "21"

print(type(edad))
edad = int(edad) # int -> 21
print(type(edad))
nueva_edad = edad + 1

print(f"Tu nueva edad es {nueva_edad}")

#Convertirlo directo en la misma línea

edad2 = int(input("Ingresa tu edad: ")) # int -> 21

print(type(edad2))
print(f"Tu nueva edad es: {edad2 + 1}")

#Proteccion por si el usuario escribe algo invalido
try:
    edad3 = int(input("Ingresa tu edad: "))
    print(f"Tu nueva edad es {edad + 1}")
except ValueError:
    print("Por favor ingresa un número válido.\n")


#While true, te deja seguir intentando

while True:
    try:
        edad4 = int(input("Ingresa tu edad: "))
        print(f"Tu nueva edad es {edad4 + 1}")
        break
    except ValueError:
        print("Por favor ingresa un numero valido.\n")
#Calculador de comisiones

nombre = input("Cual es tu nombre? ")
ventas = float(input("Cuanto has vendido este mes? "))
PORCENTAJE_COMISION = 13

comision = round(ventas * (PORCENTAJE_COMISION / 100), 2)

print(f"Estimado {nombre} tu comision por las ventas generadas en el mes es de {comision}")
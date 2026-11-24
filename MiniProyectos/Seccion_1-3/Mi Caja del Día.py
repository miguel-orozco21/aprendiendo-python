# Mi Caja del Día
#Etapa actual : Version 1

# --- Captura de datos ---
fecha = input("Introduce la fecha de hoy (##/##/##): ")
print("Entrega 1")
km = float(input("Kilometros: "))
pago = float(input("Pago: "))
propina = float(input("Propina: "))


# --- Calculos ---
total_ganado = pago + propina
ganancia_porkm = total_ganado / km

# --- Guardar entregas en un diccionario ---
entrega1 = {
    "kilometros": km,
    "pago": pago,
    "propina": propina,
    "total_de_ganancias": total_ganado,
    "ganancia_por_km": ganancia_porkm,
}

# --- Lista de 3 entregas ---
entregas_del_dia = []


#repeticion para guardar 3 entregas
print("Entrega 2")
km = float(input("Kilometros: "))
pago = float(input("Pago: "))
propina = float(input("Propina: "))
total_ganado = pago + propina
ganancia_porkm = total_ganado / km
entrega2 = {
    "kilometros": km,
    "pago": pago,
    "propina": propina,
    "total_de_ganancias": total_ganado,
    "ganancia_por_km": ganancia_porkm,
}


print("Entrega 3")
km = float(input("Kilometros: "))
pago = float(input("Pago: "))
propina = float(input("Propina: "))
total_ganado = pago + propina
ganancia_porkm = total_ganado / km
entrega3 = {
    "kilometros": km,
    "pago": pago,
    "propina": propina,
    "total_de_ganancias": total_ganado,
    "ganancia_por_km": ganancia_porkm,
}

#append
entregas_del_dia.append(entrega1)
entregas_del_dia.append(entrega2)
entregas_del_dia.append(entrega3)

#Resumen del dia: totales y promedios
total_dia = entregas_del_dia[0]["total_de_ganancias"] + entregas_del_dia[1]["total_de_ganancias"] + entregas_del_dia[2]["total_de_ganancias"]
total_propinas = entregas_del_dia[0]["propina"] + entregas_del_dia[1]["propina"] + entregas_del_dia[2]["propina"]
total_km = entregas_del_dia[0]["kilometros"] + entregas_del_dia[1]["kilometros"] + entregas_del_dia[2]["kilometros"]

promedio_por_entrega = total_dia / len(entregas_del_dia)
# --- Salida de datos ---

print("\t=== Mi Caja del Día ===\n"
      f"Día trabajado:\t{fecha}\n"
      f"ENTREGAS\n"
      f"1.Pago por viaje: {entrega1['pago']:.2f} | kilometros: {entrega1['kilometros']:.2f} | propina: {entrega1['propina']:.2f} | Total: {entrega1['total_de_ganancias']:.2f}\n"
      f"2.Pago por viaje: {entrega2['pago']:.2f} | kilometros: {entrega2['kilometros']:.2f} | propina: {entrega2['propina']:.2f} | Total: {entrega2['total_de_ganancias']:.2f}\n"
      f"3.Pago por viaje: {entrega3['pago']:.2f} | kilometros: {entrega3['kilometros']:.2f} | propina: {entrega3['propina']:.2f} | Total: {entrega3['total_de_ganancias']:.2f}")
print("-" * 30)
print(f"RESUMEN\n"
      f"Promedio por pedido: {promedio_por_entrega:.2f}\nTotal ganado: {total_dia:.2f}\nKm recorridos: {total_km:.2f}\nTotal propinas: {total_propinas:.2f}")
print("=" * 30)



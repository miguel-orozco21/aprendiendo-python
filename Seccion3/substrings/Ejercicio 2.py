sku = "MX2024030087"

#pais (2 chars) + anio (4 chars) + mes (2 chars) + folio (4 chars)
#Extrae cada parte y arma un diccionario

pais = sku[:2]
anio = sku[2:6]
mes = sku[6:8]
folio = sku[8:]

sku_dict = {
    "pais": pais,
    "anio": anio,
    "mes": mes,
    "folio": folio
}

print(sku_dict)

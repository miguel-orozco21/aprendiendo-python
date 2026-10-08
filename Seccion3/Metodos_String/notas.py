"""
Los strings son inmutables: Ningún método modifica el string original,
siempre devuelve uno nuevo. Si se quiere conservar el cambio, se guarda en
una variable

"""

"""
Metodos de estas notas:
- upper
- lower
- split
- join
- find
- replace

Consulta el pdf para conocer más de los 30 metodos de string
"""

texto = "Este es el texto de Miguel"
mayus = texto.upper()
minus = texto.lower()
separar = texto.split()
encontrar = texto.find("s")
remplazar = texto.replace("Miguel","Pedrito")


print(mayus)
print(minus)
print(separar)
print(encontrar)
print(remplazar)

a = "Aprender"
b = "Python"
c = "es"
d = "genial"

e = " ".join([a,b,c,d])
print(e)

#  variable

diccionario={"color":"violeta", "talle":"xs", "precio":174.25}

# obtener el valor de una clave

diccionario.get("color")

# saber si una clave existe en el diccionario

existe="precio" in diccionario
print(existe)

# obtener las claves  y los valores de un diccionario

for clave, valor in diccionario.items():
    print("El valor de la clave %s es %s "%(clave, valor))


# obtener las claves de un diccionario

claves=diccionario.keys()
print(claves)

# obtener los valores de un diccionario

valores=diccionario.values()
print(valores)

# obtener la cantidad de elementos de un diccionario

len(diccionario)

























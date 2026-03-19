
#  variable

diccionario={"color":"violeta", "talle":"xs", "precio":174.25}

# copair diccionario

remera=diccionario.copy()
print(remera)


# crear  un nuevo diccionario desde las claves de una secuencia

secuencia=["color", "talle", "marca"]
diccionario1=dict.fromkeys(secuencia)
print(diccionario1)

diccionario2=dict.fromkeys(secuencia, 'valor x defecto')
print(diccionario2)

# concatenar diccionarios

diccionario1={"color":"rosa", "tamaño":"xl"}
diccionario2={"marca":"adidas", "precio":45.85}

diccionario1.update(diccionario2)
print(diccionario1)

# establecer una clave y valor por defecto

remera={"color":"rojo", "marca":"zara"}
clave=remera.setdefault("talle", "u")
print(remera)

# si la clave no existe, entonces se crea por defecto






















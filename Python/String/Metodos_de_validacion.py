
# variable

cadena="bienvenido a mi aplicacion"

# saber si una cadena comienza con una subcadena determinada 

print(cadena.startswith("bienvenido"))
print(cadena.startswith("aplicacion"))
print(cadena.startswith("aplicacion", 16)) # Posicion incial y final 
print("")

# saber si una cadena finaliza con una subcadena determinada

print(cadena.endswith("aplicacion"))
print(cadena.endswith("bienvenido"))
print(cadena.endswith("bienvenido", 0, 10)) # Posicion incial y final 
print("")

# saber si una cadena es alfa numerica

frase="pop 74"
print(frase.isalnum())

frase="pop"
print(frase.isalnum())

frase="pop74"
print(frase.isalnum())
print("")

# saber si una cadena es alfabetica

frase="pop 74"
print(frase.isalpha())

frase="pop"
print(frase.isalpha())

frase="pop74"
print(frase.isalpha())
print("")

# saber si una cadena es numerica

frase="pepe 75"
print(frase.isdigit())

frase="7584"
print(frase.isdigit())

frase="75 84"
print(frase.isdigit())

frase="75.84"
print(frase.isdigit())
print("")

# saber si una cadena contiene solo minusculas

frase="pepe grillo"
print(frase.islower())

frase="Pepe Grillo"
print(frase.islower())

frase="Pepegrillo"
print(frase.islower())

frase="pepegrillo75"
print(frase.islower())
print("")

# saber si una cadena contiene solo mayusculas

frase="PEPE GRILLO"
print(frase.isupper())

frase="Pepe Grillo"
print(frase.isupper())

frase="Pepegrillo"
print(frase.isupper())

frase="PEPEGRILLO"
print(frase.isupper())
print("")


# saber si una cadena contiene solo espacios en blanco

print(cadena.isspace())

frase="       "
print(cadena.isspace())
print("")

# saber si un cadena tiene formato de titulo

frase="Pepe Grillo"
print(frase.istitle())

frase="Pepe grillo"
print(frase.istitle())
print("")












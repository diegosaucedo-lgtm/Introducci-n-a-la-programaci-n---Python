
# EL PUNTERO ESTA AL INICIO DEL ARCHIVO

# R -> solo lectura

archivo=open("Archivo.txt", "r")

# rb -> solo lectura en modo binario

archivo=open("Archivo.txt", "rb")

# r+ -> lectura  y escritura

archivo=open("Archivo.txt", "r+")

# rb+-> lectura y escritura en modo binario

archivo=open("Archivo.txt", "rb+")

# w -> solo escritura, sobreescribe si el archivo existe, crea el archivo si no existe

archivo=open("Archivo.txt", "w")

# wb-> solo escritura en modo binario, sobreescribe si el archivo existe, crea el archivo si no existe

archivo=open("Archivo.txt", "wb")

# w+ -> solo escritura, sobreescribe si el archivo existe, crea el archivo si no existe

archivo=open("Archivo.txt", "w+")

# wb+-> solo escritura en modo binario, sobreescribe si el archivo existe, crea el archivo si no existe

archivo=open("Archivo.txt", "wb+")

# EL PUNTERO, SI EL ARCHIVO EXISTE AL FINAL DE ESTE Y SI EL ARCHIVO NO EXISTE AL COMIENZO

# a -> añadido(agregar contenido) y crear el archivo si no existe

archivo=open("Archivo.txt", "a")

# ab -> añadido en modo binario (agregar contenido) y crear el archivo si no existe

archivo=open("Archivo.txt", "ab")

# a+ -> añadido(agregar contenido) y lectura y crear el archivo si no existe

archivo=open("Archivo.txt", "a+")

# ab+ -> añadido(agregar contenido) y lectura en modo binario y crear el archivo si no existe

archivo=open("Archivo.txt", "a")





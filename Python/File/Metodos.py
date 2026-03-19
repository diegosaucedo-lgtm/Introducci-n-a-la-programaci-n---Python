
# seek(byte) -> mueve el puntero hacia el byte indicado

#archivo=open("Archivo.txt", "r")
#contenido=archivo.read()
#archivo.seek(1) # el puntero queda al final o inicio del documento
#archivo.close

# read([bytes]) -> lee todo el contenido de un archivo, si se le pasa la longitud de bytes, leera solo el contenido hasta la longitud indicada

#archivo=open("Archivo.txt", "r")
#contenido = archivo.read()
#print(contenido)
#archivo.close()

# readline([bytes]) ->  lee una linea del archivo

#archivo=open("Archivo.txt", "r")
#linea1=archivo.readline()
#print(linea1)
#archivo.close

# readlines() -> lee todas las lineas de un archivo 

#archivo=open("Archivo.txt", "r")
#for linea in archivo.readlines():
    #print(linea)

# tell() -> retorna la posicion actual del puntero

#archivo=open("Archivo.txt", "r")
#linea1=archivo.readline()
#mas=archivo.read(archivo.tell()*2)
#if archivo.tell()>50:
    #archivo.seek(50)

# write(cadena) -> escribe cadena dentro del texto

archivo=open("Archivo.txt", "r+")
contenido=archivo.read()
final=archivo.tell()
archivo.write('Nueva linea')
archivo.seek(final)
nuevo_contenido=archivo.read()
archivo.close()
print(nuevo_contenido)

# writelines(secuencia) -> secuencia sera cualquier iterable cuyos elementos seran escritos por linea

archivo=open("Archivo.txt", "r+")
contenido=archivo.read()
final=archivo.tell()
lista = ['Linea 1\n', 'Linea 2']
archivo.writelines(lista)
archivo.seek(final)
print(archivo.readline())
print(archivo.readline())


# close() -> cierra un archivo

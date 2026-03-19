

# unir una cadena de forma iterativa

factura=("N° 0000-0", "-0000 (ID: ", ")")
numero="275"
numero_factura=numero.join(factura)
print(numero_factura)

# partir una cadena en tres partes, usando un separador

tupla="http://www.peruano.com".partition("www.")
print(tupla)

protocolo, separador, dominio=tupla
print("Protocolo: {0}\nDominio: {1}".format(protocolo, dominio))

# partir una cadena en varias partes, usando un separador

keywords="phyton, guia, curso, tutorial".split(", ")
print(keywords)

# partir una cadena en lineas

texto="""Linea1
Linea 2
Linea 3 
Linea 4"""

print(texto.splitlines())

texto="Linea 1\nLinea 2\nLinea 3"
print(texto.splitlines())























































































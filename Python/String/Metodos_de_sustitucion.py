
# variable

cadena="bienvenido a mi aplicacion {0}"

# dar formato a una cadena, sustituyendo texto dinamicamente

print(cadena.format("en Python"))

cadena="Importe bruto: ${0}+ IVA: ${1} = Importe neto: {2}" 
print(cadena.format(100, 21, 121))

cadena="Importe bruto: ${bruto}+ IVA: ${iva} = Importe neto: {neto}" 
print(cadena.format(bruto=100, iva=21, neto=121))
print(cadena.format(bruto=100, iva=100*21/100, neto=(100*21)/100+100))

# reemplazar texto en una cadena

frase="nombre apellido"
reemplazar="Juan Perez"
print("Estimado señor nombre apellido: ".replace(frase, reemplazar))

# eliminar caracteres a la izquierda y derecha de una cadena

cadena=" www.peruano.com "
print(cadena.strip())
print(cadena.strip(' '))

# eliminar caracteres a la izquierda de una cadena

print(cadena.lstrip(" w."))


# eliminar caracteres a la derecha de una cadena

cadena="www.peruano.com         "
print(cadena.lstrip( ))































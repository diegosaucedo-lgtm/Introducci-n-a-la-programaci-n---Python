

cadena=input("Ingresa una palabra: ")

numCaracteres=len(cadena)

inversion=""

i=numCaracteres-1

while i>=0:
    inversion+=cadena[i]
    i-=1

print("La cadena: ",cadena)
print("La cadena invertida: ",inversion)














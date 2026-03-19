


palabra=input("Ingresa una palabra: ")

can=len(palabra)
inversion=""
i=can-1

while i>=0:
    inversion+=palabra[i]
    i-=1

if inversion==palabra:
    print("La palabra es un palídromo")





























palabra=input("Introduzca una palabra: ")

lista=['a','e','i','o','u','A','E','I','O','U']

cont=0

for vocal in lista:
    for a in palabra:
        if vocal == a:
            cont+=1


print("Hay ",cont," vocales en la palabra ",palabra)





























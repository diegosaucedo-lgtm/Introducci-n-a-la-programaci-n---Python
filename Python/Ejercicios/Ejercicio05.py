

a=int(input("Ingresa un número: "))
i=1
j=0

tupla=(1,2,3,5,7)

for b in tupla:
    if a==b:
        print(a," es un número primo")
    

while i<=4:
    if  a%tupla[i] == 0:
        j+=1

    i+=1
   

if j>=1:
    print(a," no es un número primo")
else:
    print(a," es un número primo")



















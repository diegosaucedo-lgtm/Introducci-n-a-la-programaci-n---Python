

a=int(input("Ingresa la base: "))
b=int(input("Ingresa el exponente: "))

i=1

acum=1



if b==0:
    print("El resultado es 1")
elif b==1:
    print("El resultado es ",a)
else:
    
    while i<=b:
        acum*=a

        i+=1
    
    print("El resultado es ",acum)























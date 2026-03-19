

n=int(input("Ingresa el termino n de la secuencia de Fibonacci: "))

a=0
b=1

i=3

if n==1:
    print(a)
elif n==2:
    print(a," ",b)
elif n>=3:
     print(a," ",b, end='')

     while i<=n:
        c=a+b
        print(" ",c, end='')
        a=b
        b=c

        i+=1











a=int(input("Ingresa el número del factorial: "))
i=1
factorial=i

while i<=a:

    if i != a:
        print(i," x ", end='')
    else:
        print(i," = ", end='')

    factorial*=i
    i+=1


print(factorial)
























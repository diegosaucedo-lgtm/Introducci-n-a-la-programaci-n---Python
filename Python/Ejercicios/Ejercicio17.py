

lista=[]

a=int(input("Ingresa la cantidad de números a introducir: "))
i=0
num=a-1

while i<=num:
    b=int(input("Ingresa el número: "))
    lista.append(b)
    i+=1


print("Los números de la lista : ", lista)


def ordenarLista(lista, num):
    aux=0
    for num1 in lista:
        for num2 in lista[1:]:
            if num2<num1:
                aux=num
            
        

























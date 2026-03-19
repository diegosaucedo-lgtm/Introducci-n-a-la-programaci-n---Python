
# OPERADORES RELACIONALES -> == es igual, =! es diferente, <, >, etc
# OPERADORES LOGICOS -> and(y), or(o), xor(o excluyente, es decir, una de las premisas deber ser V porque las dos a lavez no pueden F)


# Simple
semaforo="verde"

if semaforo=="verde":
    print("Puedes cruzar la calle")


# Compuesto

if semaforo=="verde":
    print("Puedes cruzar la calle")
else:
    print("Debes esperar")


# Anidados

compra=400

if  compra<= 100:
    print("Pago en efectivo")
elif compra>100 and compra<300:
    print("Pago con tarjeta de credito")
else:
    print("Pago con tarjeta de debito")









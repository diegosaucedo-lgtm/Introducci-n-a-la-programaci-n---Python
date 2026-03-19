
#Procedimeiento
def mi_funcion():
    print("Hola")

mi_funcion()


#Funcion sin parametros
def funcion25():
    return "Hola Mundo"

frase=funcion25()

print(frase)

#Funcion con parametross

nombre="Diego"
apellido="Saucedo"

def funcion1(nombre, apellido):
    nombre_completo = nombre+" "+apellido
    print(nombre_completo)

funcion1(nombre, apellido)

# Parametros por omision

def saludar(nombre, mensaje="Hola"):
    print(mensaje, nombre)

saludar("Pepe grillo")


# Keywords como parametros

def saludar2(nombre, mensaje="Hola"):
    print(mensaje, nombre)

saludar2(mensaje="Buen dia", nombre="Juancho")

# Parametros arbitrarios

def recorrer1 (fijo, *arbitrarios):
    print(fijo)

    for argumento in arbitrarios:
        print(argumento)


recorrer1("Hola", "Otco", "Marceka", "Fer")

def recorrer2 (fijos, *arbitrario, **kwords):
    print(fijos)

    for argumentos in arbitrario:
        print(argumentos)

    for clave in kwords:
        print("El valor de ", clave, " es ", kwords[clave])



recorrer2 ("Oto", "Hola", "bhy", "kio", j="jul",  k="yu", l="iol")

# TUPLAS O LISTAS como parametros -> *

def calcular(importe, descuento):
    return importe-(importe*descuento/100)

datos=[1500, 10]

print(calcular(*datos))

# DICCIONARIOS como parametros -> **

dato={"descuento":10, "importe":1500}
print(calcular(**dato))

# LLamadas de retorno -> se lama a la funcion no por su nombre
# Para ello, se usa dos funciones nativas -> locals() y globals()

def func():
    return "Hola mundo"

def saludo(mensaje="Bienvenido", nombre="Diego"):
    print(mensaje, nombre)
    print(func())

saludo()

# Ejemplo 1

#GLOBAL
def llamada_de_retorno(func=""):
    #Llamada de retorno a nivel global
    return globals()[func]()

print(llamada_de_retorno("func"))

#LOCAL
#Llamada de retorno a nivel local
nombre_de_la_funcion = "func"
print (locals()[nombre_de_la_funcion]())

# Ejemplo 2

def funci(nombre):
    return "Hola"+nombre

#GLOBAL
def llamada_de_retorn(func=""):
    return globals()[func]("Laura")

print(llamada_de_retorn("funci"))

#LOCAL
nombre_de_la_fun="funci"
print(locals()[nombre_de_la_fun]("fACUNDO"))


#Saber si una funcion existe y puede ser llamada por retorno

#if nombre_de_la_fun in locals():
   # if callable(locals()[nombre_de_la_fun]):
       # print(locals()[nombre_de_la_fun]("Emilse"))

def funciones(nombre):
    return "Hola "+nombre

def llamada_retorno(func=""):
    if func in globals():
        if callable(globals()[func]):
            return globals()[func]("Laura")
        
    else:
        return "Funcion no encontrada"

print(llamada_retorno("funciones"))


nombre_funcion = "funciones"

if nombre_funcion in locals():
    if callable(locals()[nombre_funcion]):
        print(locals()[nombre_funcion]("fACUNDO"))
else:
    print("Funcion no encontrada")






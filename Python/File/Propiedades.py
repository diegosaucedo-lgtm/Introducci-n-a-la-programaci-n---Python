
# closed -> retorna v si el archivo se ha cerrado
# mode -> retorna el modo de apertura
# name -> retorna el nombre del archivo
# encoding -> retorna la codificacion de caracteres de un archivo de texto

archivo=open("Archivo.txt", "r+")
contenido=archivo.read()
nombre=archivo.name
modo=archivo.mode
encoding=archivo.encoding
archivo.close()

if archivo.closed:
    print("El archivo se ha cerrdo correctamente")
else:
    print("El archivo permanece abierto")











































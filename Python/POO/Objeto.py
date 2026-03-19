
#Creamos los objetos

class antena():
    color=""
    longitud=""

class pelo():
    color=""
    textura=""

class ojo():
    forma=""
    color=""
    tamaño=""

class objeto():
    color="verde"
    tamaño="grande"
    aspecto="feo"
    antenas=antena() #Propiedad compuesta por el objeto objeto Antena
    ojos=ojo()       #Propiedad compuesta por el objeto objeto Ojo
    pelos=pelo()     #Propiedad compuesta por el objeto objeto Pelo


    def flotar(self): #El primer parametro de un metodo siempre debe ser SELF
        print(12)


#OBJETO

et = objeto()
print(et.color)
print(et.tamaño)
print(et.aspecto)

et.color="rosa"
print(et.color)







# Una clase hereda las propiedades y metodos a tora clase       
# Cuando una clase no hereda se tiene que usar OBJECT

class antena(object):
    color=""
    longitud=""

class pelo(object):
    color=""
    textura=""

class ojo(object):
    forma=""
    color=""
    tamaño=""

class objeto(object):
    color="verde"
    tamaño="grande"
    aspecto="feo"
    antenas=antena() #Propiedad compuesta por el objeto objeto Antena
    ojos=ojo()       #Propiedad compuesta por el objeto objeto Ojo
    pelos=pelo()     #Propiedad compuesta por el objeto objeto Pelo


    def flotar(self): #El primer parametro de un metodo siempre debe ser SELF
        print(12)


# ----------------------------------

class dedo(object):
    longitud=""
    forma=""
    color=""

class pie(object):
    forma=""
    color=""
    dedos=dedo()


# HERENCIA

class nuevoObjeto(objeto):
    pie=pie()

    def saltar(self):
        pass


ob = nuevoObjeto()
print(ob.color)
print(ob.flotar())














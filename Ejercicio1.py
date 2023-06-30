#Crea un diccionario que mapee cada letra del alfabeto a un numero del 1 al 26.
#crea una funcion que para cada numero te devuelva el valor de la letra del alfabeto. Esta función tiene que manejar la exceptción de que el número no se encuentre en el diccionario.
#Luego, escribe un programa que tome un mensaje cifrado (una lista de números) y use la función y el diccionario para decodificarlo.

diccionario = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,
                'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,
                'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,
                'v':22,'w':23,'x':24,'y':25,'z':26}

def decodificar(numero):
    try:
        return diccionario[numero]
    except KeyError:
        return "No se encuentra el numero en el diccionario"
    
mensaje = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
mensaje2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,27]

for i in mensaje:
    print(decodificar(i))

for i in mensaje2:
    print(decodificar(i))

    
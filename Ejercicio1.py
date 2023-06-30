#Crea un diccionario que mapee cada letra del alfabeto con un numero del 1 al 26
#Escribe una función que para cada número te devuelva el valor de la letra del alfabeto. Esta función tiene que manejar la exceptción de que el número no se encuentre en el diccionario.
#Luego, escribe un programa que tome un mensaje cifrado (una lista de números) y use la función y el diccionario para decodificarlo.


diccionario = {}
for i in range(1,27):
    diccionario[i] = chr(i+96)
print(diccionario)

def decodificar(lista):
    mensaje = ''
    for i in lista:
        try:
            mensaje += diccionario[i]
        except:
            mensaje += ' Desconocido '
    return mensaje

print(decodificar([1,2,3,4,5,6,7,8,9,10]))
print(decodificar([1,2,3,58,93,45,15]))











    

    
#Crea una clase Biblioteca que contenga como atributo un diccionario de libros. Cada clave del diccionarioo será un título de libro y cada valor será una lista en el que el primer elemento es el autor y el segundo el año de publicación. No importa que no sean reales los libros.
#Agrega los siguientes métodos:
#agregar_libro: Este método aceptará un título de libro y su año de publicación. Añadirá el libro al diccionario con sus características correspondientes.
#remover_libro: Este método aceptará un título de libro y lo removerá del diccionario.
#buscar_por_titulo: Este método aceptará un título y devolverá las características de ese libro, o None si no existe.
#libros_por_autor: Este método aceptará un nombre de autor y devolverá una lista de títulos de libros de ese autor.

#Pruébalo con una biblioteca de 5 libros y comprueba que funcionan todos los métodos.

class Biblioteca:
    def __init__(self):
        self.libros = {}
        
    def agregar_libro(self,titulo,autor,anio):
        self.libros[titulo] = [autor,anio]
        
    def remover_libro(self,titulo):
        del self.libros[titulo]
        
    def buscar_por_titulo(self,titulo):
        return self.libros.get(titulo)
    
    def libros_por_autor(self,autor):
        lista = []
        for i in self.libros:
            if self.libros[i][0] == autor:
                lista.append(i)
        return lista
    
biblioteca = Biblioteca()
biblioteca.agregar_libro("Libro1","Autor1",2000)
biblioteca.agregar_libro("Libro2","Autor2",2001)
biblioteca.agregar_libro("Libro3","Autor3",2002)
biblioteca.agregar_libro("Libro4","Autor4",2003)
biblioteca.agregar_libro("Libro5","Autor5",2004)

print(biblioteca.libros)
biblioteca.remover_libro("Libro1")
print(biblioteca.libros)
print(biblioteca.buscar_por_titulo("Libro2"))
print(biblioteca.libros_por_autor("Autor3"))





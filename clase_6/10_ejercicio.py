"""
Crear un programa que tenga dos modelos: Biblioteca y Libro.

Atributos de Libro: titulo, autor, año
Atributos de Biblioteca: nombre, libros (lista de instancias de Libro)
Métodos de Biblioteca: agregar(libro: Libro), eliminar, listar

- Crear 3 libros, agregarlos a la biblioteca y listarlos
"""


class Libro:
    def __init__(self, titulo: str, autor: str, año: int):
        self.titulo = titulo
        self.autor = autor
        self.año = año


class Biblioteca:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.libros: list[Libro] = []

    def agregar_libro(self, libro: Libro):
        self.libros.append(libro)

    def eliminar_libro(self, libro: Libro):
        if libro in self.libros:
            self.libros.remove(libro)
        else:
            print(f"❌ El libro {libro.titulo} no está en la biblioteca")

    def listar_libros(self):
        print(f"Libros de la Biblioteca {self.nombre}")
        for libro in self.libros:
            print(f"- {libro.titulo} de {libro.autor} ({libro.año})")


libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
libro2 = Libro("1984", "George Orwell", 1949)
libro3 = Libro("Órganon", "Aristóteles", -384)

biblioteca = Biblioteca("Mi Gran Biblioteca")
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)
biblioteca.agregar_libro(libro3)
biblioteca.listar_libros()
biblioteca.eliminar_libro(libro2)
biblioteca.eliminar_libro(libro2)
print()
biblioteca.listar_libros()

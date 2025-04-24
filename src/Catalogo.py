class Catalogo:
    def __init__(self, titulo, autor, isbn, año, genero, libros=0):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.año = año
        self.genero = genero
        self.libros = libros
        self.disponible = True if libros > 0 else False

    def agregar_libros(self, cantidad=1):
        self.libros += cantidad
        self.disponible = True

    def eliminar_libro(self, cantidad=1):
        if self.libros >= cantidad:
            self.libros -= cantidad
        if self.libros == 0:
            self.disponible = False

    def mostrar_libros(self):
        return f"{self.titulo} ({self.autor}) - ISBN: {self.isbn} - Disponibles: {self.libros}"

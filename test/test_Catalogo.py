import pytest
from src.Catalogo import Catalogo  

# CP – CAT - 01
def test_libro_disponible_al_crear():
    libro = Catalogo("1984", "George Orwell", "111222333", 1949, "Distopía", libros=5)
    assert libro.disponible is True
    assert libro.libros == 5

# CP – CAT - 02
def test_detalle_libro():
    libro = Catalogo("Fahrenheit 451", "Ray Bradbury", "444555666", 1953, "Ciencia ficción", libros=2)
    detalle = libro.mostrar_libros()
    assert "Fahrenheit 451" in detalle
    assert "Ray Bradbury" in detalle
    assert "ISBN: 444555666" in detalle
    assert "Disponibles: 2" in detalle


def test_eliminar_libros_y_desactivar_disponibilidad():
    libro = Catalogo("El Principito", "Antoine de Saint-Exupéry", "777888999", 1943, "Fábula", libros=1)
    libro.eliminar_libro(1)
    assert libro.libros == 0
    assert libro.disponible is False


def test_agregar_libros_y_activar_disponibilidad():
    libro = Catalogo("Don Quijote", "Miguel de Cervantes", "123123123", 1605, "Novela", libros=0)
    assert libro.disponible is False
    libro.agregar_libros(3)
    assert libro.libros == 3
    assert libro.disponible is True

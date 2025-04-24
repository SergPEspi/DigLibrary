import pytest
from datetime import timedelta
from src.Prestamo_Reserva import Prestamo_Reserva
from src.Usuario import Usuario
from src.Catalogo import Catalogo

# CP – P&R 01
def test_prestamo_libro_disponible():
    usuario = Usuario("Juan Pérez", "juanP", "juan@mail.com", "3101234567", "Estudiante", "Ingeniería", "Software")
    libro = Catalogo("1984", "George Orwell", "1234567890", 1949, "Distopía", libros=1)
    prestamo = Prestamo_Reserva(usuario, libro)

    assert prestamo.usuario.nombre == "Juan Pérez"
    assert prestamo.recurso.titulo == "1984"
    assert prestamo.entregado is False
    assert prestamo.penalizado is False

# CP – P&R 02
def test_penalizacion_tardia(monkeypatch):
    usuario = Usuario("Laura Romero", "lauraR", "laura@mail.com", "310998877", "Profesor", "Educación", "Historia")
    libro = Catalogo("El Hobbit", "Tolkien", "9876543210", 1937, "Fantasía", libros=2)
    prestamo = Prestamo_Reserva(usuario, libro, dias_prestamo=0)

    
    monkeypatch.setattr(prestamo, "fecha_devolucion", prestamo.fecha_inicio - timedelta(days=1))
    assert prestamo.verificar_penalizacion() is True

# CP – P&R 03
def test_devolucion_libro():
    usuario = Usuario("Sofía Márquez", "sofiaM", "sofia@mail.com", "311445566", "Estudiante", "Artes", "Diseño")
    libro = Catalogo("Crimen y Castigo", "Dostoievski", "444333222", 1866, "Clásico", libros=1)
    prestamo = Prestamo_Reserva(usuario, libro)

    prestamo.devolver_libro()

    assert prestamo.entregado is True
    assert libro.libros == 2 

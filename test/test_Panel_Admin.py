import pytest
from src.Panel_Admin import Panel_Admin
from src.Usuario import Usuario
from src.Catalogo import Catalogo

# CP – ADMIN 01
def test_asignar_rol_a_usuario():
    admin = Panel_Admin()
    usuario = Usuario("Ana Torres", "ana123", "ana@mail.com", "3101234567", "Estudiante", "Salud", "Nutrición")
    admin.agregar_usuario(usuario)

    admin.asignar_rol("ana123", "Bibliotecario")
    assert usuario.rol == "Bibliotecario", " El rol no fue actualizado correctamente"

# CP – ADMIN 02
def test_agregar_y_buscar_recurso():
    admin = Panel_Admin()
    libro = Catalogo("Crónica de una Muerte Anunciada", "Gabriel García Márquez", "123456789", 1981, "Novela", libros=2)
    admin.agregar_recurso(libro)

    resultados = admin.buscar_recurso("Crónica")
    assert len(resultados) == 1
    assert resultados[0].titulo == "Crónica de una Muerte Anunciada"

# CP – ADMIN 03
def test_cambiar_estado_usuario():
    admin = Panel_Admin()
    usuario = Usuario("Pedro Mejía", "pedroM", "pedro@mail.com", "3109876543", "Profesor", "Ingeniería", "Software")
    admin.agregar_usuario(usuario)

    admin.cambiar_estado_usuario("pedroM", False)
    assert usuario.activo is False


def test_eliminar_usuario():
    admin = Panel_Admin()
    usuario = Usuario("Laura Ramos", "lauraR", "laura@mail.com", "3017654321", "Estudiante", "Humanidades", "Psicología")
    admin.agregar_usuario(usuario)

    admin.eliminar_usuario("lauraR")
    assert admin.buscar_usuario("lauraR") is None

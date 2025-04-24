import pytest
from src.Usuario import Usuario  

# CP – GESU - 01
def test_registro_usuario_exitoso():
    usuario = Usuario(
        nombre="Camilo Sánchez",
        usuario="Cami102",
        correo="camilo78@ucomepnsar.com",
        telefono="320845431",
        rol="Estudiante",
        facultad="Medicina",
        carrera="Salud"
    )
    assert usuario.nombre == "Camilo Sánchez"
    assert usuario.usuario == "Cami102"
    assert usuario.rol == "Estudiante"
    assert usuario.activo is True

# CP – GESU - 02
def test_usuario_rol_definido():
    usuario = Usuario(
        nombre="Luis Torres",
        usuario="LuisT01",
        correo="luis.torres@ucomepnsar.com",
        telefono="3104456321",
        rol="Profesor",
        facultad="Ingeniería",
        carrera="Sistemas"
    )
    assert usuario.rol == "Profesor"
    assert usuario.facultad == "Ingeniería"

# CP – GESU - 03
def test_usuario_incorrecto():
    usuario = Usuario(
        nombre="María López",
        usuario="MariaL03",
        correo="maria.lopez@ucomepnsar.com",
        telefono="315554789",
        rol="Profesor", 
        facultad="Humanidades",
        carrera="Psicología"
    )
    
    usuario.desactivar_usuario()
    assert usuario.activo is False
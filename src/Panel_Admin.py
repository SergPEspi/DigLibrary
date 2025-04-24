class Panel_Admin:
    def __init__(self):
        self.usuarios = []
        self.recursos = []
        self.prestamos = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def eliminar_usuario(self, usuario_id):
        self.usuarios = [u for u in self.usuarios if u.usuario != usuario_id]

    def asignar_rol(self, usuario_id, nuevo_rol):
        for usuario in self.usuarios:
            if usuario.usuario == usuario_id:
                usuario.rol = nuevo_rol

    def generar_reporte_prestamos(self):
        print("=== Reporte de Préstamos ===")
        for prestamo in self.prestamos:
            print(prestamo)

    def cambiar_estado_usuario(self, usuario_id, estado):
        for usuario in self.usuarios:
            if usuario.usuario == usuario_id:
                usuario.activo = estado

    def agregar_recurso(self, recurso):
        self.recursos.append(recurso)

    def registrar_prestamo(self, prestamo):
        self.prestamos.append(prestamo)
        prestamo.recurso.eliminar_ejemplar() 
    def buscar_usuario(self, usuario_id):
        for usuario in self.usuarios:
            if usuario.usuario == usuario_id:
                return usuario
        return None

    def buscar_recurso(self, titulo):
        return [r for r in self.recursos if titulo.lower() in r.titulo.lower()]

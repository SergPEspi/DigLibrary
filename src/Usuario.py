import uuid

class Usuario: 
    def __init__(self, nombre, usuario, correo, telefono, rol, facultad, carrera): 
        self.nombre = nombre 
        self.usuario = usuario 
        self.correo = correo 
        self.telefono = telefono 
        self.rol = rol 
        self.facultad = facultad 
        self.carrera = carrera 
        self.activo = True

        if self.rol.lower() == "profesor":
            self.codigo_profesor = self.generar_codigo_profesor()
        else:
            self.codigo_profesor = None
 
    def generar_codigo_profesor(self):
        return f"PROF-{str(uuid.uuid4())[:8].upper()}"
 
    def actualizar_datos(self, **kwargs): 
        for atributo, valor in kwargs.items(): 
            setattr(self, atributo, valor) 
 
    def desactivar_usuario(self): 
        self.activo = False 
 
    def __str__(self): 
        descripcion = f"{self.nombre} ({self.rol}) - Activo: {self.activo}"
        if self.codigo_profesor:
            descripcion += f" - Código: {self.codigo_profesor}"
        return descripcion

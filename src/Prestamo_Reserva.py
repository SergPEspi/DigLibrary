from datetime import datetime, timedelta
class Prestamo_Reserva:
    def __init__(self, usuario, recurso, dias_prestamo=7):
        self.usuario = usuario
        self.recurso = recurso
        self.fecha_inicio = datetime.now()
        self.fecha_devolucion = self.fecha_inicio + timedelta(days=dias_prestamo)
        self.entregado = False
        self.penalizado = False

    def devolver_libro(self):
        self.entregado = True
        self.recurso.agregar_libros()  

    def verificar_penalizacion(self):
        if not self.entregado and datetime.now() > self.fecha_devolucion:
            self.penalizado = True
        return self.penalizado

    def mostrar_info_reserva (self):
        estado = "Entregado" if self.entregado else "Pendiente"
        return (f"Usuario: {self.usuario.nombre} - Libro: {self.recurso.titulo} - "
                f"Devolución: {self.fecha_devolucion.date()} - Estado: {estado}")

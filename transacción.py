class Transaccion:
    num_transacciones = 0

    def __init__(self, usuario_origen):
        type(self).num_transacciones += 1
        self.id_transaccion = type(self).num_transacciones
        self.usuario_origen = usuario_origen
        self.estado = "Pendiente"

    def ejecutar(self):
        pass

    @staticmethod
    def normas_transaccion():
        print('Toda transacción completada es definitiva y no admite devoluciones.')

    def __str__(self):
        return f'Transaccion #{self.id_transaccion} | Estado: {self.estado} | Usuario: {self.usuario_origen}'
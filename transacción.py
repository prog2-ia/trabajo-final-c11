class Transaccion(ABC):
    num_transacciones = 0

    def __init__(self, usuario_origen):
        type(self).num_transacciones += 1
        self.__id_transaccion = type(self).num_transacciones
        self.usuario_origen = usuario_origen
        self.estado = "Pendiente"

    @property
    def id_transaccion(self):
        return self.__id_transaccion

    @abstractmethod
    def ejecutar(self):
        pass

    @staticmethod
    def normas_transaccion():
        print('Toda transacción completada es definitiva y no admite devoluciones.')

    def __str__(self):
        return f'Transacción #{self.id_transaccion} | Estado: {self.estado} | Usuario: {self.usuario_origen}'
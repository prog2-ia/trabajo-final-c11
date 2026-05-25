from abc import ABC, abstractmethod
from usuario import Usuario

class Transaccion(ABC):
    num_transacciones: int = 0

    def __init__(self, usuario_origen: Usuario) -> None:
        type(self).num_transacciones += 1
        self.__id_transaccion: int = type(self).num_transacciones
        self.usuario_origen: Usuario = usuario_origen
        self._estado: str = "Pendiente"

    @property
    def id_transaccion(self) -> int:
        return self.__id_transaccion

    @property
    def estado(self) -> str:
        return self._estado

    @estado.setter
    def estado(self, nuevo_estado: str) -> None:
        self._estado = nuevo_estado

    @abstractmethod
    def ejecutar(self) -> None:
        pass

    @staticmethod
    def normas_transaccion() -> None:
        print('Toda transacción completada es definitiva y no admite devoluciones.')

    def __str__(self) -> str:
        return f'Transacción #{self.id_transaccion} | Estado: {self.estado} | Usuario: {self.usuario_origen.nombre}'
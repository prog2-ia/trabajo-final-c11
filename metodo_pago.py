from abc import ABC, abstractmethod

class MetodoPago(ABC):
    def __init__(self, titular: str) -> None:
        self.titular: str = titular

    @abstractmethod
    def procesar_pago(self, cantidad: float) -> bool:
        pass

    def __str__(self) -> str:
        return f'Metodo de pago de {self.titular}'
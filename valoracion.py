from abc import ABC, abstractmethod

class Valoracion(ABC):
    @abstractmethod
    def calcular_nota(self):
        pass

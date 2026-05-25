from metodo_pago import MetodoPago

class Tarjeta(MetodoPago):
    def __init__(self, titular: str, numero_tarjeta: str) -> None:
        super().__init__(titular)
        self.__numero_tarjeta: str = numero_tarjeta

    @property
    def numero_tarjeta(self) -> str:
        return self.__numero_tarjeta

    def procesar_pago(self, cantidad: float) -> bool:
        print(f'Cobrando {round(cantidad, 2)}€ a la tarjeta terminada en {self.numero_tarjeta[-4:]}')
        return True
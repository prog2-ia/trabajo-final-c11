from metodo_pago import MetodoPago

class Transferencia(MetodoPago):
    def __init__(self, titular: str, iban: str) -> None:
        super().__init__(titular)
        self.__iban: str = iban

    def procesar_pago(self, cantidad: float) -> bool:
        print(f'Esperando transferencia de {round(cantidad, 2)}€ a la cuenta terminada en {self.__iban[-4:]}')
        return True
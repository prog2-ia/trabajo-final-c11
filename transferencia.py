from metodo_pago import MetodoPago

class Transferencia(MetodoPago):
    def __init__(self, titular, iban):
        super().__init__(titular)
        self.__iban = iban

    def procesar_pago(self, cantidad):
        print(f'Esperando transferencia de {cantidad} euros a la cuenta {self.iban}...')
        return True
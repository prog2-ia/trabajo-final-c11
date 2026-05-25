from metodo_pago import MetodoPago

class PayPal(MetodoPago):
    def __init__(self, titular: str, email: str) -> None:
        super().__init__(titular)
        self.email: str = email

    def procesar_pago(self, cantidad: float) -> bool:
        print(f'Cobrando {round(cantidad, 2)}€ a la cuenta PayPal: {self.email}')
        return True
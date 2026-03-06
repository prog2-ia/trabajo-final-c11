from transacción import Transaccion

class Pedido(Transaccion):
    def __init__(self, usuario_origen, carrito, metodo_pago):
        super().__init__(usuario_origen)
        self.carrito = carrito
        self.metodo_pago = metodo_pago
        self.total = self.calcular_total()

    def calcular_total(self):
        total = 0
        for prod in self.carrito:
            total += prod.precio()
        return total

    def ejecutar(self):
        if self.estado == 'Pendiente':
            print(f'Procesando pedido de {self.total} euros...')
            self.estado = 'Completada'
            print('Pedido completado.')
        else:
            print('El pedido ya no está pendiente.')
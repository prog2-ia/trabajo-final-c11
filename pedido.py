import copy
from transacción import Transaccion

class Pedido(Transaccion):#
    def __init__(self, usuario_origen, carrito, metodo_pago):
        super().__init__(usuario_origen)
        self.carrito = copy.deepcopy(list(carrito))
        self.metodo_pago = metodo_pago
        self.total = sum(prod.precio() for prod in self.carrito)

    def __len__(self):
        return len(self.carrito) #Cuantos productos hay en el carrito

    def __bool__(self):
        return len(self.carrito) > 0 # true si en el pedido hay cosas en el carrito
    def ejecutar(self): #Mirar cambios el viernes.
        if self._estado == 'Pendiente':
            print(f'Procesando pedido de {self.total} euros...')
            self._estado = 'Completada'
            print('Pedido completado.')
        else:
            print('El pedido ya no está pendiente.')
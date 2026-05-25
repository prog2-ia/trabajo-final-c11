import copy
from typing import List
from transacción import Transaccion
from producto import Producto
from metodo_pago import MetodoPago
from usuario import Usuario
from excepciones import PedidoVacioException

class Pedido(Transaccion):
    def __init__(self, usuario_origen: Usuario, carrito: List[Producto], metodo_pago: MetodoPago) -> None:
        super().__init__(usuario_origen)
        self.carrito: List[Producto] = copy.deepcopy(list(carrito))
        self.metodo_pago: MetodoPago = metodo_pago
        self.total: float = float(sum(prod.precio() for prod in self.carrito))

    def __len__(self) -> int:
        return len(self.carrito)

    def __bool__(self) -> bool:
        return len(self.carrito) > 0

    def ejecutar(self) -> None:
        if self._estado != 'Pendiente':
            print('El pedido ya no está pendiente.')
            return

        if not self.carrito:
            raise PedidoVacioException('No se puede procesar un pedido porque el carrito está vacío.')

        try:
            print(f'Procesando pedido de {self.total} euros...')
            pago_exitoso: bool = self.metodo_pago.procesar_pago(self.total)
            if pago_exitoso:
                self._estado = 'Completada'
                print('Pedido completado.')
                self.generar_recibo()
        except Exception as e:
            print(f'Ocurrió un error inesperado al procesar el pedido: {e}')

    def generar_recibo(self) -> None:
        nombre_fichero: str = f'recibo_pedido_{self.id_transaccion}.txt'

        try:
            with open(nombre_fichero, 'w', encoding='utf-8') as writer:
                writer.write(f'RECIBO DE PEDIDO #{self.id_transaccion}\n')
                writer.write(f'Usuario: {self.usuario_origen.nombre}\n')
                writer.write('Artículos:\n')
                for prod in self.carrito:
                    writer.write(f'- {prod.nombre} ({prod.marca}): {round(prod.precio(), 2)}€\n')
                writer.write(f'TOTAL pagado: {round(self.total, 2)}€\n')

            print(f'Recibo generado con éxito en {nombre_fichero}')
        except OSError as e:
            print(f'Error de disco al escribir el recibo: {e}')
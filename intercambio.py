from typing import List
from transacción import Transaccion
from usuario import Usuario
from producto import Producto

class Intercambio(Transaccion):
    def __init__(self, usuario_origen: Usuario, usuario_destino: Usuario, ofrecemos: List[Producto], solicitamos: List[Producto]) -> None:
        super().__init__(usuario_origen)
        self.usuario_destino: Usuario = usuario_destino
        self.ofrecemos: List[Producto] = ofrecemos
        self.solicitamos: List[Producto] = solicitamos

    def ejecutar(self) -> None:
        if self.estado == 'Pendiente':
            print(f'Ejecutando intercambio entre {self.usuario_origen.nombre} y {self.usuario_destino.nombre}...')
            self.estado = 'Completada'
        else:
            print('El intercambio ya no está pendiente.')
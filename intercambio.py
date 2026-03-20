from transacción import Transaccion

class Intercambio(Transaccion):#
    def __init__(self, usuario_origen, usuario_destino, ofrecemos, solicitamos):
        super().__init__(usuario_origen)
        self.usuario_destino = usuario_destino
        self.ofrecemos = ofrecemos
        self.solicitamos = solicitamos

    def ejecutar(self): #Gestionar en clase, decidir que hacer.
        if self.estado == 'Pendiente':
            print(f'Ejecutando intercambio entre {self.usuario_origen} y {self.usuario_destino}...')
            self.estado = 'Completada'
        else:
            print('El intercambio ya no está pendiente.')
from pedido import Pedido
from cromos import Cromos
from figuras import Figura
class Stats:
    @staticmethod
    def total_ventas(lista_transacciones):#
        total = 0
        for transaccion in lista_transacciones:
            if isinstance(transaccion, Pedido):
                total += transaccion.total
        return total

    @staticmethod
    def usuario_con_mas_saldo(lista_usuarios):
        if not lista_usuarios:
            return None

        usuario_top = lista_usuarios[0]
        for usuario in lista_usuarios:
            if usuario.saldo > usuario_top.saldo:
                usuario_top = usuario
        return usuario_top

    @staticmethod
    def contar_tipos_productos(inventario):
        num_cromos = 0
        num_figuras = 0

        for prod in inventario.productos:
            if isinstance(prod, Cromos):
                num_cromos += 1
            elif isinstance(prod, Figura):
                num_figuras += 1

        print(f'Estadísticas del inventario: {num_cromos} Cromos | {num_figuras} Figuras')
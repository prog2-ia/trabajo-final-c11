from cromos import *
from figuras import *
from inventario import *
from paypal import *
from pedido import *
from usuario import *
from stats import *

def main():
    print(' DEMOSTRACIÓN DEL SISTEMA DE COLECCIONISMO')

    # Incorporación de objetos
    print('COMPROBANDO ENCAPSULAMIENTO Y VALIDACIONES (SETTERS)')
    usuario1 = Usuario(1, "David", "david@gmail.com", 300.0)
    #usuario = id, nombre, email, saldo

    # Comprobación de error en la validación del correo
    usuario1.email = 'david_sin_gmail'

    # Comprobación de la validación del estado (debe imprimir error y asignar 0 al estado
    cromo_error = Cromos('Blastoise', 'Pokemon', 'Primera edición', 100, 18)
    #cromos = Nombre, marca, edición, copias y estado

    # Incorporación de objetos válidos
    cromo1 = Cromos('Ho-oh', 'Pokemon', 'Segunda edición', 10000, 9)
    cromo2 = Cromos('Lugia', 'Pokemon', 'Segunda edición', 10000, 7)
    figura1 = Figura('Malenia', 'Elden Ring', 'Segunda Fase', 10000, 15, 10, 8, 9)

    # Uso de Inventario y métodos mágicos
    print('SOBRECARGA DE MÉTODOS ESPECIALES (__add__, __len__, __bool__')
    mi_inventario = Inventario()
    mi_inventario.agregar_producto(usuario1)
    # agregar_producto es un metodo de inventario

    # Añadir objetos al inventario por medio del metodo magico __add__
    inventario_actualizado = mi_inventario + figura1
    inventario_actualizado.agregar_producto(cromo2)

    print(f'Cantidaddd de productos en el inventario actualizado: {len(inventario_actualizado)}')
    print(f'Valor total del inventario: {inventario_actualizado.valor_total()} €')

    # Transacciones, Clases Abstractas y Polimorfismo
    print('TRANSACCIONES Y POLIMORFISMO')
    metodo_paypal = PayPal('David', 'david@gmail.com')

    # Creación de un pedido con el carrito del usuario ya creado
    pedido_david = Pedido(usuario1, inventario_actualizado.productos, metodo_paypal)

    # Al ejecutar,  el pedido llamará a procesar_pago() de la clase PayPal
    pedido_david.ejecutar()
    # ejecutar es un metodo de la clase pedido

    # Uso de métodos estáticos(stats)
    print('ESTADÍSTICAS Y MÉTODOS ESTÁTICOS')
    Stats.contar_tipos_productos(inventario_actualizado)

    lista_transacciones = [pedido_david]
    total_recaudado = Stats.total_ventas(lista_transacciones)
    print(f'El total recaudado por las ventas completadas es: {total_recaudado} €')

if name == '__main__':
    main()
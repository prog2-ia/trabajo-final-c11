from inventario import Inventario
from paypal import PayPal
from usuario import Usuario
from gestor_usuario import GestorUsuarios
from pedido import Pedido
from cromos import Cromos
from figuras import Figura
from excepciones import (
    EmailInvalidoException,
    UsuarioDuplicadoException,
    ProductoDuplicadoException,
    PedidoVacioException
)


def mostrar_menu() -> None:
    print('\n==================================================')
    print('   SISTEMA DE GESTIÓN DE TIENDA DE COLECCIONISMO  ')
    print('==================================================')
    print('1. Crear y registrar un nuevo Usuario')
    print('2. Mostrar todos los Usuarios registrados (Fichero)')
    print('3. Añadir un Cromo al Inventario global')
    print('4. Añadir una Figura al Inventario global')
    print('5. Mostrar Inventario global y su valor total')
    print('6. Simular procesamiento de Pedido (Carrito)')
    print('7. Salir de la aplicación')
    print('==================================================')


def main() -> None:
    gestor = GestorUsuarios()
    inventario = Inventario()

    # Añadimos unos datos base para que el sistema no empiece vacío
    cromo_base = Cromos('Ho-oh', 'Pokemon', 'Neo Revelation', 5, 9)
    inventario.agregar_producto(cromo_base)

    while True:
        mostrar_menu()
        opcion = input('Seleccione una opción (1-7): ').strip()

        if opcion == '1':
            print('\n--- CREAR NUEVO USUARIO ---')
            try:
                id_u = int(input('ID de usuario (número): '))
                nombre = input('Nombre del usuario: ')
                email = input('Email (debe ser @gmail.com o @hotmail.com): ')
                saldo = float(input('Saldo inicial (€): '))

                nuevo_usuario = Usuario(id_u, nombre, email, saldo)
                gestor.añadir_usuario(nuevo_usuario)
            except ValueError:
                print('Error: El ID debe ser un número entero y el saldo un número decimal.')
            except EmailInvalidoException as e:
                print(f'Capturado error de validación: {e}')
            except UsuarioDuplicadoException as e:
                print(f'Aviso del sistema: {e}')

        elif opcion == '2':
            print('\n--- LISTA DE USUARIOS EN BASE DE DATOS (PICKLE) ---')
            usuarios = gestor.usuarios
            if not usuarios:
                print('No hay usuarios registrados todavía.')
            else:
                for u in usuarios:
                    print(u)

        elif opcion == '3':
            print('\n--- AÑADIR CROMO AL INVENTARIO ---')
            try:
                nombre = input('Nombre del cromo: ')
                marca = input('Marca (ej: Pokemon, Magic): ')
                edicion = input('Edición: ')
                copias = int(input('Número de copias existentes: '))
                estado = int(input('Nota de estado (0 al 10): '))

                nuevo_cromo = Cromos(nombre, marca, edicion, copias, estado)
                inventario += nuevo_cromo
            except ValueError:
                print('Error: Las copias y el estado deben ser números enteros.')
            except ProductoDuplicadoException as e:
                print(f'Error del inventario: {e}')

        elif opcion == '4':
            print('\n--- AÑADIR FIGURA AL INVENTARIO ---')
            try:
                nombre = input('Nombre de la figura: ')
                marca = input('Marca (ej: Funko, Hot Toys): ')
                modelo = input('Modelo: ')
                copias = int(input('Número de copias existentes: '))
                alto = float(input('Alto (cm): '))
                ancho = float(input('Ancho (cm): '))
                largo = float(input('Largo (cm): '))
                estado = int(input('Nota de estado (0 al 10): '))

                nueva_figura = Figura(nombre, marca, modelo, copias, alto, ancho, largo, estado)
                inventario += nueva_figura
            except ValueError:
                print('Error: Verifique que las dimensiones y cantidades sean numéricas.')
            except ProductoDuplicadoException as e:
                print(f'Error del inventario: {e}')

        elif opcion == '5':
            print('\n--- INVENTARIO ACTUAL ---')
            if len(inventario) == 0:
                print('El inventario global está vacío.')
            else:
                for i, prod in enumerate(inventario.productos):
                    print(f'[{i}] {prod} | Precio estimado: {round(prod.precio(), 2)}€')
                print(f'>> VALOR TOTAL DEL INVENTARIO: {round(inventario.valor_total(), 2)}€')

        elif opcion == '6':
            print('\n--- SIMULACIÓN DE PEDIDO ---')
            if not gestor.usuarios:
                print('Error: Primero debes registrar un usuario (Opción 1) para asignarle el pedido.')
                continue
            if len(inventario) == 0:
                print('Error: No hay productos en el inventario para comprar.')
                continue

            print('Usuarios disponibles:')
            for u in gestor.usuarios:
                print(f'  ID: {u.id_usuario} - {u.nombre}')

            try:
                id_sel = int(input('Introduce el ID del usuario que compra: '))
                usuario_comprador = gestor.buscar_usuario(id_sel)

                if not usuario_comprador:
                    print('Usuario no encontrado.')
                    continue

                print('\nProductos disponibles en inventario:')
                for i, prod in enumerate(inventario.productos):
                    print(f'  Index [{i}]: {prod.nombre} - {round(prod.precio(), 2)}€')

                idx_sel = int(input('Elige el índice del producto para el carrito (o -1 para simular carrito vacío): '))

                carrito_simulado = []
                if idx_sel != -1:
                    if 0 <= idx_sel < len(inventario):
                        carrito_simulado.append(inventario.productos[idx_sel])
                    else:
                        print('Índice de producto inválido.')
                        continue

                metodo_pago = PayPal(usuario_comprador.nombre, usuario_comprador.email)
                pedido = Pedido(usuario_comprador, carrito_simulado, metodo_pago)
                pedido.ejecutar()

            except ValueError:
                print('Error: Introduce números válidos para las selecciones.')
            except PedidoVacioException as e:
                print(f'Operación cancelada por el sistema: {e}')
            except Exception as e:
                print(f'Error inesperado en la transacción: {e}')

        elif opcion == '7':
            print('\nCerrando la aplicación de coleccionismo. ¡Hasta pronto!')
            break
        else:
            print('\nOpción no válida. Por favor, introduzca un número del 1 al 7.')


if __name__ == '__main__':
    main()
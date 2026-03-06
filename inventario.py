class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)
        print(f'Añadido: {producto.nombre}')

    def valor_total(self):
        total = 0
        for prod in self.productos:
            total += prod.precio()
        return total

    def __str__(self):
        return f'Inventario con {len(self.productos)} productos. Valor total: {self.valor_total()} euros.'

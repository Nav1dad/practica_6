class Articulo:
    def __init__(self, nombre, cantidad, precio):
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def vender(self, cantidad_vendida):
        if cantidad_vendida <= self.cantidad:
            self.cantidad -= cantidad_vendida
            total_venta = cantidad_vendida * self.precio
            return f"Venta exitosa. Total a pagar: ${total_venta:.2f}"
        else:
            return "No hay suficiente cantidad disponible para la venta."

    def agregar_stock(self, cantidad_nueva):
        self.cantidad += cantidad_nueva
        return f"Se han agregado {cantidad_nueva} unidades al stock de {self.nombre}."

    def __str__(self):
        return f"Producto: {self.nombre}\nStock disponible: {self.cantidad}\nPrecio por unidad: ${self.precio:.2f}"


if __name__ == "__main__":
    producto1 = Articulo("Camiseta", 50, 15.99)
    print(producto1)

    print("\nRealizando una venta...")
    resultado_venta = producto1.vender(10)
    print(resultado_venta)
    print(producto1)

    print("\nAgregando stock...")
    resultado_stock = producto1.agregar_stock(20)
    print(resultado_stock)
    print(producto1)
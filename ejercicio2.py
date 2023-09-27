class Usuario:
    def __init__(self, nombre, apellido, email, saldo_inicial=0.0):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.saldo = saldo_inicial

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            return f"Depósito exitoso. Nuevo saldo: ${self.saldo:.2f}"
        else:
            return "La cantidad de depósito debe ser mayor que cero."

    def retirar(self, cantidad):
        if cantidad > 0:
            if cantidad <= self.saldo:
                self.saldo -= cantidad
                return f"Retiro exitoso. Nuevo saldo: ${self.saldo:.2f}"
            else:
                return "Fondos insuficientes para realizar el retiro."
        else:
            return "La cantidad de retiro debe ser mayor que cero."

    def consultar_saldo(self):
        return f"Saldo actual: ${self.saldo:.2f}"

    def __str__(self):
        return f"Nombre: {self.nombre} {self.apellido}\nEmail: {self.email}\nSaldo: ${self.saldo:.2f}"


if __name__ == "__main__":
    usuario1 = Usuario("Juan", "Pérez", "juan@example.com", 1000.0)
    print(usuario1)

    print("\nRealizando un depósito...")
    resultado_deposito = usuario1.depositar(500.0)
    print(resultado_deposito)
    print(usuario1)

    print("\nRealizando un retiro...")
    resultado_retiro = usuario1.retirar(300.0)
    print(resultado_retiro)
    print(usuario1)

    print("\nConsultando saldo...")
    saldo_actual = usuario1.consultar_saldo()
    print(saldo_actual)
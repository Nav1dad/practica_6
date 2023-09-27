# class padre
class Figura:
    nombre = ""

    def area(self):
        pass

    def getFigura(self):
        return self.nombre


# class hija
class Triangulo(Figura):
    def __init__(self, _nombre, _base, _altura):
        self.nombre = _nombre
        self.base = _base
        self.altura = _altura

    def area(self):
        return (self.base * self.altura) / 2

class Cuadrado(Figura):
    def __init__(self, _nombre, _base, _altura):
        self.nombre = _nombre
        self.base = _base
        self.altura = _altura
    
    def area(self):
        return self.base * self.altura


triangulo = Triangulo("equilatero", 10, 5)
print(f"El area de el triangulo {triangulo.getFigura()} es {triangulo.area()}")

cuadrado = Cuadrado("cuadrado", 10, 10)
print(f"El area de un cuadrado {cuadrado.getFigura()} es {cuadrado.area()}")

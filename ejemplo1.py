# creando una clase
class Personas:
    nombre = ""
    apellido = ""
    genero = ""
    edad = ""
    estado_civil = ""

    # parametros
    def __init__(self, _nombre, _apellido, _genero):
        self.nombre = _nombre
        self.apellido = _apellido
        self.genero = _genero

    # Metodo
    def hablar(self, mensaje):
        print(mensaje)


# creando un objeto
# objeto es una instancia de la clase
# instancionar es crear un objeto a partir de una clase

persona1 = Personas("Pedro", "Alvarez", "Masculino")
persona2 = Personas("Antonio", "Hernandez", "Masculino")

print(f"{persona1.nombre} {persona1.apellido}")
print(f"{persona2.nombre} {persona2.apellido}")

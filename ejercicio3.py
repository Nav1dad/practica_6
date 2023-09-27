class Estudiante:
    def __init__(self, nombre, apellido, carnet, carrera):
        self.nombre = nombre
        self.apellido = apellido
        self.carnet = carnet
        self.carrera = carrera

    def actualizar_nombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def actualizar_apellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def actualizar_carnet(self, nuevo_carnet):
        self.carnet = nuevo_carnet

    def actualizar_carrera(self, nueva_carrera):
        self.carrera = nueva_carrera

    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nCarnet: {self.carnet}\nCarrera: {self.carrera}"

if __name__ == "__main__":
    estudiante1 = Estudiante("Juan", "Pérez", "202345678", "Ingeniería Informática")
    print(estudiante1)

    estudiante1.actualizar_nombre("María")
    print("\nNombre actualizado:")
    print(estudiante1)

   
    estudiante1.actualizar_carrera("Ingeniería Eléctrica")
    print("\nCarrera actualizada:")
    print(estudiante1)

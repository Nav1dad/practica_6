class Biblioteca:
    def __init__(self, _libros):
        self.libros = _libros
    
    # Mostrar libros.    
    def mostraLibros(self):
        for libro in self.libros:
            print(libro)
            
    def prestarLibros(self, nombreLibros):
        # verificar si el libro existe
        if nombreLibros in self.libros:
            print("Se presto el libro", nombreLibros)
            self.libros.remove(nombreLibros)
        else:
            print("El libro no existe")
            
    def agregarLibros(self, nombreLibros):
        # Verifircar que el libro no exista
        if nombreLibros not in self.libros:
            print("Se añadio el libro", nombreLibros)
            self.libros.append(nombreLibros)
        else:
            print("El libro ya existe")
            
libros = ["Clean Code" , "Java" , "Analisis"]

biblioteca = Biblioteca(libros)

while True:
    print("1) Agregar Libro")
    print("2) Prestar Libro")
    print("3) Mostrar Libros")
    print("4) Salir")
    
    opcion = int(input("Ingresa una opcion (1-4)"))
    
    if opcion == 1:
        libro = (input("\nIngresa el nombre del libro: "))
        biblioteca.agregarLibros(libro)
    elif opcion == 2:
        libro = (input("\nIngresa el nombre del libro: "))
        biblioteca.prestarLibros(libro)
    elif opcion == 3:
        print("Mis libros son")
        biblioteca.mostraLibros()
    elif opcion == 4:
        break
        
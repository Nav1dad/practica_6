class Perro:
    def sonido(self):
        print("Guuuuuuu!!")
        
class Gato:
    def sonido(self):
        print("Miauuuu!!")
        
class Vaca:
    def sonido(self):
        print("Muuuuuuu!!")
        
        
perro1 = Perro()
gato1 = Gato()
vaca1 = Vaca()

misPersonajes = []

for i in range(0, 10):
    if i%2==0:
        misPersonajes.append(Perro())
        
    elif i%3==0:
        misPersonajes.append(Vaca())
    else:
        misPersonajes.append(Gato())
        
for animal in misPersonajes:
    animal.sonido()
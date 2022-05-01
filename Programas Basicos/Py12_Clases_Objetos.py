class Coordenada:
    # constructor
    def __init__(self, x=0, y=0):
        self.posx = x
        self.posy = y

    def ver(self):
        return self.posx, self.posy

    def mover(self, x, y):
        self.posx = x
        self.posy = y


# crear instancia u objeto
punto_1 = Coordenada(10, 10)
punto_2 = Coordenada(20, 20)
# acceso a funciones
print(punto_1.ver())
print(punto_2.ver())

punto_1.mover(15, 23)
print(punto_1.ver())

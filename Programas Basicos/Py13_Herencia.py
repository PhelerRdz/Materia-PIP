class Coordenada:
    def __init__(self, x, y):
        self.posx = x
        self.posy = y

    def ver(self):
        return self.posx, self.posy

    def mover(self, x, y):
        self.posx = x
        self.posy = y


class Circulo(Coordenada):
    def __init__(self, x, y, r):
        Coordenada.__init__(self, x, y)
        self.radio = r

    def ver(self):
        coord = Coordenada.ver(self)
        return coord[0], coord[1], self.radio


circulo = Circulo(10, 10, 5)
print(circulo.ver())
circulo.mover(5, 5)
print(circulo.ver())

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


class Cuadrado(Coordenada):
    def __init__(self, x, y, l):
        Coordenada.__init__(self, x, y)
        self.lado = l

    def ver(self):
        coord = Coordenada.ver(self)
        return coord[0], coord[1], self.lado


figuras = []
figuras.append(Circulo(10, 10, 5))
figuras.append(Cuadrado(20, 20, 10))
una_figura = Coordenada(0, 0)

for figura in figuras:
    una_figura = figura
    una_figura.mover(5, 5)
    print(una_figura.ver())

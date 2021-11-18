class Calculos:
    def __init__(self,valor):
        self.x = valor

    def calc_quad(self):
        quad = self.x * self.x
        return "o quadrado do número é {}" .format(quad)

    def calc_cubo(self):
        cubo = self.x * self.x * self.x
        return "O cubo do número é {}" .format(cubo)
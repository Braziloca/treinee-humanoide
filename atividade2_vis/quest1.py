class Bola:
    def __init__(self, cor, circ, mat):
        self.cor = cor
        self.cinc = circ
        self.mat = mat

    def change_color(self, nova_cor):
        self.cor = nova_cor
        
    def __str__(self):
        return "A nova cor da bola é {}" .format(self.cor)

bola = Bola("azul", "redondo", "plastico")
mudar = bola.change_color("verde")
print(bola)
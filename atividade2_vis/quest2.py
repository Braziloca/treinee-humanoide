class Motor:
    def __init__(self, id, vel, sent_giro):
        self.id = id
        self.vel = vel
        self.sent_giro = sent_giro

    def change_id(self, novo_id):
        self.id = novo_id
    
    def change_vel(self, nova_vel):
        self.vel = nova_vel

    def change_sg(self, novo_sg):
        self.sg = novo_sg
    
    def __str__(self):
        return "{}, {}, {}".format(self.id, self.vel, self.sg)

class Movimento:
    def __init__(self):
        self.motorA = Motor(1, 0, "parado")
        self.motorB = Motor(2, 0, "parado")


    def para_frente(self):
        self.motorA.change_id(3)
        self.motorA.change_vel(100)
        self.motorA.change_sg("anti-horario")
        self.motorB.change_id(4) 
        self.motorB.change_vel(100)
        self.motorB.change_sg("anti-horario")

    def para_tras(self):
        self.motorA.change_id(5)
        self.motorA.change_vel(100)
        self.motorA.change_sg("horario")
        self.motorB.change_id(6) 
        self.motorB.change_vel(100)
        self.motorB.change_sg("horario")

    def girar(self):
        self.motorA.change_id(7)
        self.motorA.change_vel(50)
        self.motorA.change_sg("anti-horario")
        self.motorB.change_id(8) 
        self.motorB.change_vel(50)
        self.motorB.change_sg("horario")

    def parar(self):
        self.motorA.change_id(9)
        self.motorA.change_vel(0)
        self.motorA.change_sg("parado")
        self.motorB.change_id(10) 
        self.motorB.change_vel(0)
        self.motorB.change_sg("parado")

    def __str__(self):
        return "Motor A: {}\nMotor B: {}" .format(self.motorA, self.motorB)
    
'''TESTES'''
mov = Movimento()
#mov.para_frente()
#mov.para_tras()
mov.girar()
#mov.parar()
print(mov) 


     
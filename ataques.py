

class personaje:
    def __init__(self, vida, ataque, defensa):
        self.ataque= ataque
        self.defensa=defensa
        self.vida=vida
Superman=personaje(500,120,50)
Goku=personaje(400,100,40)



def atacar(x,y):
    dano=(x.ataque-y.defensa)
    y.vida=y.vida-dano
    if y.vida<=0:
        return ('K.O')
    else:
        return (y.vida)

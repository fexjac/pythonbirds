class Carro:
    def __init__(self, direcao, motor):
        self.direcao = direcao
        self.motor = motor

    def calcular_velocidade(self):
        velocidade = motor.velocidade
        return velocidade

    def calcular_direcao(self):
        direcao = self.direcao.valor()
        return direcao

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.acelerar()

    def girar_a_direita(self):
        self.direcao.girar_a_direita()

    def girar_a_esquerda(self):
        self.direcao.girar_a_esquerda()

class Motor:

    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        if self.velocidade >= 2:
            self.velocidade -=2
        elif self.velocidade == 1:
            self.velocidade -= 1
        else:
            print('O carro está parado')


class Direcao:

    def __init__(self):
        self.direcao = ('Norte', 'Leste', 'Sul', 'Oeste')
        self.posicao_direcao = 0

    def girar_a_direita(self):
        if self.posicao_direcao != 3:
            self.posicao_direcao += 1
        else:
            self.posicao_direcao = 0

    def girar_a_esquerda(self):
        if self.posicao_direcao != 0:
            self.posicao_direcao -= 1
        else:
            self.posicao_direcao = 3


    def valor(self):
        posicao_direcao = self.posicao_direcao
        direcao = self.direcao[posicao_direcao]
        return direcao



if __name__ == '__main__':
    print('# Testando motor')
    motor = Motor()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.acelerar()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    motor.frear()
    print(motor.velocidade)
    print('# Testando direcao')
    direcao = Direcao()
    print(direcao.valor())
    direcao.girar_a_direita()
    print(direcao.valor())
    direcao.girar_a_direita()
    print(direcao.valor())
    direcao.girar_a_direita()
    print(direcao.valor())
    direcao.girar_a_direita()
    print(direcao.valor())
    direcao.girar_a_esquerda()
    print(direcao.valor())
    direcao.girar_a_esquerda()
    print(direcao.valor())
    direcao.girar_a_esquerda()
    print(direcao.valor())
    direcao.girar_a_esquerda()
    print(direcao.valor())

    carro = Carro(direcao, motor)
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.acelerar()
    print(carro.calcular_velocidade())
    carro.frear()
    print(carro.calcular_velocidade())
    print(carro.calcular_direcao())
    carro.girar_a_direita()
    print(carro.calcular_direcao())
    carro.girar_a_esquerda()
    print(carro.calcular_direcao())
    carro.girar_a_esquerda()
    print(carro.calcular_direcao())
"""
Você deve criar uma classe carro que vai possuir
dois atributos compostos por outras duas classes:

Motor
Direção
O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:

Atributo de dado velocidade
Método acelerar, que deverá incremetar a velocidade de uma unidade
Método frear que deverá decrementar a velocidade em duas unidades
A Direção terá a responsabilidade de controlar a direção. Ela oferece
os seguintes atributos:

Valor de diração com valores possíveis: Norte, Sul, Leste, Oeste.
Método girar_a_direita
Método girar_a_esquerda
       N
    O     L
       S

Exemplo:
    >>> # Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> # Testando Direcao
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.calcular_direcao()
    'Oeste'

"""
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
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)


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
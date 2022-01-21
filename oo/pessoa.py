class Pessoa:
    def __init__(self, *filhos, nome=None, idade=32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

if __name__ == '__main__':
    nico = Pessoa(nome='Nico')
    sophia = Pessoa(nome='Sophia')
    jaison = Pessoa(nico, sophia, nome='Jaison')
    print(Pessoa.cumprimentar(jaison))
    print(id(jaison))
    print(jaison.cumprimentar())
    print(jaison.nome)
    print(jaison.idade)
    for filho in jaison.filhos:
        print(filho.nome)
    jaison.sobrenome = 'Costa'
    del jaison.filhos
    print(jaison.__dict__)
    print(nico.__dict__)
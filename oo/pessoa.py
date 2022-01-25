class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=32):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá{id(self)}'

    @staticmethod
    def metodo_estatico():
        return 35

    @classmethod
    def nome_e_atributos_da_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

class Mutante(Pessoa):
    olhos = 3
    pass

if __name__ == '__main__':
    nico = Mutante(nome='Nico')
    sophia = Homem(nome='Sophia')
    jaison = Homem(nico, sophia, nome='Jaison')
    print(Pessoa.cumprimentar(jaison))
    print(id(jaison))
    print(jaison.cumprimentar())
    print(jaison.nome)
    print(jaison.idade)
    for filho in jaison.filhos:
        print(filho.nome)
    jaison.sobrenome = 'Costa'
    del jaison.filhos
    jaison.olhos=1
    print(jaison.__dict__)
    print(nico.__dict__)
    print(Pessoa.olhos)
    print(nico.olhos)
    print(sophia.olhos)
    print(jaison.olhos)
    print(id(Pessoa.olhos), id(nico.olhos), id(sophia.olhos), id(jaison.olhos))
    Pessoa.olhos = 2
    del jaison.olhos
    print(Pessoa.olhos)
    print(nico.olhos)
    print(sophia.olhos)
    print(jaison.olhos)
    print(id(Pessoa.olhos), id(nico.olhos), id(sophia.olhos), id(jaison.olhos))
    print(Pessoa.metodo_estatico(), jaison.metodo_estatico())
    print(Pessoa.nome_e_atributos_da_classe(), jaison.nome_e_atributos_da_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(jaison, Pessoa))
    print(isinstance(jaison, Homem))
    print(nico.olhos)

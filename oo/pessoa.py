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
    jaison.olhos=1
    print(jaison.__dict__)
    print(nico.__dict__)
    print(Pessoa.olhos)
    print(nico.olhos)
    print(sophia.olhos)
    print(jaison.olhos)
    print(id(Pessoa.olhos), id(nico.olhos), id(sophia.olhos), id(jaison.olhos))
    Pessoa.olhos = 3
    del jaison.olhos
    print(Pessoa.olhos)
    print(nico.olhos)
    print(sophia.olhos)
    print(jaison.olhos)
    print(id(Pessoa.olhos), id(nico.olhos), id(sophia.olhos), id(jaison.olhos))
    print(Pessoa.metodo_estatico(), jaison.metodo_estatico())
    print(Pessoa.nome_e_atributos_da_classe(), jaison.nome_e_atributos_da_classe())

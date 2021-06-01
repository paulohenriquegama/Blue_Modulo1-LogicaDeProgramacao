'''class Heroi:
    def __init__(self,nome, idade = 30,habilidade = 'magia'):
        self.nome = nome
        self.idade = idade
        self.habilidade = habilidade
        

    def usar_habilidade(self):
        print(f"{self.nome} está usando sua habilidade: {self.habilidade}.")

nome = input("Digite o nome: ")
heroi = Heroi(nome)
heroi.idade = 32
print(vars(heroi))
for a,v in heroi.
'''
class Pessoa:
    def __init__(self, nome, sexo, cpf, ativo):
        self.__nome = nome
        self.__sexo = sexo
        self.__cpf = cpf
        self.__ativo = ativo

    def desativar(self):
        self.ativo = False
        print('Apessoa foi desativada com sucesso')

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome


    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


if __name__ == '__main__':
    pessoa1 = Pessoa('Marcos', 'M', '123456', True)
    pessoa1.desativar()
    pessoa1.ativo = True
    print(pessoa1.ativo)
    pessoa1.nome = "Paulo"
    print(pessoa1.nome)
    #utilizando getter e setters
    pessoa1.set_nome('Joao')
    print(pessoa1.get_nome())
    print(pessoa1.nome)

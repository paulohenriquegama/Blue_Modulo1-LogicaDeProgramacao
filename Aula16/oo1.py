class Heroi:
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
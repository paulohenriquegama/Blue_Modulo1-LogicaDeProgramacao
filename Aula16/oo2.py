class Pessoa:
    def __init__(self, nome, sexo, cpf, ativo):
        self.__nome = nome
        self.__sexo = sexo
        self.cpf = cpf
        self.__ativo = ativo
       

    def desativar(self):
        self.ativo = False
        print('Apessoa foi desativada com sucesso')

    def mostrarnome(self):
        return self.__nome
    
    def mudarNome(self,nome):
        self.__nome = nome

class Conta(Pessoa):

    def __init__(self,saldo):
        self.saldo = saldo
         

    def depositar(self,valor):
        self.saldo += valor

    def sacar(self,valor):
        self.saldo -= valor
    
    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self,valor):
        if isinstance(valor,str):
            valor = float(valor.replace(",", "."))
        self._saldo = valor

        


p = Pessoa("Paulo", "M", '09039291470',True)
print(p.mostrarnome())
p.__nome = "João"
print(p.__nome)
print(p.mostrarnome())
p.mudarNome("Zé")
#print(p.__nome)
print(p.mostrarnome())
saldo = input("Digite um valor do saldo incial: ")
c = Conta(saldo)
print(c.saldo)
c.depositar(200.5)
print(c.saldo)

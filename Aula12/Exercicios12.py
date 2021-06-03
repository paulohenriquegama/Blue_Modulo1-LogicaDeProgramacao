#Questão 1
'''l1 = [1,4,5,6,7,9]
l2 = []

for cont in l1:
    l2.append(cont**2)

dic = dict(zip(l1,l2))
print(dic)'''



# Questão 2
'''
l1 = []
l2 = []

for cont in range(1,11):
    l1.append(cont)
    l2.append(cont**2)

dic = dict(zip(l1,l2))
print(dic)'''

#Questão 3
'''
opc = 0
while opc == 0:
    nome = input("Digite o nome do aluno: ")
    media = float(input("Digite a média: "))
    def med(media):
        if media>=7:
            return "Aprovado"
        elif media <5:
            return "Reprovado"
        else:
            return "Recuperação"


    dic = {'nome':nome,'media':media,'situação':med(media)}

    print(dic)
    resp = input("Deseja continuar: s/n? ")
    if resp == 'n':
        opc = 1
print("Programa finalizado!!")
'''
#Questão 4

'''from os import readlink
import random
import time
import operator

jogadores = {'Jogador 1':random.randint(1,6),'Jogador 2':random.randint(1,6),
             'Jogador 3':random.randint(1,6),'Jogador 4':random.randint(1,6)}
rank = list()
for k,v in jogadores.items():
    print(f'O {k} tirou {v} no dado.')
    rank.append(v)
    time.sleep(2)

rank = sorted(jogadores.items(), key=operator.itemgetter(1),reverse=True)
print("RANKING!!")
for i,v in enumerate(rank):
    print(F'{i+1}º lugar foi o {v[0]} que tirou {v[1]} nos dados.')
    time.sleep(1)
'''

#Questão 5
'''import datetime
import operator
nome = input("Qual seu nome? ")
anoNasc = int(input("Digite o ano de nascimento: "))
carteira = input("Tem carteira registrada? se não digite 0: ")
data_atual = datetime.date.today()
ano_atual = int(data_atual.year)

if carteira != '0':
    anoContrato = int(input("Digite o ano que foi contratado: "))
    salario = float(input("Digite o seu salario: "))
    temp_aposentar = 35 - (ano_atual - anoContrato)
    dic = {'nome': nome,'idade':ano_atual-anoNasc,'ano_aposentadoria': temp_aposentar+ano_atual}
    print(f'O Seu nome é {dic["nome"]} atualmente tem {dic["idade"]} anos, você ira se aposentar em {dic["ano_aposentadoria"]}')
else:
    dic = {'nome': nome,'idade':ano_atual-anoNasc}
    print(f'O Seu nome é {dic["nome"]} atualmente tem {dic["idade"]} anos, você não possui carteira de trabalho')
'''

# Desafio
opc = 0
cont = 0
nome = []
sexo = []
idade = []
pessoas = []


while opc == 0:
    pessoa = {input("Digite o nome "):[sexo,idade]}
    respSexo = input("Digite o sexo: M/F: ")
    while respSexo not in ("MmFf"):
        respSexo = input("Por favor informe 'F' ou 'M': ")
    sexo.append(respSexo)
    respIdade = int(input("Digite sua idade: "))
    idade.append(respIdade)

    pessoas.append(pessoa)
    resp = input("Deseja continuar? s/n: ")
    while resp not in ("snSN"):
        resp = input("Por favor digite 's' ou 'n': ")
    if resp in ("Nn"):
        opc = 1
media = sum(idade)/len(pessoas)
print()
print("O total de pessoas cadastradas é ", len(pessoas))
print()
print("A media da idade das pessoas cadastradas é ", sum(idade)/len(pessoas))
print()
print("Lista de Mulheres: ")
for i in pessoas:
    for k,v in i.items():
        if sexo[cont] in "Ff":
            print(k)
        cont += 1
print()
cont = 0
print("Pessoas com idade acima de ", media)
for i in pessoas:
    for k,v in i.items():
        if idade[cont] > media:
            print(f'{k} que tem {idade[cont]} anos de idade')
        cont += 1

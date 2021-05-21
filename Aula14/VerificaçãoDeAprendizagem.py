#Questão 1
'''def maior(n1,n2):
    if n1>n2:
        print(f"{n1} é o maior")
    elif n1<n2:
        print(f"{n2} é o maior")
def impopar(n1,n2):
    soma = n1 + n2
    resto = soma%2
    if resto == 0:
        return "par"
    else:
        return "impar" 
def maior40(n1,n2):
    if n1*n2 >40:
        div = (n1*n2)/(n1//n2)
        print("Sim a multiplicação dos dois numeros é maior que 40 e o valor desejado é ", div)
    else:
        print("A multiplicação dos dois números não é maior que 40, pois o resultado é ",n1*n2)
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

print(f"A soma dos valores é {n1+n2:.0f}")
print(f"A multiplicão dos valores é {n1*n2:.0f}")
print(f"A divisão dos valores é {n1//n2:.0f}")
maior(n1,n2)
print("O resultado da soma dos dois numeros é ", impopar(n1,n2))
maior40(n1,n2)'''

#Questão 2
'''frase = input("Digite uma frase: ").lower()
a = 0
e = 0
i = 0
o = 0
u = 0
consoante = 0

for cont in frase:
    if cont in "aáâã":
        a = a+1
    elif cont in "eéê":
        e = e+1
    elif cont in "iíî":
        i = i+1
    elif cont in "oóôõ":
        o = o+1
    elif cont in "uúû":
        u = u+1
    else:
        consoante = consoante+1

print(f"Sua frase tem {a} letra(s) 'a' {e} letra(s) 'e' {i} letra(s) 'i' {o} letra(s) 'o' e {u} letra(s) 'u', além de {consoante} consoantes")

print("A frase digitada sem as vogais fica:")
for cont in frase:
    if cont not in ('aeéêiíîoóôõuúûaáâã'):
        print(cont, end="")
  '''  
#Questão 3
'''import random
import os
import time

senha = input("Cadastre uma senha para entrar no jogo: ")
print("Senha cadastrada com sucesso!!")
time.sleep(0.3)
os.system('cls')

resp = ""
while resp != senha:
    resp = input("Digite a senha: ")
    if resp != senha:
        print("Senha invalida tente novamente!")

print("Seja bem vindo(a) ao jogo da adivinhação!")        

maquina = str(random.randint(1,10))
resp = input("Digite um número: ")
while resp != maquina:
    os.system('cls')
    time.sleep(0.3)
    print("Resposta errada")
    if resp > maquina:
        resp = input("O numero digitado é maior, tente um número menor: ")
        os.system('cls')
        time.sleep(0.5)
    else:
        resp = input("O numero digitado é menor, tente um número maior: ")
        os.system('cls')
        time.sleep(1)

print("Parabéns você acertou o número!!!!")

'''
#Questão 4
'''
import datetime
from time import strptime
opc= 0

def bissexto(ano):
    
        if ano%4==0:
            return 1
            if ano%100==0:
                return 0
                if ano%400==0:
                    return 1
        else:
            return 0

def mesExtenso(data):
    
        dia = int(data[0])
        mes = int(data[1])
        ano = int(data[2])

        if bissexto(ano) == 1:
            if mes == 2:
                if dia <= 0 or dia >29 or mes <1 or mes >12 or ano <1:
                    return print("Data inválida")
                else: 
                    meses = ["Janeiro","Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"] 
                    print(f'{data[0]} de {meses[mes-1]} de {data[2]}')
                    
            else:
                if dia <= 0 or dia >31 or mes <1 or mes >12 or ano <1:
                    return print("Data inválida")
                else: 
                    meses = ["Janeiro","Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"] 
                    print(f'{data[0]} de {meses[mes-1]} de {data[2]}')
        else:
            if mes == 2:
                if dia <= 0 or dia >28 or mes <1 or mes >12 or ano <1:
                    return print("Data inválida")
                else: 
                    meses = ["Janeiro","Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"] 
                    print(f'{data[0]} de {meses[mes-1]} de {data[2]}')
            else:
                if dia <= 0 or dia >31 or mes <1 or mes >12 or ano <1:
                    return print("Data inválida")
                else: 
                    meses = ["Janeiro","Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"] 
                    print(f'{data[0]} de {meses[mes-1]} de {data[2]}')

while opc != 1:
    data = input("Digite uma data no formato 'DD/MM/AAAA: " ).split("/")
    try:
        mesExtenso(data)
    except:
        print("NULL")
    resp = input("Deseja continuar? s/n: ")
    while resp not in ('SsNn'):
        resp = input("Por favor digite 's' ou 'n': ")
    if resp in "nN":
        opc = 1
print("Programa finalizado!!")
'''
# Questão 5
'''
def semvogais(frase):
    vogais = 0
    
    imprimir = []
    for cont in frase:
        if cont not in ('aeéêiíîoóôõuúûaáâã'):
            print(cont, end="")
            imprimir.append(cont)
        else:
            vogais +=1
    return imprimir,print(f'\nForam retiradas {vogais} vogais')
        
frase = input("Digite uma frase: ")
print('Frase impresa sem vogais:')
semvogais(frase)
print()

'''
# Questão 6

'''
perguntas = [input('Telefonou para a vítima? \n')
             ,input('Esteve no local do crime? \n')
             ,input('Mora perto da vítima? \n')
             ,input('Devia para a vítima? \n')
             ,input('Já trabalhou com a vítima? \n')]



sim = 0

for cont in range(5):
    if perguntas[cont] in ('sS'):
        sim += 1
    
sim = perguntas.count('s')
if sim == 2:
    print("Suspeito")
elif sim >2 and sim <5:
    print("Cúmplice")
elif sim == 5:
    print("Culpado")
else:
    print("Inocente")

'''
# Questão 7
'''
impar = []
par = []
lista = [par,impar]
cont = 0
while cont < 7:
    cont +=1
    n1 = int(input(f"Digite o {cont}º numero: "))
    if n1%2 == 0:
        par.append(n1)
    else:
        impar.append(n1)

par.sort()
impar.sort()
print(lista)
'''
# Questão 8

import datetime
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
    print(f'O Seu nome é {dic["nome"]} atualmente tem {dic["idade"]} anos, você ira se aposentar em {dic["ano_aposentadoria"]} com {dic["idade"]+35} anos.')
else:
    dic = {'nome': nome,'idade':ano_atual-anoNasc}
    print(f'O Seu nome é {dic["nome"]} atualmente tem {dic["idade"]} anos, você não possui carteira de trabalho.')

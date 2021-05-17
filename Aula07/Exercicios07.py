#Questão 1
def menor(n1,n2):
    if n1>n2:
        return print(f"{n2} é o menor valor digitado!")
    elif n1<n2:
        return print(f"{n1} é o menor valor digitado!")
    else:
        return print("Valores idênticos")

n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))

menor(n1,n2)

#Questão 2
'''def compara(a,b):
    soma = a+b
    if soma>limite:
        return True
    else:
        return False

limite = 150
n1 = float(input("Digite o primeiro numero: "))
n2 = float(input("Digite o segundo numero: "))
print(compara(n1,n2))'''

#Questão 3

'''def maiscula(stg):
   s =  stg.upper()
   return s

stg = input("Digite uma palavra: ")

print(f"Essa palavra ficou assim '{maiscula(stg)}'em maiúscolo")'''

#Questão 4


'''from datetime import date as dt
def voto(anoNascimento):
    anoAtual = dt.today().year
    idade = anoAtual - anoNascimento
    
    if idade > 18 and idade <=65:
        voto =  "Obrigatorio"
    elif idade<18 or idade > 65:
        voto =  "Opcional"
    else:
        voto =  "Negado"

    return voto

anoNascimento = int(input("Informe o ano de nascimento: "))

print(voto(anoNascimento))'''

#Questão 5
'''def ficha(nome,qtdGols):
    fichaCompleta = [nome,qtdGols]
    return print(f"O nome do jogador é {fichaCompleta[0]} \nEle marcou {fichaCompleta[1]}\n")

nome = input("Digite o nome do jogador: ")
qtdGols = 0
try:
    qtdGols = int(input("Digite a quantidade de gols que ele marcou: "))
except:
    qtdGols = "\nA quantidade de gols informada é invalida "

ficha(nome,qtdGols)'''

#Projeto: Gastos com viagem
'''
def custo_hotel(noites):
    custo = noites*140
    return custo

def custo_aviao(cidade):
    if cidade in ("SP",'sp'):
        passagem = 312
    elif cidade in ("PA",'pa'):
        passagem = 447
    elif cidade in ("RC",'rc'):
        passagem = 831
    elif cidade in ("MN",'mn'):
        passagem = 986
    return passagem

def custo_carro(qtdDias):
    custo = qtdDias*40
    if qtdDias >= 7:
        custo = custo -50
    elif qtdDias >= 3:
        custo = custo-20
    return custo

def custo_total(cidade,qtdDias,gastos_estras):
    noites = int(input(f"Você irá dormir quantas noites em {cidade}? : "))
    valorTotal = custo_hotel(noites) + custo_aviao(cidade) + custo_carro(qtdDias)
    valorTotal = valorTotal + gastos_estras
    return valorTotal

cidade = input("Digite a cidade de destino, 'SP' para São Paulo, 'PA' para Porto Alegre, 'RC' para Recife ou 'MN' para Manaus: ")

qtdDias = int(input(f"Informe a quantidade de dias da sua viagem para {cidade}: "))
gastos_estras = float(input("Informe o valor caso tenha tido algum gasto extra, se não digite 0: "))

print(f"O custo para viagem informada é {custo_total(cidade,qtdDias,gastos_estras)}")'''





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
def ficha(nome,qtdGols):
    fichaCompleta = [nome,qtdGols]
    return print(f"O nome do jogador é {fichaCompleta[0]} \nEle marcou {fichaCompleta[1]}\n")

nome = input("Digite o nome do jogador: ")
qtdGols = 0
try:
    qtdGols = int(input("Digite a quantidade de gols que ele marcou: "))
except:
    qtdGols = "\nA quantidade de gols informada é invalida "

ficha(nome,qtdGols)

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

print(f"A soma dos valor é {n1+n2:.0f}")
print(f"A multiplicão dos valor é {n1*n2:.0f}")
print(f"A multiplicão dos valor é {n1//n2:.0f}")
maior(n1,n2)
print("O resultado da soma dos dois numeros é ", impopar(n1,n2))
maior40(n1,n2)'''

#Questão 2
'''frase = input("Digite uma frase: ")
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
        print(cont, end="")'''
    
#Questão 3
'''import random
import os
import time

senha = "1a2b"
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

print("Parabéns você acertou o número!!!!")'''


#Questão 4

import datetime
opc = 0

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
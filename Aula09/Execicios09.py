#Questão 1
'''n1 = int(input("Qual tabuada você deseja imprimir: "))
resultado = 0
for cont in range(0,11):
    resultado = n1 * cont
    print(f"{n1}x{cont} = {resultado}")'''



#Questão 2
'''for cont in range(10,0,-1):
    print(cont)'''

#Questão 3
'''casado = 0
solteiro = 0
qtd = 3
cont = 0
while ( cont < qtd):
    statusCivil = input(f"Qual é o estatus civil da {cont+1} pessoa? digite (c/s): ")
    if statusCivil in ("cC"):
        casado += 1
        cont += 1
    elif statusCivil in ("sS"):
        solteiro += 1
        cont += 1
    else:
        print("O estatus digitado é invalido por favor digite 'c' ou 's': ")
        

print(f"Na sua lista possui {casado} pessoas casadas e {solteiro} solteiras.")'''

#Questão 5
'''for cont in range(1,20,2):
    print(cont)'''

#Questão 6
'''preco = float(input("Digite o valor do pão: "))
result = 0
for cont in range(1,51):
    result = cont * preco
    print(f"{cont} - R$ {result:.2f}")'''


#Questão 8
'''respostas = []
sim = 0

print("Responda as perguntas abaixo com 's' para sim e 'n' para não:")
pergunta = input('Telefonou para a vítima? \n')
respostas.append(pergunta) 
pergunta = input('Esteve no local do crime? \n')
respostas.append(pergunta)
pergunta = input('Mora perto da vítima? \n')
respostas.append(pergunta)
pergunta= input('Devia para a vítima? \n')
respostas.append(pergunta)
pergunta = input('Já trabalhou com a vítima? \n')
respostas.append(pergunta)

for cont in range(5):
    if respostas[cont] in ('sS'):
        sim += 1
    
sim = respostas.count('s')
if sim == 2:
    print("Suspeito")
elif sim >2 and sim <5:
    print("Cúmplice")
elif sim == 5:
    print("Culpado")
else:
    print("Inocente")'''

#Questão 9
import time
d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
d6 = 0

for d1 in range(1,61):
    for d2 in range(2,60):            
        for d3 in range(3,59):
            for d4 in range(4,58):
                for d5 in range(5,57):
                    for d6 in range(6,56):
                            print(d1,d2,d3,d4,d5,d6)
                            time.sleep(0.1)

#Desafio 1
'''def func(valor):
    priDezena = valor//100
    segDezena = valor%100
    soma = priDezena + segDezena
    if soma**2 == valor:
        return valor
    else:
        return "false"

for cont in range(1000,10000):
    if func(cont) != "false":
        print(cont)'''
        
    



 


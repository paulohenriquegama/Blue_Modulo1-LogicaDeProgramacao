'''nomes = ['Paulo','Morgania','Hadassa']
print(nomes)
familia = "Familia Gama"

for nome in nomes:
    print("-",nome)

print(len(nomes))'''

#nomes.sort  - Ordena de forma crescente

'''if "hadassa" in nomes:
    print("Está")
else:
    print("Não")

for letra in familia:
    if letra == " ":
       None 
    else:
        print(letra)'''

#Exercício de Fixação

#Exercicio 01
'''frase = input("Digite uma frase: ")
a = 0
e = 0
i = 0
o = 0
u = 0
consoante = 0

for cont in frase:
    if cont == "a":
        a = a+1
    elif cont == "e":
        e = e+1
    elif cont == "i":
        i = i+1
    elif cont == "o":
        o = o+1
    elif cont == "u":
        u = u+1
    else:
        consoante = consoante+1

print(f"Sua frase tem {a} letra(s) 'a' {e} letra(s) 'e' {i} letra(s) 'i' {o} letra(s) 'o' e {u} letra(s) 'u', além de {consoante} consoantes")'''

#Questão 2

'''n1 = int(input("Digite um número: "))

for cont in range(1,n1+1):
    div = n1%cont
    if div == 0:
        print(cont)'''

#Questão 3

'''frase = input("Digite uma frase: ")

for letra in frase:
    if letra in ("aeiouAEIOU"):
        None
    else:
        print(letra, end="")'''



singleAccaunt = 0
marriedAccaunt = 0
wrongAnswer = 0

for i in range(3):
  maritalStatus = input('waths your marital status?[single/married]: ').lower()
  if (maritalStatus == 'married'):
    marriedAccaunt+=1
  elif (maritalStatus == 'single'):
    singleAccaunt+=1
  # handling error
  elif (maritalStatus != 'single' or maritalStatus!= 'married'):
    print('invalid response, try again...')
    wrongAnswer +=1
    newAttempt = [input(f'waths your marital status? [single/married]: ') for i in range(wrongAnswer)]
    
    newAttemptMarried = 0
    newAttemptSingle = 0

    for c in newAttempt: 
      if ('married' in newAttempt):
        newAttemptMarried+=1 
      elif ('single' in newAttempt):
        newAttemptSingle+=1

    singleAccaunt += newAttemptSingle
    marriedAccaunt += newAttemptMarried

print() 
print(f'the number of singles is: {marriedAccaunt}.')
print(f'the number of married is: {singleAccaunt}.')
print(f'the wrong answers : {wrongAnswer}')


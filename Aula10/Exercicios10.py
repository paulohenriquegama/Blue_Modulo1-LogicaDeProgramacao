'''opc = 1
opc1 = 1
while opc ==1:
    num = 1
    cont = 1
    qtd = int(input("Digite a quantidade de números imapares desejado: "))
    números =[]
    while cont <=qtd:
        print (num)
        números.append(num)
        cont = cont +1
        num = num + 2

    print()
    print("Tamanho da lista: ",len(números))
    print()
    print("Lista:",números)
    print()
    revertido = []
    for i in números:
        revertido = sorted(números,reverse=True)
    for num in revertido:
        print(num)

    aux = len(números)

    for i in range(aux, 1,1):
        print(números[aux])

    resp =input ("Você deseja continuar:(S/N)?")
    if resp in "Nn":
        opc = 0
    elif resp in "Ss":
        opc = 1 
    else:
        opc1 = 0
        while opc1 == 0:
            resp = input("Opção Inválida. Digite S ou N?")
            if resp in "Nn":
                opc = 0
                opc1 = 1
            elif resp in "Ss":
                opc = 1 
                opc1 = 1

print("Programa finalizado!!")
'''
#Questão 1
'''x = 3
cont = 0
num = list()
altura = list()
while cont < x:
    num.append(int(input(f"Digite o número do {cont+1}º aluno: ")))
    altura.append(float(input(f"Digite a altura do {cont+1}º aluno: ")))
    cont += 1
    
dic = dict(zip(num,altura))

print(max(num))
print(min(num))          
    '''

#Questão 2

senha = "1a2b"
resp = ""
while resp != senha:
    resp = input("Digite a senha: ")
    if resp != senha:
        print("Senha invalida tente novamente!")
print("Parabéns senha digitada corretamente.")

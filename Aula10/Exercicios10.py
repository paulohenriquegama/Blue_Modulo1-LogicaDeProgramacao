opc = 1
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
    
            
    

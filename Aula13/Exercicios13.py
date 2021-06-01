#Questão 1

'''produtos = {'arroz':[100,4.5],'feijão':[80,3.5],'macarrão':[150,2.1]}
opc = 0

cupom = {}
total = 0
valor_item = 0
v_item_t = 0
while opc != 1:
    opc2 = 0 
    item = input("Qual produto você deseja comprar: ")
    item = item.lower()
    if item in produtos:
        qtd = int(input(f"Quanto de {item} você deseja comprar? "))
        
        if produtos[item][0] == 0:
            print("Produto Indisponível")
        elif produtos[item][0] < qtd: 
            print("Quantidade solicitada não disponível")
        else:
            valor_item = produtos[item][1] * qtd
            v_item_t = v_item_t + valor_item
            produtos[item][0] = produtos[item][0] - qtd

            print(f'Essa quantidade de {item} custa {valor_item} R$')
            cupom[item] = [qtd,valor_item] 
            total = total + valor_item
            
    else:
        print("Produto Inválido.")
    while opc2 != 1:
        resp = input("Deseja continuar comprando? s/n: ")
        
        if resp in ('N','n','Não','não','s','s'):
            opc2 = 1
        else:
            print("Por favor digite 's' ou  'n'")

    if resp in ('N','n','Não','não'):
        opc = 1
        print("#"*30)
        print("######## CUPOM FISCAL ########")
        print()
for k,v in cupom.items():
    print(f'Você comprou {cupom[k][0]} kg de {k} = {cupom[k][1]} \n')
print("Total da sua compra =  ",total)
print()
print("#"*30)
print()
print("Programa finalizado!!")'''

#Questão 3
import os
import time

alunos = {}
opc = 0
def listar(alunos):
    if alunos == {}:
        print("Não temos alunos matriculados!!")
    else:
        for k,v in alunos.items():
            print(f'{k} - {v}')
def alterar(aluno):
    alunos[aluno] = [float(input(f"Digite a nova nota do aluno {aluno}: "))]

def consulta(aluno):
    print(f'A nota do {aluno} é ',alunos.get(aluno,"Aluno não encontrado"))

while opc == 0:
    menu = input('0. Sair\n1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)\n2. Inserir aluno e nota\n3. Alterar a nota de um aluno\n4. Consultar nota de um aluno específico\n5. Apagar um aluno da lista\n6. Exibir a média da turma\n')

    while menu not in ("0","1","2","3","4","5","6"):
        os.system('cls')
        print("Por favor digite um numero correspondente a opção desejada: ")
        menu = input('0. Sair\n1. Exibir lista de alunos com suas notas (cada aluno tem uma nota)\n2. Inserir aluno e nota\n3. Alterar a nota de um aluno\n4. Consultar nota de um aluno específico\n5. Apagar um aluno da lista\n6. Exibir a média da turma\n')    
        
    if menu == '0':
        opc = 1
    elif menu == '1':
        listar(alunos)
    elif menu == '2':
        aluno = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota: "))
        alunos[aluno] = {nota}
        os.system('cls')
        time.sleep(1)
        print("Cadastro realizado com sucesso!")
    elif menu == '3':
        aluno = input("Digite o nome do aluno que deseja alterar a nota:\n")
        alterar(aluno)    
        os.system('cls')
        time.sleep(1)
        print("Nota alterada com sucesso!!")
    elif menu == '4':
        aluno = input("Digite o nome do aluno que deseja consultar a nota: ")
        consulta(aluno)

    else:
        print("Continua")

print("Programa finalizado!!")
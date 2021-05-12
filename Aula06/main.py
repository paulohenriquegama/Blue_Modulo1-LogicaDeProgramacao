#Questão 1
'''def soma(a,b,c):
    print("A soma dos valores digitados é: ", a + b + c)

n1 = float(input("Digite o primiero numero: "))
n2 = float(input("Digite o segundo numero: "))
n3 = float(input("Digite o terceiro2 numero: "))

soma(n1,n2,n3)'''

#Questão 2
'''def poloridade(n1):
    if n1 > 0:
        return "P"
    elif n1 < 0:
        return "N"
    else:
        return 0

n1 = float(input("Digite um valor para descobrir se é 'P' para positivo ou 'N' para negativo: "))

print("O valor informado é: ", poloridade(n1))'''

#Questão 3
'''def somaImposto(taxaImposto,valorVenda):
    valorFinal = valorVenda + ((taxaImposto/100)*valorVenda)
    return print("O valor final da venda com o imposto é: ", valorFinal)

taxaImposto = float(input("Digite o  valor da taxa a ser cobrada sem o simbolo de '%': ")) 
valorVenda = float(input("Digite o valor da venda: "))

somaImposto(taxaImposto,valorVenda)'''

#Questão 4
'''def salario(horasTrabalhada):
    x = horasTrabalhada*valorHora
    he = 0

    if horasTrabalhada > 40:
        he = horasTrabalhada - 40
        he = he * (valorHora*1.5)
        x = x + he
        print("O valor da hora extra é: ", he)
    return x
valorHora = 50
horasTrabalhada = float(input("Digite a quantidade de horas trabalhada: "))

print(f'Esse mês você receberá {salario(horasTrabalhada)} reais de salário')'''

#Questão 5
'''def imc(peso,altura):
    x = peso/(altura**2)
    return x

altura = 1.68
peso = 75

print(f"O seu imc é: {imc(peso,altura):.2f}", )'''

#Questão 6
'''def convertNota(nota):
    if nota <= 4:
        return "F"
    elif nota < 7:
        return "D"
    elif nota < 8:
        return "C"
    elif nota <9:
        return "B"
    else:
        return "A"

nota = float(input("Digite uma nota: "))

print("Sua nota corresponde a letra: ", convertNota(nota))'''

#Questão 7
'''def menor(n1,n2):
    if n1>n2:
        return print("O menor numero digitado é: ", n2)
    elif n1<n2:
        return print("O menor numero digitado é: ", n1)
    else:
        return print("Os numeros são iguais")

n1 = float(input("Digite o primiero número: "))
n2 = float(input("Digite o segundo número: "))

menor(n1,n2)'''
'''try:

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
                    

    

    data = input("Digite uma data no formato '28/04/1992: " ).split("/")
    mesExtenso(data)
except:
    print("O que foi informado não é uma data!!")'''




class Personagem:
    def __init__(self,nome, dormindo=True, infectado=False,machucado = False, vida = True):
        self.nome = nome
        self.dormindo = dormindo
        self.infectado = infectado
        self.machucado = machucado
        self.vida = vida
    
    def __str__(self):
        #return "Você está " + ("acordado" if self.dormindo else "dormindo")
        if self.dormindo == False:
            dormindo = "Acordado"
        else:
            dormindo = "dormindo"

        if self.vida == True:
            vida = "vivo"
        else:
            vida = "morto"

        if self.machucado == False:
            machucado = "está bem"
        else:
            machucado = " machucado"

        if self.infectado == True:
            infectado = "foi contaminado"
        else:
            infectado = "não foi contaminado"
        
        if self.vida == True:
            return f'\033[1;32m {self.nome} está {vida} e {dormindo} {infectado} {machucado} fisicamente.\033[m'
        else:
            return f'\033[1;91m {self.nome} está {vida} {infectado} e {machucado} fisicamente.\033[m'


class Relogio:
    def __init__(self):
        self.dias = 1
        self.horas = 5
        self.minutos = 0
    
    def __str__(self):
        return f"{self.horas:02d}:{self.minutos:02d} do dia {self.dias:02d}"
    
    def avancaTempo(self, horas):
        self.horas += horas
        if self.horas >=24:
            self.dias += 1
            self.horas = self.horas - 24
        
        


import time
import os,sys
os.system('cls')
opc = 0
print('''
Loading…
█▒▒▒▒▒▒▒▒▒
''')

time.sleep(2)
os.system('cls')
print('''
10%
███▒▒▒▒▒▒▒
''')

time.sleep(2)
os.system('cls')
print('''
30%
█████▒▒▒▒▒
''')

time.sleep(3)
os.system('cls')
print('''
50%
███████▒▒▒
''')

time.sleep(3)
os.system('cls')
print('''
100%
██████████
''')

os.system('cls')
frase = "\033[;1mInicio do jogo!!\033[m"
print(frase.center(150))
print()
nome = input("\033[;1mDigite o nome do seu personagem: \033[m")
p1 = Personagem(nome)   
relogio = Relogio()
os.system('cls')
print(f"\033[;1m{p1.nome} acorda com uma grande explosão, olha no relógio e são {relogio}.\n\033[m")
p1.dormindo = False

while opc == 0:

    print('''\033[;1m
O que você irá fazer?

1 - Vai até a porta para vê o que está acontecendo.
2 - Liga a TV para ver os noticiários.
3 - Fica com tanto medo e procura um lugar para se esconder.
        \033[m''')
    escolha = input("\033[;1mDigite uma das alternativas acima: \033[m")
    if escolha == "1":
       os.system('cls')
       p1.infectado = True
       p1.machucado = True
       p1.vida = False
       print(f"\nVc se depara com um zumbi, e como não estava preparado ele conseguiu te atingir, vc é contaminado e após 1h morre.\n")
       relogio.avancaTempo(1)
       time.sleep(2)
       
       print(relogio)
       print()
       print(p1)
       print()
       opc = 1
    elif escolha == "2":
        os.system('cls')
        frase = f"\033[1;32m{p1.nome} ligou a TV e os noticiários estão informando que houve uma explosão em um laboratório e um vírus muito perigoso foi disseminado e as pessoas infectadas estão virando zumbis. \033[m"

        for i in list(frase):
            print(i, end='')
            #O stdout só é atualizado quando há nova linha e como nós estamos mandando tudo na mesma é preciso forçar a atualização.
            sys.stdout.flush()
            time.sleep(0.02)
        print()

        while opc == 0:
            
            print(f'''\033[;1m
O que vc fará agora?
1 – Procurar uma arma para se defender e permanecer na sua residência.
2 - Fica com tanto medo e procura um lugar para se esconder.
3 - Procurar uma arma para se defender e ir em busca de mais pessoas que não estão infectadas.
\033[m
            ''')
            escolha = input("\033[;1mDigite uma das alternativas acima: \033[m")
            if escolha == "1":
                os.system('cls')
                frase = f'{p1.nome} encontrou uma arma para se defender, os zumbis começaram a invadir sua casa após 2hrs de batalha, vc fica cansado e como estava sozinho foi atingido e contaminado e morre após 1hr.'
                for i in list(frase):
                    print(i,end= "")
                    sys.stdout.flush()
                    time.sleep(0.05)
                print()
    elif escolha == "3":
        os.system('cls')
        p1.infectado = True
        p1.machucado = True
        p1.vida = False
        frase = f'\033[1;91m {p1.nome} trancou a porta do seu quarto e ficou escondido embaixo da cama. O número de zumbis crescia a cada instantes. Após 2hrs de tentativa eles conseguiram arrombar a porta e vc não teve como se defender, foi contaminado fica muito ferido e após 1hr morre.\033[m'
        for i in list(frase):
            print(i, end='')
            #O stdout só é atualizado quando há nova linha e como nós estamos mandando tudo na mesma é preciso forçar a atualização.
            sys.stdout.flush()
            time.sleep(0.05)
        print()    
        time.sleep(2)
        relogio.avancaTempo(3)
        print()
        print(relogio)
        print()
        print(p1)
        print()
        opc = 1
print("Programa Finalizado!!")

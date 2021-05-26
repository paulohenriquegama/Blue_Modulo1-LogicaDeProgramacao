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
            machucado = "e machucado"

        if self.infectado == True:
            infectado = "foi contaminado"
        else:
            infectado = "não foi contaminado"
        
        if self.vida == True:
            return f'{self.nome} está {vida} e {dormindo} {infectado} {machucado} fisicamente.'
        else:
            return f'{self.nome} está {vida} {infectado} e {machucado} fisicamente.'


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
import os
opc = 0

print("Inicio do jogo!!") 
print()
nome = input("Digite o nome do seu personagem: ")
p1 = Personagem(nome)   
relogio = Relogio()
print(f"{p1.nome} acorda com uma grande explosão, olho no relógio e são {relogio}.\n")
p1.dormindo = False

while opc == 0:
    print("O que você irá fazer?\n")
    print("1 - Vai até a porta para vê o que está acontecendo.")
    print("2 - Liga a TV para ver os noticiários.")
    print("3 - Fica com tanto medo e procura um lugar para se esconder.")
    escolha = input("Digite uma das alternativas acima: ")
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
    elif escolha == "3":
        os.system('cls')
        p1.infectado = True
        p1.machucado = True
        p1.vida = False
        print(f'{p1.nome} trancou a porta do seu quarto e ficou escondido embaixo da cama.', end= "" )
        time.sleep(3)
        print(end=' O número de zumbis crescia a cada instantes.') 
        time.sleep(3) 
        print(' Após 2hrs de tentativa eles conseguiram arrombar a porta e vc não teve como se defender, foi contaminado fica muito ferido e após 1hr morre.')
        time.sleep(5)
        relogio.avancaTempo(3)
        print()
        print(relogio)
        print()
        print(p1)
        print()
        opc = 1
print("Programa Finalizado!!")

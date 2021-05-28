class Personagem:
    def __init__(self, nome, dormindo=True, infectado=False, machucado=False, vida=True):
        self.nome = nome
        self.dormindo = dormindo
        self.infectado = infectado
        self.machucado = machucado
        self.vida = vida

    def __str__(self):
        # return "Você está " + ("acordado" if self.dormindo else "dormindo")
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
        if self.horas >= 24:
            self.dias += 1
            self.horas = self.horas - 24


class Texto:
    def __init__(self):
        self.__texto = ''
        self.__estilo = "verde"
        self.__velocidade = 0.02

    @property
    def texto(self):
        return self.__texto

    @texto.setter
    def texto(self, novo_texto):
        raise ValueError("Impossível escrever texto diretamente, tente u outro método.")

    def escreverTexto(self, texto, estilo='vermelho', velocidade=0.02):
        self.__texto = texto
        self.__estilo = estilo
        self.__velocidade = velocidade
        if self.__estilo == "vermelho":
            for i in list(f'\033[1;91m{self.__texto}\033[m'):
                print(i, end='')
                sys.stdout.flush()
                time.sleep(self.__velocidade)
        elif self.__estilo == 'verde':
            for i in list(f'\033[1;32m{self.__texto}\033[m'):
                print(i, end='')
                sys.stdout.flush()
                time.sleep(self.__velocidade)
        elif self.__estilo == 'negrito':
            for i in list(f'\033[;1m{self.__texto}'):
                print(i, end='')
                sys.stdout.flush()
                time.sleep(self.__velocidade)
        else:
            for i in list(self.__texto):
                print(i, end='')
                sys.stdout.flush()
                time.sleep(self.__velocidade)
        print()


class Morto:
    texto = Texto()

    def __init__(self):
        self.infectado = True
        self.vida = False

    def imprimir(self):
        frase = '''
            ███████████████████████████████████████████████████████████████████████████████████████████
            █░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░██
            █░██╗░░░██╗░█████╗░░█████╗░███████╗░░███╗░░░███╗░█████╗░██████╗░██████╗░███████╗██╗░░░██╗██
            █░██║░░░██║██╔══██╗██╔══██╗██╔════╝░░████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔════╝██║░░░██║██
            █░╚██╗░██╔╝██║░░██║██║░░╚═╝█████╗░░░░██╔████╔██║██║░░██║██████╔╝██████╔╝█████╗░░██║░░░██║██
            █░░╚████╔╝░██║░░██║██║░░██╗██╔══╝░░░░██║╚██╔╝██║██║░░██║██╔══██╗██╔══██╗██╔══╝░░██║░░░██║██
            █░░░╚██╔╝░░╚█████╔╝╚█████╔╝███████╗░░██║░╚═╝░██║╚█████╔╝██║░░██║██║░░██║███████╗╚██████╔╝██
            █░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝░░╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝░╚═════╝░██
            ███████████████████████████████████████████████████████████████████████████████████████████
            █████████████████████████████████████▀▀▀░░░░░░░▀▀▀█████████████████████████████████████████
            ██████████████████████████████████▀░░░░░░░░░░░░░░░░░▀██████████████████████████████████████
            █████████████████████████████████│░░░░░░░░░░░░░░░░░░░│█████████████████████████████████████
            ████████████████████████████████▌│░░░░░░░░░░░░░░░░░░░│▐████████████████████████████████████
            ████████████████████████████████░└┐░░░░░░░░░░░░░░░░░┌┘░████████████████████████████████████
            ████████████████████████████████░░└┐░░░░░░░░░░░░░░░┌┘░░████████████████████████████████████
            ████████████████████████████████░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░████████████████████████████████████
            ████████████████████████████████▌░│██████▌░░░▐██████│░▐████████████████████████████████████
            █████████████████████████████████░│▐███▀▀░░▄░░▀▀███▌│░█████████████████████████████████████
            ████████████████████████████████▀─┘░░░░░░░▐█▌░░░░░░░└─▀████████████████████████████████████
            ████████████████████████████████▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄████████████████████████████████████
            ██████████████████████████████████▄─┘██▌░░░░░░░▐██└─▄██████████████████████████████████████
            ███████████████████████████████████░░▐█─┬┬┬┬┬┬┬─█▌░░███████████████████████████████████████
            ██████████████████████████████████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐██████████████████████████████████████
            ███████████████████████████████████▄░░░└┴┴┴┴┴┴┴┘░░░▄███████████████████████████████████████
            █████████████████████████████████████▄░░░░░░░░░░░▄█████████████████████████████████████████
            ████████████████████████████████████████▄▄▄▄▄▄▄████████████████████████████████████████████
        '''
        texto.escreverTexto(frase, 'vermelho', 0.01)


import time
import os, sys
import pygame

texto = Texto()


os.system('cls')
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("Projeto/audio.mp3")
pygame.mixer.music.play(-1)



opc = 0
print('''
Loading…
█▒▒▒▒▒▒▒▒▒
''')

time.sleep(1)
os.system('cls')
print('''
10%
███▒▒▒▒▒▒▒
''')

time.sleep(1)
os.system('cls')
print('''
30%
█████▒▒▒▒▒
''')

time.sleep(1)
os.system('cls')
print('''
50%
███████▒▒▒
''')

time.sleep(1)
os.system('cls')
print('''
100%
██████████
''')

os.system('cls')
# frase = "\033[;1mInicio do jogo!!\033[m"
frase = '''
                        ██╗███╗░░██╗██╗░█████╗░██╗░█████╗░  ██████╗░░█████╗░  ░░░░░██╗░█████╗░░██████╗░░█████╗░
                        ██║████╗░██║██║██╔══██╗██║██╔══██╗  ██╔══██╗██╔══██╗  ░░░░░██║██╔══██╗██╔════╝░██╔══██╗
                        ██║██╔██╗██║██║██║░░╚═╝██║██║░░██║  ██║░░██║██║░░██║  ░░░░░██║██║░░██║██║░░██╗░██║░░██║
                        ██║██║╚████║██║██║░░██╗██║██║░░██║  ██║░░██║██║░░██║  ██╗░░██║██║░░██║██║░░╚██╗██║░░██║
                        ██║██║░╚███║██║╚█████╔╝██║╚█████╔╝  ██████╔╝╚█████╔╝  ╚█████╔╝╚█████╔╝╚██████╔╝╚█████╔╝
                        ╚═╝╚═╝░░╚══╝╚═╝░╚════╝░╚═╝░╚════╝░  ╚═════╝░░╚════╝░  ░╚════╝░░╚════╝░░╚═════╝░░╚════╝░
'''
texto.escreverTexto(frase, 'negrito', 0.005)
print()

print()
nome = input("\033[;1mDigite o nome do seu personagem: \033[m")
#pygame.mixer.music.stop()
p1 = Personagem(nome)
relogio = Relogio()
morto = Morto()

os.system('cls')
frase = f"\033[;1m{p1.nome} acorda com uma grande explosão, olha no relógio e são {relogio}.\n\033[m"
p1.dormindo = False
pygame.mixer.music.load("Projeto/explosao.mp3")
pygame.mixer.music.play()
texto.escreverTexto(frase, 'negrito', 0.03)


#pygame.mixer.music.stop()
pygame.mixer.music.load("Projeto/audio.mp3")
pygame.mixer.music.play(-1)

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
        frase = f"\nVc se depara com um zumbi, e como não estava preparado ele conseguiu te atingir, vc é contaminado e após 1h morre.\n"
        texto.escreverTexto(frase)
        relogio.avancaTempo(1)
        time.sleep(2)

        print(relogio)
        print()
        print(p1)
        print()
        morto.imprimir()
        opc = 1


    elif escolha == "2":
        os.system('cls')
        frase = f"\033[1;32m{p1.nome} ligou a TV e os noticiários estão informando que houve uma explosão em um laboratório e um vírus muito perigoso foi disseminado e as pessoas infectadas estão virando zumbis. \033[m"
        texto.escreverTexto(frase, 'verde', 0.03)

        while opc == 0:

            print(f'''\033[;1m
O que vc fará agora?
1 – Procurar uma arma para se defender e permanecer na sua residência.
2 - Fica com tanto medo e procura um lugar para se esconder.
3 - Procurar uma arma para se defender e ir em busca de mais pessoas que não estão infectadas.
\033[m
            ''')
            escolha = input("\033[;1mDigite uma das alternativas acima: \033[m")
            #Caminho 2->1
            if escolha == "1":
                os.system('cls')
                frase = f'{p1.nome} encontrou uma arma para se defender, os zumbis começaram a invadir sua casa após 1hrs de batalha, vc fica cansado e como estava sozinho foi atingido e contaminado e morre após 1hr.'
                p1.infectado = True
                p1.machucado = True
                p1.vida = False
                pygame.mixer.music.load("Projeto/zombie-attack.wav")
                pygame.mixer.music.play(2)
                texto.escreverTexto(frase)
                time.sleep(2)
                relogio.avancaTempo(2)
                print()
                print(relogio)
                print()
                print(p1)
                print()
                opc = 1

            #Caminho 2->2
            elif escolha == "2":
                os.system('cls')
                p1.infectado = True
                p1.machucado = True
                p1.vida = False
                frase = f'{p1.nome} trancou a porta do seu quarto e ficou escondido embaixo da cama. O número de zumbis crescia a cada instantes. Após 2hrs de tentativa eles conseguiram arrombar a porta e vc não teve como se defender, foi contaminado fica muito ferido e após 1hr morre.'
                pygame.mixer.music.load("Projeto/zombie-attack.wav")
                pygame.mixer.music.play(1)
                time.sleep(1)
                pygame.mixer.music.stop()
                pygame.mixer.music.load("Projeto/arrombamento.wav")
                pygame.mixer.music.play(2)
                time.sleep(2)
                pygame.mixer.music.load("Projeto/zombie-attack.wav")
                pygame.mixer.music.play(2)
                texto.escreverTexto(frase)
                time.sleep(2)
                relogio.avancaTempo(3)
                print()
                print(relogio)
                print()
                print(p1)
                print()
                opc = 1
            #Caminho 2->3 essa opção da seguimento ao jogo
            elif escolha == '3':
                os.system('cls')
                frase = f'{p1.nome} encontrou uma arma pegou alguns mantimentos e fugiu pela janela aproveitando que não tinha nenhum zumbi por perto. Depois de 5h de caminhada em busca de ajuda, ouvi pessoas pedindo ajuda.'
                texto.escreverTexto(frase, 'verde')
                pygame.mixer.music.load("Projeto/gritos.wav")
                pygame.mixer.music.play()
                time.sleep(2)
                pygame.mixer.music.load("Projeto/audio.mp3")
                pygame.mixer.music.play(-1)
                relogio.avancaTempo(5)
                print()
                print(relogio)
                print()
                print(p1)
                print()
                #Esse while da inicio a terceira etapa do jogo.
                while opc == 0:
                    print(f'''\033[;1m{p1.nome} tem duas opções:

1 – Vc irá até elas, para tentar ajudá-las?
2 – Ignora o pedido de ajuda e continua na sua jornada sozinho?
\033[m
                    ''')
                    escolha = input("\033[;1mDigite uma das alternativas acima: \033[m")
                    #Caminho 2->3->1
                    if escolha == "1":
                        os.system('cls')
                        p1.infectado = True
                        p1.machucado = True
                        p1.vida = False
                        frase = f'\033[1;91m {p1.nome} encontra um grupo de 3 pessoas e se junta a elas em uma batalha contra um grupo de zumbis que não para de crescer, depois de 3hrs de batalha vc e todos os seus amigos são infectados e não resistem a infecção morrendo após 1hr.\033[m'
                        texto.escreverTexto(frase)
                        time.sleep(2)
                        relogio.avancaTempo(4)
                        print()
                        print(relogio)
                        print()
                        print(p1)
                        print()
                        opc = 1
                    #Caminho 2->3->2
                    elif escolha == '2':
                        os.system('cls')

                        frase = f"\033[1;32m{p1.nome} ignorou os pedidos de ajuda, pq viu que fora do prédio havia um grupo muito grande de zumbis e que vc não teria chance de entrar.\033[m"
                        time.sleep(2)
                        texto.escreverTexto(frase, 'verde')

                        print(relogio)
                        print()
                        print(p1)
                        print()
                        frase = '\033[1;91mPassa-se 1hrs e um grupo de zumbis te cercam como vc estava sozinho não consegui resistir e é atingido e infectado.\033[m'


    elif escolha == "3":
        os.system('cls')
        p1.infectado = True
        p1.machucado = True
        p1.vida = False
        frase = f'\033[1;91m {p1.nome} trancou a porta do seu quarto e ficou escondido embaixo da cama. O número de zumbis crescia a cada instantes. Após 2hrs de tentativa eles conseguiram arrombar a porta e vc não teve como se defender, foi contaminado fica muito ferido e após 1hr morre.\033[m'
        pygame.mixer.music.load("Projeto/zombie-attack.wav")
        pygame.mixer.music.play(1)
        time.sleep(1)
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Projeto/arrombamento.wav")
        pygame.mixer.music.play(2)
        time.sleep(2)
        pygame.mixer.music.load("Projeto/zombie-attack.wav")
        pygame.mixer.music.play(2)
        texto.escreverTexto(frase, 'vermelho', 0.06)
        
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

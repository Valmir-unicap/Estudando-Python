#Quiz sobre Vingadores
def menu():
    print("")
    print("Quiz sobre Vingadores")
    print("")
    print("1 - Iniciar quiz")
    print("0 - Sair do quiz")
    print("")


def pergunta1():
    print("")
    print("Quem foi o personagem que morreu em Vingadores Ultimato?\n \n 1- Homem de ferro\n 2- Capitão América\n 3- Hulk\n 4- Thor")
    escolha1 = int(input("Escolha uma opção: "))
    validacaoPerguntas(escolha1)
    if escolha1 == 1:
        print("Você acertou!")
    else:
        print("Você errou!\n Resposta = Homem de Ferro")


def pergunta2():
    print("")
    print("Qual personagem foi digno, de levantar o martelo de Thor?\n \n 1- Homem formiga\n 2- Doutor estranho\n 3- Pantera negra\n 4- Capitão América")
    escolha2 = int(input("Escolha uma opção: "))
    validacaoPerguntas(escolha2)
    if escolha2 == 4:
        print("Você acertou!")
    else:
        print("Você errou!\n Resposta = Capitão América")


def pergunta3():
    print("")
    print("Quem o Thanos matou para conseguir a joia da alma?\n \n 1- Nebulosa\n 2- Viuva negra\n 3- Gamora\n 4- Visão")
    escolha3 = int(input("Escolha uma opção: "))
    validacaoPerguntas(escolha3)
    if escolha3 == 3:
        print("Você acertou!")
    else:
        print("Você errou!\n Resposta = Gamora")


def pergunta4():
    print("")
    print("Quem encontra Thor no espaço?\n \n 1- Capitã Marvel \n 2- Os guardiões da galaxia\n 3- Loki\n 4-Homem de Ferro")
    escolha4 = int(input("Escolha uma opção: "))
    validacaoPerguntas(escolha4)
    if escolha4 == 2:
        print("Você acertou!")
    else:
        print("Você errou!\n Resposta = Os guardiões da galaxia")


def pergunta5():
    print("")
    print("Quem criou o Ultron?\n \n 1- Homem de Ferro\n 2- Loki\n 3- Thanos\n 4- Thor")
    escolha5 = int(input("Escolha uma opção: "))
    validacaoPerguntas(escolha5)
    if escolha5 == 1:
        print("Você acertou!")
    else:
        print("Você errou!\n Resposta = Homem de Ferro")


def validacaoPerguntas(escolha):
    while escolha < 1 or escolha > 4:
        print("Opção inválida! Tente novamente!")
        escolha = int(input("Escolha uma opção: "))
    return escolha


def validacao(escolha):
    while escolha < 0 or escolha > 1:
        print("Opção inválida! Tente novamente!")
        escolha = int(input("Escolha uma opção: "))
    return escolha


#main
menu()
escolha = int(input("Escolha uma opção: "))
recebe = validacao(escolha)
while recebe == 1:
    pergunta1()
    pergunta2()
    pergunta3()
    pergunta4()
    pergunta5()
    break
print("Fim do programa! @Developer Valmir Junior")

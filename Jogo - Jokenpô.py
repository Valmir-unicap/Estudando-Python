def menu():
    print("")
    print("Bem Vindo - Jogo Jokenpô")
    print("")
    print("1- Iniciar jogo")
    print("0- Sair do jogo")
    print("")


def jogotradicional():
    print("")
    print("1- papel")
    print("2- Tesoura")
    print("3- Pedra")
    print("")


def logicatradicional(numero, computador):
    if numero == computador:
        print("Empate")
        analisarComputador(computador)
    elif numero == 1 and computador == 3:
        print("Você venceu!")
        analisarComputador(computador)
    elif numero == 2 and computador == 1:
        print("Você venceu!")
        analisarComputador(computador)
    elif numero == 3 and computador == 2:
        print("Você venceu!")
        analisarComputador(computador)
    else:
        print("Você perdeu!")
        analisarComputador(computador)


def nivel():
    print("")
    print("1- Fácil")
    print("2- Difícil")
    print("0- Voltar ao menu do jogo")
    print("")


def jogodificil():
    print("")
    print("1- Papel")
    print("2- Tesoura")
    print("3- Pedra")
    print("4- Largato")
    print("5- Spoke")
    print("")


def logicadificil(numero, computador):
    if numero == computador:
        print("Empate")
        analisarComputador(computador)
    elif numero == 1 and computador == 3:
        print("Você venceu!")
        analisarComputador(computador)
    elif numero == 2 and computador == 1:
        print("Você venceu!")
        analisarComputador(computador)
    elif numero == 3 and computador == 2:
        print("Você venceu!")
        analisarComputador(computador)
    elif numero == 4 and computador == 1:
        print("Você venceu!")
        analisarComputador(computador)
    elif numero == 4 and computador == 5:
        print("Você venceu!")
        analisarComputador(computador)
    elif numero == 2 and computador == 4:
        print("Você venceu!")
        analisarComputador(computador)
    elif numero == 3 and computador == 4:
        print("Você venceu!")
        analisarComputador(computador)
    elif numero == 5 and computador == 3:
        print("Você venceu!")
        analisarComputador(computador)
    elif numero == 5 and computador == 2:
        print("Você venceu!")
        analisarComputador(computador)
    elif numero == 1 and computador == 5:
        print("Você venceu!")
        analisarComputador(computador)
    else:
        print("Você perdeu!")
        analisarComputador(computador)


def analisarComputador(computador):
    if computador == 1:
        print("Computador escolheu papel")
    elif computador == 2:
        print("Computador escolheu tesoura")
    elif computador == 3:
        print("Computador escolheu pedra")
    elif computador == 4:
        print("Computador escolheu Largato")
    elif computador == 5:
        print("Computador escolheu Spok")


# main
menu()
escolha = int(input("Escolha uma opção: "))
while escolha < 0 or escolha > 1:  # validaçao entrada de dados
    print("Inválido!")
    escolha = int(input("Escolha uma opção: "))
while escolha != 0:
    nivel()
    grau = int(input("Escolha o nível do jogo: "))
    while grau < 0 or grau > 2:
        print("Inválido!")
        grau = int(input("Escolha o nível do jogo: "))

    if grau == 1:
        jogotradicional()
        import random
        computador = random.randint(1, 3)
        print("Computador já escolheu!")
        numero = int(input("Escolha uma opção: "))
        while numero < 1 or numero > 3:
            print("Inválido!")
            numero = int(input("Escolha uma opção: "))
        logicatradicional(numero, computador)

    elif grau == 2:
        jogodificil()
        import random
        computador = random.randint(1, 5)
        print("Computador já escolheu!")
        numero = int(input("Escolha uma opção: "))
        while numero < 1 or numero > 5:
            print("Inválido!")
            numero = int(input("Escolha uma opção: "))
        logicadificil(numero, computador)

    else:
        menu()
        escolha = int(input("Escolha uma opção: "))
        while escolha < 0 or escolha > 1:  # validaçao entrada de dados
            print("Inválido!")
            escolha = int(input("Escolha uma opção: "))

print("Fim do programa! Developer Valmir Júnior")

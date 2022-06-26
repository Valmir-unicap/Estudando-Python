def menu():
    print("")
    print("Menu")
    print("")
    print("1- Dólar (Moeda Americano)")
    print("2- Euro (Moeda da União Europeia)")
    print("3- Rublo (Moeda Russa)")
    print("4- Remimbi (Moeda Chinesa)")
    print("5- Libra esterlina (Moeda do Reino Unido)")
    print("0- Sair do programa!")


def tipo():
    print("")
    print("Converção")
    print("")
    print("1- De Real para Moeda estrangeira")
    print("2- Moeda estrangeira para Real")
    print("0- Voltar para menu")


#main
print("Conversor de moedas")
menu()
escolha = int(input("Escolha uma opção: "))
while escolha < 0 or escolha > 5:
    print("Opção inválida!")
    escolha = int(input("Escolha novamente uma opção: "))
while escolha != 0:
    tipo()
    opcao = int(input("Escolha uma opção: "))
    while opcao < 0 or opcao > 2:
        print("Opção inválida!")
        opcao = int(input("Escolha novamente uma opção: "))
    if escolha == 1 and opcao == 1:
        cotacao = float(input("Digite a cotação atual do dólar: "))
        valor = float(input("Digite em real, quanto deseja converter para dólar: "))
        operacao = valor/cotacao
        print("A conversão de Real, para o Dólar= U$", operacao)

    elif escolha == 1 and opcao == 2:
        cotacao = float(input("Digite a cotação atual do dólar: "))
        valor = float(input("Digite em dolár, quanto deseja converter para real: "))
        operacao = valor*cotacao
        print("A conversão de Dólar, para Real= R$", operacao)

    elif escolha == 2 and opcao == 1:
        cotacao = float(input("Digite a cotação atual do dólar: "))
        valor= float(input("Digite em real, quanto deseja converter para Euro: "))
        operacao = valor/cotacao
        print("A conversão de Real, para o Euro= €$", operacao)

    elif escolha == 2 and opcao == 2:
        cotacao = float(input("Digite a cotação atual do Euro: "))
        valor = float(input("Digite em Euro, quanto deseja converter para real: "))
        operacao = valor*cotacao
        print("A conversão de Euro, para Real= R$", operacao)

    elif escolha == 3 and opcao == 1:
        cotacao = float(input("Digite a cotação atual do Rublo: "))
        valor = float(input("Digite em Real, quanto deseja converter para Rublo: "))
        operacao = valor/cotacao
        print("A conversão de Real, para o Rublo= ₽$", operacao)

    elif escolha == 3 and opcao == 2:
        cotacao = float(input("Digite a cotação atual do Rublo: "))
        valor = float(input("Digite em Rublo, quanto deseja converter para real: "))
        operacao = valor*cotacao
        print("A conversão de Euro, para Real= R$", operacao)

    elif escolha == 4 and opcao == 1:
        cotacao = float(input("Digite a cotação atual do Remimbi: "))
        valor = float(input("Digite em Real, quanto deseja converter para Remimbi: "))
        operacao = valor/cotacao
        print("A conversão de Real, para o Remimbi= ¥$", operacao)

    elif escolha == 4 and opcao == 2:
        cotacao = float(input("Digite a cotação atual do Remimbi: "))
        valor = float(input("Digite em Remimbi, quanto deseja converter para real: "))
        operacao = valor*cotacao
        print("A conversão de Remimbi, para Real= R$", operacao)

    elif escolha == 5 and opcao == 1:
        cotacao = float(input("Digite a cotação atual da Libra esterlina: "))
        valor = float(input("Digite em Real, quanto deseja converter para Libra esterlina: "))
        operacao = valor/cotacao
        print("A conversão de Real, para o Libra esterlina= £$", operacao)

    elif escolha == 5 and opcao == 2:
        cotacao = float(input("Digite a cotação atual do Libra esterlina: "))
        valor = float(input("Digite em Libra esterlina, quanto deseja converter para real: "))
        operacao = valor*cotacao
        print("A conversão de Libra esterlina, para Real= R$", operacao)

    menu()
    escolha = int(input("Escolha uma opção: "))
    while escolha < 0 or escolha > 5:
        print("Inválido!")
        escolha = int(input("Escolha uma opção: "))
print("Fim do programa! Developer Valmir Júnior")

# -*- coding: utf-8 -*-
print("Calculadora Básica")
numero1= int(input("Digite o primeiro número: "))
numero2= int(input("Digite o segundo número: ")) 
print("Menu")
print("1- Adição")
print("2- Subtração")
print("3- Divisão")
print("4- Multiplicação")
print("0- Sair do programa!")
escolha= int(input("Escolha uma das opções acima: "))
while escolha >= 5 or escolha <0: #validacão da entrada de dados 
    print("Opção inválida")
    escolha= int(input("Escolha uma das opções acima: "))
if escolha == 1:
    soma= numero1 + numero2
    print("Resultado= ",soma)
elif escolha == 2:
    subtracao= numero1 - numero2
    print("Resultado= ",subtracao)
elif escolha == 3:
    divisao= numero1/numero2
    print("Resultado= ",divisao)
elif escolha == 4:
    multiplica= numero1 * numero2
    print("Resultado= ",multiplica)
else:
    print("Fim do programa! @Developer Valmir Jr")

# -*- coding: utf-8 -*-
print("IMC - Índice de massa corporal")
peso= float(input("Digite seu peso: "))
while peso<=0: #validação de entrada de dados
    print("Opção inválida!")
    peso= float(input("Digite seu peso: "))
altura= float(input("Digite sua altura: "))
while altura<=0: #validação de entrada de dados
    print("Opção inválida!")
    altura= float(input("Digite sua altura: "))
imc= peso/(altura*altura)
imc= round (imc) #arredondando o número com a função round
print("Seu IMC= ",imc)

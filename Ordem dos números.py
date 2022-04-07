# -*- coding: utf-8 -*-
print("Ordem dos números")
print("")
print("Menu")
print("1- exibir ordem crescente")
print("2- exibir ordem decrescente")
print("0- sair do programa")
escolha= int(input("escolha uma opção: "))
while escolha>2 and escolha>0:
    escolha= int(input("Opção inválida! digite uma opção: "))
if escolha==1:
    numero= int(input("digite um numero: "))
    ate= int(input("até quanto: "))
    for numero in range(numero, ate): # o que esta em parenteses significa (comaça,termina)
        print(numero)
elif escolha==2:
    numero= int(input("digite um numero: "))
    ate= int(input("até quanto: "))
    for numero in range(numero, ate, -1): # o que esta em parenteses significa (comaça,termina,incrementador)
        print(numero)
else:
    print("fim do programa!")

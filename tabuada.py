# -*- coding: utf-8 -*-
print("Tabuada")
numero= int(input("Digite um número, que deseja saber a tabuada: "))
while numero<0:
    print("Não existe tabuada de números negativos")
    numero= int(input("Digite novamente um número: "))
recebe=0
while recebe<10: #so para quando recebe=10
    recebe= recebe+1 #incrimento mais 1
    resultado= numero*recebe
    print(numero,"*",recebe,"=",resultado)

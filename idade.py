# -*- coding: utf-8 -*-
print("Mensagem!")
nome= raw_input("digite seu nome: ") #raw_input serve para entrada de palavras, em Python 2
print("Bem vindo: ",nome)
nasceu= int(input("Digite seu ano de nascimento: "))
while nasceu<1900 or nasceu>2022: #validação de entrada de dados
   nasceu= int(input("inválido! Digite novamente seu ano de nascimento: "))
idade= 2022-nasceu
print("Sua idade= ",idade)

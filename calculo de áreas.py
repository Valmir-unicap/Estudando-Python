# -*- coding: utf-8 -*-
print("Área das figuras planas")
print("Menu")
print("1- Triângulo")
print("2- Quadrado")
print("3- Retângulo")
print("4- Círculo")
print("0- Sair do programa")
escolha= int(input("Escolha uma das opções acima: "))
while escolha>4 or escolha<0: #validação de entrada de dados
    print("Opção inválida!")
    escolha= int(input("Digite novamente: "))   
if escolha==1:
    base= float(input("Digite o valor da base: ")) 
    altura= float(input("Digite a altura: ")) 
    area= (base*altura)/2
    print("Area= ",area)
elif escolha==2:
    print("Todos os lados são iguais")
    lado= float(input("Digite o valor do lado: "))
    area= lado*lado
    print("Area= ",area)
elif escolha==3: 
    altura= float(input("Digite o valor da altura: "))
    base= float(input("Digite o valor da base: ")) 
    area= altura*base
    print("Area= ",area)
elif escolha==4: 
    raio= float(input("Digite o valor do raio: "))
    import math #chamo a biblioteca para obter pi
    raio2= raio*raio
    area= math.pi * raio2
    area= round (area) #arredondando o número com a função round
    print("Area= ",area)
else:
    print("Fim do programa - @Developer Valmir Jr")

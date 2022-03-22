# -*- coding: utf-8 -*-
print("Mercado")
pagar= float(input("Digite o valor total da compra: R$"))
while pagar<0:
    pagar= float(input("Valor inválido, digite novamente: R$"))
dinheiro= float(input("Digite o valor que foi pago: R$"))
while dinheiro<0:
    dinheiro= float(input("Valor inválido, digite novamente: R$"))
if dinheiro==pagar:
    print("Não tem troco!")
elif dinheiro>pagar:
    troco= dinheiro - pagar
    print("Seu troco foi de R$",troco)
else:
    deve= pagar - dinheiro
    print("Voce ainda deve: R$",deve)

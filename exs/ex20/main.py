valor01 = int(input("digite um valor: "))
valor02 = int(input("digite um valor: "))
valor03 = int(input("digite um valor: "))
if valor01 > valor02 and valor01 > valor03:
    maior = valor01
if valor02 > valor01 and valor02 > valor03:
    maior = valor02
if valor03 > valor01 and valor03 > valor02:
    maior = valor03
if valor01 < valor02 and valor01 < valor03:
    menor = valor01
if valor02 < valor01 and valor02 < valor03:
    menor = valor02
if valor03 < valor01 and valor03 < valor02:
    menor = valor03
print("o maior valor é: {}" .format(maior))
print("o maior valor é: {}" .format(menor))
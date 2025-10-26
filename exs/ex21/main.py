salario = float(input("digite seu salário: "))
if salario >= 1250:
    novosalario = salario + (salario * 10 / 100)
else:
    novosalario = salario + (salario * 15 / 100)
print("seu novo salário é de {}" .format(novosalario))
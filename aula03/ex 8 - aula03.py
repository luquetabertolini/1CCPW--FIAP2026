print(f'REAJUSTE DE SALÁRIOS!')
salario = float(input(f' Digite seu salário em reais: '))



if salario <= 280:
    novo_salario = salario + (salario * 0.20)
    bonus = (f'20%')
elif salario <= 700:
    novo_salario = salario + (salario * 0.15)
    bonus = (f'15%')
elif salario <= 1500:
    novo_salario = salario + (salario * 0.1)
    bonus = (f'10%')
else:
    novo_salario = salario + (salario * 0.05)
    bonus = (f'5%')

aumento = novo_salario -  salario

print(f' Salário anterior: R${salario}.')
print(f' O aumento foi de R${aumento}.')
print(f' O bônus foi de {bonus}')
print(f' Seu novo salário: {novo_salario}')




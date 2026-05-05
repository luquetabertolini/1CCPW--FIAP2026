n1 = float(input(f' Digite a nota: '))
n2 = float(input(f' Digite a nota: '))
n3 = float(input(f' Digite a nota: '))
n4 = float(input(f' Digite a nota: '))
media = (n1 + n2 + n3 + n4) / 4

if media >= 7:
    print(f' Aprovado! ')
elif media >= 5:
    print(f' Recuperação. ')
else:
    print(f' Reprovado. ')
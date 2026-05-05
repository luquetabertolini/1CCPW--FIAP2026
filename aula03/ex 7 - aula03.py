nascimento = int(input(f' Digite o ano do seu nascimento: '))
ano = 2026
if ano - nascimento >= 70:
    print(f' O seu voto é opcional! ')
elif ano - nascimento >= 18:
    print(f' O seu voto é obrigatório! ')
elif ano - nascimento >= 16:
    print(f' O seu voto é opcional! ')
else:
    print(f' O seu voto é proibido! ')
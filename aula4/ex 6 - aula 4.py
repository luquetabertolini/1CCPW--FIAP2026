# EXERCÍCIO 6
# Faça um programa capaz de exibir todos os valores pares entre 2 e um valor fornecido pelo usuário.

limite = int(input('Digite um valor: '))

for i in range(2, limite + 1, 2):
    print(i)
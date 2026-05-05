# ATIVIDADE 03

# Faça um programa que receba a quantidade de produtos que o usuário deseja
# A seguir, seu programa deve exibir a mensagem “Produto” a quantidade de vezes que o usuário solicitou.
# Utilize o laço for

while True:
    qnt = int(input('Digite a quantidade de produtos: '))
    if qnt > 0:
        break
    else:
        print('Digite um valor válido!')

for i in range(qnt):
    print(f'Produto {i+1}')
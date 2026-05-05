# FUNÇÃO SEM RETORNO E COM PARÂMETRO

def boas_vindas(nome):
    print(f' Olá, {nome}!! Seja bem-vindo! ')

nome_digitado = input(f' Digite seu nome: ')
boas_vindas(nome_digitado)

# FUNÇÃO COM RETORNO E COM PARÂMETRO
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

resultado_soma1=  soma(2, 4)
print(resultado_soma1)
print(type(nome_digitado))
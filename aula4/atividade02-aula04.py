# ATIVIDADE 2
# Escreva um programa que dadas duas notas de 0 a 10 calcula a média aritmética entre elas.

# Função para validar nota
def ler_nota():
    while True:
        nota = float(input("Digite uma nota de 0 a 10: "))
        if 0 <= nota <= 10:
            return nota
        else:
            print("Valor inválido! Tente novamente.")

# Lendo as duas notas
nota1 = ler_nota()
nota2 = ler_nota()

# Calculando a média
media = (nota1 + nota2) / 2

# Exibindo resultado
print(f"Média = {media:.2f}")
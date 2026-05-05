num1 = float(input(f' Digite um número: '))
num2 = float(input(f' Digite um número: '))
sinal = input(f' Digite um sinal de operação (+, -, *, /): ')[0]

if sinal == "*":
    print(num1 * num2)
elif sinal == "/":
    print(num1 / num2)
elif sinal == "+":
    print(num1 + num2)
elif sinal == "-":
    print(num1 - num2)
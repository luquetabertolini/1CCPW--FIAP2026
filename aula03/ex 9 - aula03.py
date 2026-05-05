codigo_estado = int(input(f' Digite o código do estado de origem da carga de um caminhão: '))
peso = float(input(f' Digite o peso do caminhão em toneladas: '))
codigo_carga= int(input(f' Digite o código da carga (de 10 a 40): '))

peso_quilo = peso * 1000

if codigo_carga <= 20:
    preço = 100
elif codigo_carga <= 30:
    preço = 250
else:
    preço = 340

if codigo_estado == 1:
    imposto = 0.35
elif codigo_estado == 2:
    imposto = 0.25
elif codigo_estado == 3:
    imposto = 0.15
elif codigo_estado == 4:
    imposto = 0.05
elif codigo_carga == 5:
    imposto = 0

imposto_porcento = (f'{imposto*100}%')
total = preço + (preço * imposto)
print(f' O peso do caminhão é de {peso_quilo}kg.')
print(f' O preço é de: R${preço}.')
print(f' O imposto cobrado é de {imposto_porcento}.')
print(f' O valor total é de: R${preço}.')



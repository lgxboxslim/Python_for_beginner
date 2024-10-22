"""
nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10)

for valor in enumerate(nome):
    print(valor[0])

"""
"""
qtd = int(input('Quantas vezes esse loop deve rodar? '))

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')
    
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')    

nome = 'Geek University'
for letra in nome:
    print(letra, end='')

"""

# Original: U+1F60D
# Modificado: U0001F60D

for num in range(1, 11):
    print(f'{'\U0001F60D' * num}')



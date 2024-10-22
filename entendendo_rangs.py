"""
Ranges

- Precisamos conhecer o loop for para conhecer os ranges
- Precisamos conhecer o Range para trabalhar melhor com loops for

Ranges são utilizados para gerar sequencias numéricas, não de forma aleatórias,
mas sim de maneira especificada.

Formas gerais:

range(valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Forma 1
for num in range(11):
    print(num)

# Forma 2

range(valor_de_inicio, valor_de_parada)

OBS: valor_de_parada não inclusive (início padrão 0, e passo de 1 em 1)

# Exemplo forma 2

for num in range(1,11):
    print(num)

# Forma 3

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (início especificado pelo usuário, e passo especificado pelo usuário)

# Exemplo de forma 3
for num in range(5, 55, 5):
    print(num)

Forma 4 (Invesa)

range(valor_de_inicio, valor_de_parada, passo)

OBS: valor_de_parada não inclusive (inicio especificado pelo usuário e passo especificado pelo usuário)

# Exemplo forma 4
for num in range(10, 0, -1):
    print(num)
"""



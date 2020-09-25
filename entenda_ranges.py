"""
Ranges
- Precisamos conhecer o loop for para usar os ranges.
- Precisamos conhecer o range para trabalhar melhor com loops for.

Ranges são utilizados para gerar sequências numéricas não de forma aleatória, mas sim de maneira especificada.

Formas gerais:

#Forma 1
range(valor_de_parada)
Obs: valor_de_parada não inclusive (início padrão 0 e passa de 1 em 1)

#Forma 2
range(valor_de_inico, valor_de_parada)
Obs: valor_de_parada não inclusive (início especificado pelo usuário e passa de 1 em 1)

#Forma 3
range(valor_de_inico, valor_de_parada, passo)
Obs: valor_de_parada não inclusive (início especificado pelo usuário e passo especificado pelo usuário)

#Forma 4 (inversa)
range(valor_de_inico, valor_de_parada, passo)
Obs: valor_de_parada não inclusive (início especificado pelo usuário e passo especificado pelo usuário)
"""
#Exemplo forma 1
for num in range(11):
    print(num)

#Exemplo forma 2
for num in range(3, 11):
    print(num)

#Exemplo forma 3
for num in range(5, 55, 5):
    print(num)

#Exemplo forma 4 (contagem regressiva)
for num in range(10, 0, -1):
    print(num)
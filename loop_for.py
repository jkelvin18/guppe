"""
Loop for

Loop -> Estrutura de repetição.
For -> Uma dessas estruturas

C ou Java

for(int = 0; i < 10; i++) {
    //execução do loop
}

Python

for item in interavel:
    //execução do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 2, 5, 7, 9]
- Range
    numeros = range(1, 10)
range(valor_inicial, valor_final)
Obs: O valor final não é inclusive.

- Enumerate:
((0, 'G'), (1, 'e'), (2, 'e')...)

for indice, letra in enumerate(nome):
    print(nome[inidce])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)
obs: Quando não precisamos de uma valor, podemos descartá-lo utilizanod um underline (_)
"""

nome = 'Geek University'
lista = [1, 2, 5, 7, 9]
numeros = range(1, 10) #temos que transformar em uma lista

#Exemplo de for 1
for letra in nome:
    print(letra)

#Exemplo de for 2
for numero in lista:
    print(numero)

#Exemplo de for 3 (Iterando sobre um Range)
for numero in range(1, 10):
    print(numero)

#Exemplo de for 4 (enumerate)
for indice, letra in enumerate(nome):
    print(nome[indice])

#Exemplo de for 6
qtd = int(input('Quantas vezes esse loop deve rodar? '))
soma = 0
for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')
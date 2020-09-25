"""
loop while

Forma geral

while expressao_booleana:
    \\execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira
"""
#Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

#Exemplo 2

resposta = ''

while resposta != 'sim':
    print(numero)
    resposta = input('Ja acabou jessica? ')
"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String

Em Python, string é tudo que estiver entre:
 - Aspas simples;
 - Aspas duplas;
 - Aspas simples triplas;
 - Aspas duplas triplas;
"""
# Entrada de dados
nome = input('Qual o seu nome? ') # Input -> Entrada

# Exemplo de print 'antigo' 2.x
# print ('Seja bem-vindo(a) %s' % nome)

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem vindo(a) {nome}')

idade = int(input('Qual sua idade? '))

#Processamento

#Saída
#Exemplo print 'antigo' 2.x
#print( A %s tem %s anos' % (nome, idade)

#Exemplo print 'moderno' 3.x
#print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'A {nome} tem {idade} anos')

"""
#int(idade) => cast
Cast é a 'conversão' de um tipo de dado para outro
"""
print(f'A {nome} nasceu em {2018 - (idade)}')
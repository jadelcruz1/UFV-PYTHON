# aula de funções em python com def ():

"""
def imprimir():
    print('conseguir fazer uma função!')

print('O que está escrito em imprimir?')
imprimir()

"""

"""
def notas(nota_1, nota_2):
    print(f'Minha primeira nota foi {nota_1} e a segunda nota foi {nota_2}')


notas('5', '36')

"""

"""
def nomes(nome, sobrenome_1, sobrenome_2):
    print(f'Meu nome é {nome.title()}')
    print(f'Meu sobrenome são {sobrenome_1.title()} e {sobrenome_2.title()}')
    print(f'Então meu nome completo é: {nome.title()} {sobrenome_1.title()} {sobrenome_2.title()}')

nomes('jardel', 'batista', 'da cruz')

"""

def repete( tamanho, tamnho_texto):
    s = ''
    for i in range (0, tamnho_texto):
        s = s + tamanho
    return s
    
output =  repete('\n jardel, letícia, lenice ', 5)

print(output)

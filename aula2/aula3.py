import numpy as np

"""
notas = np.zeros(5, dtype=int)
print('Notas = ', notas)

"""

"""
arr = np.array([1,2,3,4,5])
print('este é meu array ', arr)

"""

#criando o tamanho do vetor
"""
n = int(input('insira o tamanho do vetor: '))
A = np.empty(n, dtype=int)
print('meu vetor é ', A)

"""

#vetor de strings

"""
a = input('Digite uma palavra: ')
print(a)

for  i in a:
    print(i)

"""

#construindo matrizes

linhas = int(input('Digite o numero de linhas que deseja: '))
colunas = int(input('Digite o número de colunas que deseja: '))

#criando a matriz
M = np.empty((linhas, colunas), dtype=int)
print(M)

#percorrer a matriz

for i in M:
 print('Minha matriz possui estes números : ', i)



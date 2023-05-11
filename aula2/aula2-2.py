#aula 2-2

""" 
numero = int(input("Digite o numero. "))

while numero <= 10:
    print(numero)

    numero += 1
    

print ("O número é: ", numero)

"""

#treino while loop de repetição

""" 
x = "\nDigite uma palavra."
x += "\n digite  'sair' para finalizar "
stop = ""

while stop != "sair":
    stop = input(x)

    print(stop)

"""

#treino loop repetição com flag active

"""
frase = "\n digite uma palavra"
frase += "\n digite sair para finalizar: "

active = True

while active:
    message = input(frase)
    if message == 'pare':
     active = False
    else:
       print(message)

"""

#treino while com continue

"""

number = int(input( "digite um número: "))
while number < 10:
    number +=1
    if number % 2 != 0:
        continue
    print(number)

"""

#treino com for para percorrer lista

"""
names = ["jardel", "Letícia", "Valentina", "claudio"]
for name in names:
    print(name)

"""

"""
for soletrar in "Jardel":
    print(soletrar)

"""

"""
for numeros in range (5):
    print(numeros)

"""

"""
for limite in range (2, 9): # no caso o numero vai de 9 menos 1 = 8
    print(limite)

"""

#pode especificar os passos da que a repetição irá pular

"""
for pular in range(0, 51, 10):
    print(pular)

"""

#ler aqruivos em python com a função open

#file1 = open("C:\Users\jarde\Desktop\Jardel Pessoal\UFV\ELT572\Teste.txt")

"""
file1 = open("Teste.txt", "r")
file1.close()



file2 = open(r"Teste.txt", "w+")
file2.close()

"""


"""
with open ("Teste.txt" , "r") as ler:
    print(ler.readlines())
"""


with open("senha.txt", 'r+') as escrever:
    escrever.write('senha nova criada e lida com r+')

#append
"""with open("senha.txt", 'a') as escrever:
    escrever.write('\nnova escrita na linha debaixo456')

    """

"""with open('senha.txt', 'r') as lerSenha:
    print(lerSenha.read())
    """

    


"""with open("Teste.txt", "w+")  as escrever_ler:
    print(escrever_ler)
    """


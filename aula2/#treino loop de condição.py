#treino loop de condição 

name = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
tempo_cnh = float(input("Digite o tempo de cnh: "))

print("nome: " + name)
print("idade", idade)
print("Tempo de CNH" , tempo_cnh)

""" 
    vamos ter duas condições para tirar a carteira D:
    idade >= 21
    e tempo de cnh > 2
"""

if tempo_cnh <= 2 or idade <= 21:
    print( name + "," " Você precisa de mais tempo.")

elif tempo_cnh >= 3 and idade <= 24:
    print(name + "," + "Voce pode habilitar na categoria A")   


else:
    print(name + "," " Você está habilitado para adicionar a categoria D!")

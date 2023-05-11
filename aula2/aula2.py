nome = input("Digite seu nome: ")
age = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))


print ("Seu nome é: " + nome)
print ("Sua idade é: ", age, "anos")
print ("Sua altura é: ", altura, "m")

#print(nome, idade, altura, sep=" ** ")

# separador será incluído somente no último impresso.
#print(nome, idade, altura, sep=" ** ", end="_") 

# estruturas condicionais

"""age = 19
if age >= 18:
     print("Obrigatório votar")
     
else:
     print("Não obrigado a votar.")""" 


#age = 171
if age < 16:
    print(" Você não pode votar")

elif age < 18:
    print("Você já pode a votar")

elif age < 70:
    print("Voto obrigatório")

else:
    print(" Você pode votar")
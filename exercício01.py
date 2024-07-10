#Questão 01
# for i in range(1, 100+1, 1):
#     print(i, end = (","))

#Questão 02
# for i in range(100, 1-1, - 1):
#     print(i, end=(" ,"))

#Questão 04

n = 10
lista_de_numeros = []

for i in range(n):
    numeros = int(input(f"Digite o número {i+1}: "))
    lista_de_numeros.append(numeros)

soma = sum(lista_de_numeros)
print(soma)




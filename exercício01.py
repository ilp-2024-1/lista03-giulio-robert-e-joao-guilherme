#Questão 01
for i in range(1, 100+1, 1):
    print(i, end = (","))

#Questão 02
for i in range(100, 1-1, - 1):
    print(i, end=(" ,"))

#Questão 03

var1 = int(input("Digite o primeiro valor: "))
var2 = int(input("Digite o segundo valor: "))

varSoma = 0

for i in range (var1, var2 +1):
    
    print(i, end=(","))
    varSoma += i
   
print("o valor do somatorio: ", varSoma)

#Questão 04

n = 10
lista_de_numeros = []

for i in range(n):
    numeros = int(input('Digite os números da lista:'))
    lista_de_numeros.append(numeros)

soma = sum(lista_de_numeros)
print(soma)

#Questão 05

valor_somatorio = 0

for i in range (5):
    valor =  int(input("Digite um valor: "))

    if valor < 10:
        valor_somatorio += valor 

print(valor_somatorio)

#Questão 07 

valor_somatorio_pares = 0

for i in range(5):
    valor = int(input("Digite um valor: "))

    if valor % 2 == 0:
        valor_somatorio_pares += valor

print("Valor somatorio é: ", valor_somatorio_pares)

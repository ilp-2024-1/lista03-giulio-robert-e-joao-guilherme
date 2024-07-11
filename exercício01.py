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

#Questão 06

somatorio = 0

for i in range (5):
    valor_usuario =  int(input("Digite um valor: "))

    if valor_usuario >= 10 and valor_usuario < 20:
        somatorio += valor_usuario
print(somatorio)


#Questão 07 

valor_somatorio_pares = 0

for i in range(5):
    valor = int(input("Digite um valor: "))

    if valor % 2 == 0:
        valor_somatorio_pares += valor
print("Valor somatorio é: ", valor_somatorio_pares)

#Questão 08

quantidade_de_valores_digitados = int(input('Quantos valores serão colocados?'))
lista_de_valores = []

for i in range(quantidade_de_valores_digitados):
    valores = int(input('Digite os números da lista:'))
    if valores % 2 == 0:
        lista_de_valores.append(valores)

print(lista_de_valores)

#Questão 10

numero_de_repetiçoes = 10
somatorio_par = 0
somatorio_impar = 0

for i in range(numero_de_repetiçoes):
    valores_inteiros = int(input('Digite os valores:'))
    if valores_inteiros % 2 == 0:
        somatorio_par += valores_inteiros
    else:
        somatorio_impar += valores_inteiros

if somatorio_impar > somatorio_par:
    print('Somatório dos números ímpares é maior')
elif somatorio_impar == somatorio_par:
    print('Somatório dos número ímpares é igual ao dos números pares.')
else:
    print('Somatório dos números ímpares é menor que o dos números pares.')



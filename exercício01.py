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



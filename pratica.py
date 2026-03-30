n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
n3 = int(input('Digite mais um número inteiro: '))
menor = n1
if n2 < menor:
   menor = n2
if n3 < menor: 
    menor = n3
print(menor)
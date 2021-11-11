num1 = input('Digite o primeiro número\n')
num2 = input('Digite o segundo número\n')
num3 = input('Digite o terceiro número\n')

numeros = (num1, num2, num3)
lista = list(numeros)
lista.sort(reverse = True)

print(lista)
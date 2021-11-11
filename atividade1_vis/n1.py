num1 = input("Digite o primeiro número\n")
num2 = input("Digite o segundo número\n")
num3 = input("Digite o terceiro número\n")

if num1 > num2 > num3:
    print(num1, num2, num3)
elif num1 > num3 > num2:
    print(num1, num3, num2)
elif num2 > num1 > num3:
    print(num2, num1, num3)
elif num2 > num3 > num1:
    print(num2, num3, num1)
elif num3 > num1 > num2:
    print(num3, num1, num2)
elif num3 > num2 > num1:
    print(num3, num2, num1)
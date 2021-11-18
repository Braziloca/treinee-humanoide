from quest3a import Calculos

num = int(input("Digite um número: "))
teste = Calculos(num)

c1 = teste.calc_quad()
print(c1)

c2 = teste.calc_cubo()
print(c2)
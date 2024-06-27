#7 - Faça um algoritmo que peça 3 lados de um triângulo, o programa irá
#verificar se é um triângulo Isósceles, Equilátero ou Escaleno.

lado1 = int(input("\nQual o primeiro lado ?:"))
lado2 = int(input("Qual o segundo lado ?:"))
lado3 = int(input("Qual o terceiro lado ?:"))



if lado1 == lado2 == lado3:
    print("Equilátero")
elif lado1 != lado2 != lado3:
    print("Escaleno")
else:
    print("Isósceles")

#6 - Faça um algoritmo que peça 3 números para o usuário e verifique qual o
#maior e menor número, mostrar também quando tiver números iguais.

numero1 = float(input("\nDigite o primeiro numero: "))
numero2 = float(input("Digite o segundo numero: "))
numero3 = float(input("Digite o terceiro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print(f"O numero {(numero1)} é maior")

if numero2 > numero1 and numero2 > numero3:
    print(f"O numero {(numero2)} é maior")

if numero3 > numero2 and numero3 > numero1:
    print(f"O numero {(numero3)} é maior")

if numero1 == numero2 == numero3:
    print(f"\nOs numeros são iguais")
    print(f"{(numero1,numero2,numero3)}")
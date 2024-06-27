#2 - Um usuário precisar saber o maior entre dois números digitados.
#Desenvolva o algoritmo que resolva isso.

numero = int(input("\nDigite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero > numero2:
    print(f"\nO numero {numero} é maior que o numero {numero2}")
else:
    print(f"\nO numero {numero2} é maior que o numero {numero}")
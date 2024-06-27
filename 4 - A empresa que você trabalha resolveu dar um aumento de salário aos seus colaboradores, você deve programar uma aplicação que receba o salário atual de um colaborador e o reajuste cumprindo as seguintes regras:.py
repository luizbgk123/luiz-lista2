#4 - A empresa que você trabalha resolveu dar um aumento de salário aos
#seus colaboradores, você deve programar uma aplicação que receba o
#salário atual de um colaborador e o reajuste cumprindo as seguintes regras:

salario = int(input("\nQual o salario que você recebe: "))

if salario <= 280:
    reajuste = salario * 1.2 - salario
    print("Salario antes do reajuste" ,salario)
    print("O aumento sera de 20%")
    print("O reajuste será de" ,reajuste)
    print("com o reajuste seu salario será" ,salario * 1.2)

elif salario >= 281 and salario <= 700:
    reajuste = salario * 1.15 - salario
    print("Salario antes do reajuste" ,salario)
    print("O aumento sera de 20%")
    print("O reajuste será de" ,reajuste)
    print("com o reajuste seu salario será" ,salario * 1.15)

elif salario >= 701 and salario <= 1500:
    reajuste = salario * 1.1 - salario
    print("Salario antes do reajuste" ,salario)
    print("O aumento sera de 20%")
    print("O reajuste será de" ,reajuste)
    print("com o reajuste seu salario será" ,salario * 1.1)

elif salario >= 1501:
    reajuste = salario * 1.05 - salario
    print("Salario antes do reajuste" ,salario)
    print("O aumento sera de 20%")
    print("O reajuste será de" ,reajuste)
    print("com o reajuste seu salario será" ,salario * 1.05)
    
    